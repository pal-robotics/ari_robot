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

from launch import LaunchDescription
from launch_pal.include_utils import include_launch_py_description

from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase
from launch.actions import DeclareLaunchArgument
from launch_pal.robot_arguments import CommonArgs
from ari_description.launch_arguments import AriArgs

from dataclasses import dataclass

@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    robot_model: DeclareLaunchArgument = AriArgs.robot_model
    laser_model: DeclareLaunchArgument = AriArgs.laser_model
    end_effector: DeclareLaunchArgument = AriArgs.end_effector
    head_camera_model: DeclareLaunchArgument = AriArgs.head_camera_model
    torso_front_camera_model: DeclareLaunchArgument = AriArgs.torso_front_camera_model
    torso_back_camera_model: DeclareLaunchArgument = AriArgs.torso_back_camera_model
    

    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    namespace: DeclareLaunchArgument = CommonArgs.namespace

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

    default_controllers = include_launch_py_description(
        pkg_name="ari_controller_configuration", paths=[
        "launch", "default_controllers.launch.py"],
        launch_arguments={
            "robot_model": launch_args.robot_model,
        },
    )

    launch_description.add_action(default_controllers)

    play_motion2 = include_scoped_launch_py_description(
        pkg_name="ari_bringup",
        paths=["launch", "ari_play_motion2.launch.py"],
        launch_arguments={
            "robot_model": launch_args.robot_model,
        },
    )

    launch_description.add_action(play_motion2)

    twist_mux = include_scoped_launch_py_description(
        pkg_name="ari_bringup",
        paths=["launch", "twist_mux.launch.py"],
        launch_arguments={
            "cmd_vel_out": "mobile_base_controller/cmd_vel_unstamped",
            # "config_locks": config_locks_file,
            # "config_topics": config_topics_file,
            # "config_joy": joystick_file,
        },

    )

    launch_description.add_action(twist_mux)

    robot_state_publisher = include_scoped_launch_py_description(
        pkg_name="ari_description",
        paths=["launch", "robot_state_publisher.launch.py"],
        launch_arguments={
            "robot_model": launch_args.robot_model,
        },
    )

    launch_description.add_action(robot_state_publisher)

    return

