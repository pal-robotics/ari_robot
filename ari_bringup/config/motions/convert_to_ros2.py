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

import sys
import yaml

NB_JOINTS = 0


def fix_positions(p):
    global NB_JOINTS

    res = {}
    res["joints"] = p["joints"]
    NB_JOINTS = len(res["joints"])
    if "meta" in p:
        res["meta"] = p["meta"]
    res["positions"] = []
    res["times_from_start"] = []
    for e in p["points"]:
        res["positions"] += [float(x) for x in e["positions"]]
        res["times_from_start"].append(float(e["time_from_start"]))
    return res


with open(sys.argv[1], "r") as f:
    data = yaml.load(f, yaml.Loader)
    motions = data["play_motion"]["motions"]
    print(motions)
    ros2_motions = {}
    for m, p in motions.items():
        if "points" in p:
            ros2_motions[m] = fix_positions(p)

        else:
            ros2_motions[m] = p

    with open("ros2_" + sys.argv[1], "w") as output:
        # yaml.dump(ros2_motions, output)

        res = {"/play_motion2": {"ros__parameters": {"motions": ros2_motions}}}
        yaml.dump(
            res,
            output,
            width=NB_JOINTS,
            default_flow_style=None,
        )
