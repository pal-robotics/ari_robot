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


def get_ari_hw_suffix(robot_model="v2", camera_model=None):
    """
    Generate a substitution that creates a text suffix combining the specified ARI arguments.

    The arguments are read as string

    For instance, the suffix for: arm=right-arm, end_effector='pal-gripper', ft_sensor='schunk-ft'
    would be 'pal-gripper_schunk-ft'
    """
    suffixes = [robot_model]
    if camera_model:
        suffixes.append(camera_model)

    return "_" + "_".join(suffixes)
