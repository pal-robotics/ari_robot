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
from dataclasses import dataclass
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_pal.arg_utils import LaunchArgumentsBase
from launch.substitutions import LaunchConfiguration
from ari_description.launch_arguments import AriArgs
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration, OpaqueFunction
from ari_description.ari_launch_utils import get_ari_hw_suffix
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import read_launch_argument


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    robot_model: DeclareLaunchArgument = AriArgs.robot_model


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()
    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(
    launch_description: LaunchDescription, launch_args: LaunchArguments
):
    launch_description.add_action(OpaqueFunction(function=create_play_motion_params))

    play_motion2 = include_scoped_launch_py_description(
        pkg_name="play_motion2",
        paths=["launch", "play_motion2.launch.py"],
        launch_arguments={
            "motions_file": LaunchConfiguration("motions_file"),
            "motion_planner_config": LaunchConfiguration("motion_planner_config"),
        },
    )

    launch_description.add_action(play_motion2)

    return


def create_play_motion_params(context):

    robot_model = read_launch_argument("robot_model", context)

    hw_suffix = get_ari_hw_suffix(robot_model=robot_model)

    motion_planner_file = f"motion_planner_ari{hw_suffix}.yaml"

    motion_planner_file_path = os.path.join(
        get_package_share_directory("ari_bringup"),
        "config", "motion_planner", motion_planner_file
    )

    motions_file = f"ari{hw_suffix}_motions.yaml"
    motions_file_path = os.path.join(
        get_package_share_directory("ari_bringup"), "config", "motions", motions_file
    )

    return [
        SetLaunchConfiguration("motions_file", motions_file_path),
        SetLaunchConfiguration("motion_planner_config", motion_planner_file_path),
    ]
