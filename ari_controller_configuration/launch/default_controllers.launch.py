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
from launch.actions import OpaqueFunction
from launch_pal.arg_utils import read_launch_argument
from launch_pal.include_utils import include_launch_py_description
from launch_pal.robot_utils import (
    get_robot_model,
    get_robot_name,
)


def declare_robot_args(context, *args, **kwargs):

    robot_name = read_launch_argument("robot_name", context)

    return [
        get_robot_model(robot_name),
    ]


def generate_launch_description():

    mobile_base_controller_launch = include_launch_py_description(
        "ari_controller_configuration", [
            "launch", "mobile_base_controller.launch.py"]
    )

    joint_state_broadcaster_launch = include_launch_py_description(
        "ari_controller_configuration",
        ["launch", "joint_state_broadcaster.launch.py"],
    )

    head_controller_launch = include_launch_py_description(
        'ari_controller_configuration',
        ['launch', 'head_controller.launch.py'])

    arm_left_controller_launch = include_launch_py_description(
        'ari_controller_configuration',
        ['launch', 'arm_left_controller.launch.py'])

    arm_right_controller_launch = include_launch_py_description(
        'ari_controller_configuration',
        ['launch', 'arm_right_controller.launch.py'])

    # @TODO: current limit controllers

    ld = LaunchDescription()

    ld.add_action(get_robot_name("ari"))
    ld.add_action(OpaqueFunction(function=declare_robot_args))

    ld.add_action(mobile_base_controller_launch)
    ld.add_action(joint_state_broadcaster_launch)
    ld.add_action(head_controller_launch)
    ld.add_action(arm_left_controller_launch)
    ld.add_action(arm_right_controller_launch)

    return ld
