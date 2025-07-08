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

from dataclasses import dataclass
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_pal.arg_utils import LaunchArgumentsBase
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from ari_description.launch_arguments import AriArgs
from launch.actions import DeclareLaunchArgument, SetLaunchConfiguration, OpaqueFunction
from ari_description.ari_launch_utils import get_ari_hw_suffix
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import read_launch_argument
from launch_pal.robot_arguments import CommonArgs
from launch_pal.param_utils import merge_param_files


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    robot_model: DeclareLaunchArgument = AriArgs.robot_model
    #arm_type: DeclareLaunchArgument = AriArgs.arm_type


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


    play_motion2 = include_scoped_launch_py_description(
        pkg_name="play_motion2",
        paths=["launch", "play_motion2.launch.py"],
        launch_arguments={
            "motions_file": motions_file_path,
            "motion_planner_config": motion_planner_file_path
        }.items(),
    )

    launch_description.add_action(play_motion2)

    return


def create_play_motion_params(context):

    pkg_name = "ari_bringup"
    pkg_share_dir = get_package_share_directory(pkg_name)
    robot_model = read_launch_argument("robot_model", context)

    hw_suffix = get_ari_hw_suffix(robot_model=robot_model)   

    head_motions = PathJoinSubstitution(
        [pkg_share_dir, "config", "motions", "ari_motions_head.yaml"]
    )

    if arm != 'no-arm':

        general_yaml = PathJoinSubstitution(
            [pkg_share_dir, "config", "motions", "ari_motions_general.yaml"]
        )
        if end_effector == 'no-end-effector':
            merged_yaml = general_yaml
        else:
            motions_yaml = PathJoinSubstitution(
                [pkg_share_dir, "config", "motions", f"ari_motions{hw_suffix}.yaml"]
            )
            merged_yaml = merge_param_files([motions_yaml.perform(context),
                                             general_yaml.perform(context),
                                             head_motions.perform(context)])
    else:
        merged_yaml = PathJoinSubstitution(
            [pkg_share_dir, "config", "motions", f"ari_motions{hw_suffix}.yaml"]
        )

    motion_planner_file = f"motion_planner{hw_suffix}.yaml"
    motion_planner_config = PathJoinSubstitution(
        [pkg_share_dir, "config", "motion_planner", motion_planner_file]
    )

    return [
        SetLaunchConfiguration("motions_file", merged_yaml),
        SetLaunchConfiguration("motion_planner_config", motion_planner_config),
    ]

