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
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, SetLaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.robot_arguments import CommonArgs
from ari_description.launch_arguments import AriArgs
from dataclasses import dataclass
from launch_ros.actions import Node


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    robot_model: DeclareLaunchArgument = AriArgs.robot_model
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time


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
    # Create the extra configs from the base_type LA
    launch_description.add_action(OpaqueFunction(function=create_joystick_file_config))

    pkg_dir = get_package_share_directory("ari_bringup")

    config_locks_file = os.path.join(
        pkg_dir, "config", "twist_mux", "twist_mux_locks.yaml"
    )
    config_topics_file = os.path.join(
        pkg_dir, "config", "twist_mux", "twist_mux_topics.yaml"
    )

    joystick_file = os.path.join(pkg_dir, "config", "joy_teleop", "joy_config.yaml")

    twist_mux = include_scoped_launch_py_description(
        'twist_mux', ['launch', 'twist_mux_launch.py'],
        launch_arguments={
            'cmd_vel_out': 'mobile_base_controller/cmd_vel_unstamped',
            'config_locks': config_locks_file,
            'config_topics': config_topics_file,
            "config_joy": joystick_file,
            'use_sim_time': launch_args.use_sim_time,
        }
    )

    launch_description.add_action(twist_mux)

    twist_mux_analyzer = Node(
        package='diagnostic_aggregator',
        executable='add_analyzer',
        namespace='twist_mux',
        output='screen',
        emulate_tty=True,
        parameters=[
            os.path.join(pkg_dir, 'config', 'twist_mux', 'twist_mux_analyzers.yaml')
        ],
    )

    launch_description.add_action(twist_mux_analyzer)

    return


def create_joystick_file_config(context, *args, **kwargs):

    pkg_dir = get_package_share_directory("ari_bringup")

    joystick_file = os.path.join(
        pkg_dir, "config", "joy_teleop", "joy_config.yaml"
    )

    return [SetLaunchConfiguration("config_joy", joystick_file)]
