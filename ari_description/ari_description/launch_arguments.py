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
from launch.actions import DeclareLaunchArgument as DLA
from launch_pal.arg_utils import parse_launch_args_from_yaml
from ament_index_python.packages import get_package_share_directory


@dataclass(frozen=True)
class AriArgs:
    """This dataclass contains launch arguments for ARI."""

    __robot_name = 'ari'
    __pkg_dir = get_package_share_directory(f"{__robot_name}_description")
    __arg_creator = parse_launch_args_from_yaml(
        f"{__pkg_dir}/config/{__robot_name}_configuration.yaml")

    robot_model: DLA = __arg_creator.get_argument('robot_model')
    laser_model: DLA = __arg_creator.get_argument('laser_model')
    end_effector: DLA = __arg_creator.get_argument('end_effector')
    head_camera_model: DLA = __arg_creator.get_argument('head_camera_model')
    torso_front_camera_model: DLA = __arg_creator.get_argument('torso_front_camera_model')
    torso_back_camera_model: DLA = __arg_creator.get_argument('torso_back_camera_model')
