# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_pal.arg_utils import LaunchArgumentsBase
from launch.substitutions import LaunchConfiguration

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    cmd_vel: DeclareLaunchArgument = DeclareLaunchArgument(
        name="cmd_vel",
        default_value="input_joy/cmd_vel",
        description="Joystick cmd_vel topic",
    )


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(
    launch_description: LaunchDescription, launch_args: LaunchArguments
):

    pkg_dir = get_package_share_directory("ari_bringup")
    pkg_path = os.path.join(pkg_dir, "config", "joy_teleop", "joy_teleop.yaml")

    joy_node = Node(
        package="joy_linux",
        executable="joy_linux_node",
        name="joystick",
        parameters=[os.path.join(pkg_dir, "config", "joy_teleop", "joy_config.yaml")],
    )

    launch_description.add_action(joy_node)

    joystick_analyzer = Node(
        package='diagnostic_aggregator',
        executable='add_analyzer',
        namespace='joystick',
        output='screen',
        emulate_tty=True,
        parameters=[
            os.path.join(pkg_dir, 'config', 'joy_teleop', 'joystick_analyzers.yaml')
        ],
    )

    launch_description.add_action(joystick_analyzer)

    head_incrementer_server = Node(
        package="joy_teleop",
        executable="incrementer_server",
        name="incrementer",
        namespace="head_controller",
        remappings=[('joint_trajectory', 'safe_command')]
    )

    launch_description.add_action(head_incrementer_server)

    joy_teleop_node = Node(
       package='joy_teleop',
       executable='joy_teleop',
       parameters=[pkg_path],
       remappings=[('cmd_vel', LaunchConfiguration('cmd_vel'))],
    )

    launch_description.add_action(joy_teleop_node)

    return
