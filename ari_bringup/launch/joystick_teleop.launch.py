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
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration, OpaqueFunction
from launch_ros.actions import Node
from launch_pal.arg_utils import LaunchArgumentsBase

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
    launch_description.add_action(OpaqueFunction(function=create_joy_teleop_filename))

    declare_cmd_vel = DeclareLaunchArgument(
        "cmd_vel",
        default_value="input_joy/cmd_vel",
        description="Joystick cmd_vel topic",
    )

    launch_description.add_action(declare_cmd_vel)

    pkg_dir = get_package_share_directory("ari_bringup")

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

    return


def create_joy_teleop_filename(context):

    pkg_dir = get_package_share_directory("ari_bringup")

    joy_teleop_file = f'{"joy_teleop.yaml"}'

    joy_teleop_path = os.path.join(
        pkg_dir,
        "config",
        "joy_teleop",
        joy_teleop_file,
    )

    return [SetLaunchConfiguration("teleop_config", joy_teleop_path)]
