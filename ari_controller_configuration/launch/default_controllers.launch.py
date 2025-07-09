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
from launch.actions import GroupAction, OpaqueFunction

from controller_manager.launch_utils import generate_load_controller_launch_description
from launch.actions import DeclareLaunchArgument
from launch_pal.arg_utils import read_launch_argument, LaunchArgumentsBase
from launch_pal.include_utils import include_launch_py_description
from launch.substitutions import PythonExpression, LaunchConfiguration
from launch_pal.robot_arguments import CommonArgs
from ari_description.launch_arguments import AriArgs

from launch.conditions import (
    LaunchConfigurationNotEquals,
    IfCondition,
    UnlessCondition
)

from ari_description.ari_launch_utils import get_ari_hw_suffix

@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    robot_model: DeclareLaunchArgument = AriArgs.robot_model
    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    namespace: DeclareLaunchArgument = CommonArgs.namespace


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
    # Create the extra configs from the LAs
    pkg_share_folder = get_package_share_directory(
        "ari_controller_configuration")

    # launch_description.add_action(
    #     OpaqueFunction(function=launch_mobile_base_controller))

    # Joint state broadcast

    joint_state_broadcaster = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="joint_state_broadcaster",
                controller_params_file=os.path.join(
                    get_package_share_directory("ari_controller_configuration"),
                    "config", 
                    f"joint_state_broadcaster{get_ari_hw_suffix(robot_model='v2')}.yaml",
                ),
            )
        ],
    )
    launch_description.add_action(joint_state_broadcaster)

    # Head controller
    head_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name="head_controller",
                controller_params_file=os.path.join(
                get_package_share_directory('ari_controller_configuration'),
                'config', 'head_controller.yaml'))
        ],
        forwarding=False,
    )

    launch_description.add_action(head_controller)

    # Arm left controller
    arm_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name='arm_left_controller',
                controller_params_file=os.path.join(
                    get_package_share_directory('ari_controller_configuration'),
                    'config', 'arm_left_controller.yaml'))

        ],
        forwarding=False,
        #condition=LaunchConfigurationNotEquals("arm_type", "no-arm"),
    )

    launch_description.add_action(arm_controller)

    # Arm right controller
    arm_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name='arm_right_controller',
                controller_params_file=os.path.join(
                get_package_share_directory('ari_controller_configuration'),
                'config', 'arm_right_controller.yaml'))

        ],
        forwarding=False,
        #condition=LaunchConfigurationNotEquals("arm_type", "no-arm"),
    )

    launch_description.add_action(arm_controller)

    # Base controller
    controller_file = os.path.join('mobile_base_controller.yaml')
    base_config_file = os.path.join(pkg_share_folder, 'config', controller_file)

    base_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name='mobile_base_controller',
                controller_params_file=LaunchConfiguration(base_config_file)
            )
        ],
    )
    launch_description.add_action(base_controller)

    return

# def set_base_config_file(context):

#     is_public_sim = read_launch_argument("is_public_sim", context)
#     pkg_share_folder = get_package_share_directory('ari_controller_configuration')

#     controller_file = 'mobile_base_controller.yaml'

#     if is_public_sim in ['true', 'True']:
#         controller_file = 'mobile_base_controller_public_sim.yaml'

#     base_config_file = os.path.join(pkg_share_folder, 'config', controller_file)

#     return [SetLaunchConfiguration("base_config_file", base_config_file)]



# def launch_mobile_base_controller(context, *args, **kwargs):

#     default_config = os.path.join(
#         get_package_share_directory("ari_controller_configuration"),
#         "config",
#         "mobile_base_controller.yaml",
#     )

#     calibration_config = "/etc/calibration/master_calibration.yaml"

#     if os.path.exists(calibration_config):
#         params_file = merge_param_files([default_config, calibration_config])
#     else:
#         params_file = default_config

#     return generate_load_controller_launch_description(
#         controller_name="mobile_base_controller",
#         controller_params_file=params_file,
#     )


