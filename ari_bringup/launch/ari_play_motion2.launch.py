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
from launch.actions import OpaqueFunction

from launch_pal.arg_utils import read_launch_argument
from launch_pal.include_utils import include_launch_py_description
from launch_pal.robot_utils import get_robot_model, get_robot_name

from ari_description.ari_launch_utils import get_ari_hw_suffix


def declare_args(context, *args, **kwargs):

    robot_name = read_launch_argument("robot_name", context)

    return [get_robot_model(robot_name)]


def launch_setup(context, *args, **kwargs):

    robot_model = read_launch_argument("robot_model", context)

    motion_planner_file = \
        f"motion_planner_ari{get_ari_hw_suffix(robot_model=robot_model)}.yaml"
    motion_planner_file_path = os.path.join(
        get_package_share_directory("ari_bringup"),
        "config", "motion_planner", motion_planner_file
    )

    motions_file = f"ari{get_ari_hw_suffix(robot_model=robot_model)}_motions.yaml"
    motions_file_path = os.path.join(
        get_package_share_directory("ari_bringup"), "config", "motions", motions_file
    )

    play_motion2 = include_launch_py_description(
        "play_motion2",
        ["launch", "play_motion2.launch.py"],
        launch_arguments={
            "motions_file": motions_file_path,
            "motion_planner_config": motion_planner_file_path
        }.items(),
    )

    return [play_motion2]


def generate_launch_description():

    ld = LaunchDescription()

    # Declare arguments
    # we use OpaqueFunction so the callbacks have access to the context
    ld.add_action(get_robot_name("ari"))
    ld.add_action(OpaqueFunction(function=declare_args))

    # Launch play_motion2 with the proper config
    ld.add_action(OpaqueFunction(function=launch_setup))

    return ld
