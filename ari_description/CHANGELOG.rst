^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ari_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------

0.0.52 (2023-01-23)
-------------------

0.0.51 (2022-12-15)
-------------------
* Merge branch 'new-lidar-frame' into 'ferrum-devel'
  Update lidar frame in case of ari-v2
  See merge request robots/ari_robot!58
* Update lidar frame in case of ari-v2
* Contributors: David ter Kuile, davidfernandez

0.0.50 (2022-11-17)
-------------------
* Merge branch 'feat/ydlidar' into 'ferrum-devel'
  added support to ydlidar
  See merge request robots/ari_robot!54
* added support to ydlidar 15 and 30
* added support to ydlidar
* Contributors: antoniobrandi

0.0.49 (2022-10-24)
-------------------

0.0.48 (2022-07-27)
-------------------

0.0.47 (2022-06-27)
-------------------
* Merge branch 'extrinsics-fix-in-public-sim' into 'ferrum-devel'
  set nominal extrinsics as param
  See merge request robots/ari_robot!48
* change parameter name
* set nominal extrinsics as param
* Contributors: saikishor, saracooper

0.0.46 (2022-06-09)
-------------------
* Merge branch 'ari-v2' into 'ferrum-devel'
  Ari v2
  See merge request robots/ari_robot!46
* Update collision_parameters with new caster link
* Fix ari base simulation wheels/caster
* Fix CoM for arm_right_1_link
* Contributors: David ter Kuile, Luca Marchionni, davidfernandez

0.0.45 (2022-06-08)
-------------------

0.0.44 (2022-06-07)
-------------------
* Merge branch 'eye-frames' into 'ferrum-devel'
  added frames for eyes of ari
  See merge request robots/ari_robot!43
* Change link names and z-axis pointing up now
* added frames for eyes of ari
* Contributors: David ter Kuile, davidfernandez

0.0.43 (2022-05-30)
-------------------
* Merge branch 'ari-v2' into 'ferrum-devel'
  Ari v2
  See merge request robots/ari_robot!42
* Combine base torso and head urdf files for v1 and v2
* update joint limits
* Update joint limits and wheel radius
* Update inertia of caster v2 in urdf
* Update collision geometry for docking link
* Remove docking and head base stl to avoid collision errors
* set correct joint limits
* Add frame for hand
* Update rviz and change arg order in test_ari.test
* Update launch files and add meshes
* update and delete xacro files
* update head camera
* replace version with robot_model
* fix bug in test
* fix bug in test
* typo in test
* add v2 to ari-description tests
* update stl and urdf for sensor and wheels
* Set joint rotation direction correctly for both arms
* Mirror arms succeeded
* Left arm_v2 correct
* new_arm direct copy of left-arm.urdf
* reflect arm_base_link in z-axis
* include urdf for ari_v2
* Contributors: David ter Kuile, davidfernandez

0.0.42 (2021-11-02)
-------------------
* Merge branch 'thermal-camera' into 'ferrum-devel'
  add has thermal parameter and tf link
  See merge request robots/ari_robot!40
* add has thermal parameter and tf link
* Contributors: Sara Cooper, davidfernandez

0.0.41 (2021-10-05)
-------------------
* Merge branch 'fisheye_pc_connect_option' into 'ferrum-devel'
  added the PC option to the valid fisheye connection check
  See merge request robots/ari_robot!39
* added the PC option to the valid fisheye connection check
* Contributors: Sai Kishor Kothakota, victor

0.0.40 (2021-10-05)
-------------------
* Proper handling of string parameters for fisheye camera
* Contributors: Victor Lopez

0.0.39 (2021-08-19)
-------------------
* Correct front fisheye pitch to new pose
* Contributors: davidfernandez

0.0.38 (2021-08-19)
-------------------
* Merge branch 'add-spring-cameras' into 'ferrum-devel'
  Add spring cameras
  See merge request robots/ari_robot!38
* Use separated fisheye params
* Contributors: davidfernandez, saikishor

0.0.37 (2021-08-16)
-------------------
* Merge branch 'laser_iso_fix' into 'ferrum-devel'
  Added fixed frame to the urdf with the position of the docking interface for...
  See merge request robots/ari_robot!37
* URDF distance accuracy
* Updated docking_link distance based on mechanical specifications
* reduced a bit the docking frame in order to guarantee that the parking planner is alway able to park
* Added fixed frame to the urdf with the position of the docking interface for the parking planner node
* Contributors: antoniobrandi, saikishor

0.0.36 (2021-08-05)
-------------------

0.0.35 (2021-07-28)
-------------------
* Merge branch 'fixing_laser_model' into 'ferrum-devel'
  fixing laser_model set default false
  See merge request robots/ari_robot!35
* Rename camera param and pass laser
* fixing laser_model set default false
* Update laser distances
* Contributors: antoniobrandi, davidfernandez, saikishor, sergiomoyano

0.0.34 (2021-05-20)
-------------------
* Merge branch 'ari_laser_new' into 'ferrum-devel'
  Added laser_model dependencies
  See merge request robots/ari_robot!34
* Update ari_description/robots/upload.launch
* Update ari_description/robots/ari.urdf.xacro
* Update ari_description/robots/upload.launch
* Added laser_model dependencies
* Added laser_model dependencies
* Contributors: davidfernandez, sergiomoyano

0.0.33 (2021-04-07)
-------------------
* Merge branch 'head-realsense' into 'ferrum-devel'
  Head realsense optional camera
  See merge request robots/ari_robot!33
* Modify URDF for head camera and fix topic names
* Fix urdf structure
* Add camera model param and fix location
* Modify URDF to include optional head realsense camera, location still to be defined
* Contributors: Sara Cooper, davidfernandez

0.0.32 (2021-03-16)
-------------------
* Merge branch 'ari3-laser' into 'ferrum-devel'
  Ari3 laser
  See merge request robots/ari_robot!32
* fixing stuff
* Change to support sick-571 laser in ari3
* Change to support sick-571 laser in ari3
* Contributors: Federico Nardi, Software Engineer, federiconardi

0.0.31 (2020-11-09)
-------------------
* Add Led frames
* Merge branch 'collision-meshes' into 'ferrum-devel'
  Collision meshes
  See merge request robots/ari_robot!28
* Remove duplicated vertices
* Add collision meshes
* Contributors: Victor Lopez, victor

0.0.30 (2020-10-05)
-------------------

0.0.29 (2020-09-21)
-------------------
* Merge branch 'hand_limits' into 'ferrum-devel'
  reduce the hand limits from 90deg to 75deg
  See merge request robots/ari_robot!26
* reduce the hand limits from 90deg to 75deg
* Contributors: saikishor, victor

0.0.28 (2020-08-31)
-------------------
* Merge branch 'spring_cameras' into 'ferrum-devel'
  Add SPRING cameras
  See merge request robots/ari_robot!25
* Add SPRING cameras
* Contributors: davidfernandez, victor

0.0.27 (2020-08-17)
-------------------
* Fix typo
* Contributors: Victor Lopez

0.0.26 (2020-08-17)
-------------------
* Add eps to head_2 upper limit
* Contributors: Victor Lopez

0.0.25 (2020-07-30)
-------------------
* Reduce head_2 upper limit to avoid collisions at head_1 limits
* Contributors: Victor Lopez

0.0.24 (2020-07-16)
-------------------

0.0.23 (2020-07-14)
-------------------

0.0.22 (2020-07-10)
-------------------

0.0.21 (2020-07-10)
-------------------

0.0.20 (2020-06-16)
-------------------

0.0.19 (2020-06-16)
-------------------

0.0.18 (2020-05-29)
-------------------
* Merge branch 'revert-upstream-update' into 'ferrum-devel'
  Revert "Merge branch 'update-upstream' into 'ferrum-devel'"
  See merge request robots/ari_robot!24
* Revert "Merge branch 'update-upstream' into 'ferrum-devel'"
  This reverts commit 0f64cd8488e644d55e21542c365b7a8f4bf5593c, reversing
  changes made to 4724b645f7866d510ed2a5d2face514229bfbc89.
* Contributors: Procópio Stein, procopiostein

0.0.17 (2020-05-19)
-------------------
* Merge branch 'update-upstream' into 'ferrum-devel'
  added new argument due to realsense update from upstream
  See merge request robots/ari_robot!23
* added new argument due to realsense update from upstream
* Contributors: Procópio Stein, procopiostein

0.0.16 (2020-03-24)
-------------------
* Merge branch 'actuated_hand_fix' into 'ferrum-devel'
  Actuated hand fix
  See merge request robots/ari_robot!20
* Fix dependencies
* Fix test for hands
* Separate both end effectors
* Add parameter for end_effector
* Fix color fingers in Gazebo visualization
* fix parameter value
* add hand joints and transmission for underactuation
* Fixed left and right meshes with new fingers joints
* Contributors: Luca Marchionni, YueErro, davidfernandez

0.0.15 (2020-03-17)
-------------------
* move rgbd laser frame farther
* Merge branch 'cleaned-up-ari-robot' into 'ferrum-devel'
  Clean up ari robot package
  See merge request robots/ari_robot!18
* Clean up ari robot package
* Contributors: Procópio Stein, alessandrodifava, saracooper

0.0.14 (2020-02-12)
-------------------
* Revert "Merge branch 'actuated_hand' into 'master'"
  This reverts commit 77bb9145c11c51669c2cfe5737fe9ab58d18a87f, reversing
  changes made to 2024a1af4ec1c5f3101956f4c0dbb370cfde1479.
* Merge branch 'correct-laser-frame' into 'ferrum-devel'
  changed rgbd link to base urdf
  See merge request robots/ari_robot!17
* changed rgbd link to base urdf
* Merge branch 'updated-ari-urdf' into 'master'
  Updated URDF file to include rgbd_laser_link
  See merge request robots/ari_robot!13
* Add rgbd_laser_joint and rgbd_laser_link to ari.urdfx.xacrio
* Merge branch 'actuated_hand' into 'master'
  Actuated hand
  See merge request robots/ari_robot!11
* Fix color fingers in Gazebo visualization
* Merge branch 'ari_gazebo_friction_fix' into 'master'
  Tuned again the friction of the caster wheels
  See merge request robots/ari_robot!16
* Tuned again the friction of the caster wheels
* Tuned the friction of the caster wheels
* Merge branch 'ari_gazebo_friction_fix' into 'master'
  Tuned the friction of the caster wheels
  See merge request robots/ari_robot!15
* fix parameter value
* add hand joints and transmission for underactuation
* Fixed left and right meshes with new fingers joints
* Contributors: Europrojects, Luca Marchionni, Procópio Stein, YueErro, alessandrodifava

0.0.13 (2020-02-04)
-------------------
* Merge branch 'ari_gazebo_friction_fix' into 'master'
  Fixed the friction parameters for the wheels and the caster wheels for the...
  See merge request robots/ari_robot!14
* Fixed the friction parameters for the wheels and the caster wheels for the simulation, before this the robot was not rotating well
* Contributors: Victor Lopez, alessandrodifava

0.0.12 (2020-01-22)
-------------------
* Add required dependency
* Contributors: Victor Lopez

0.0.11 (2020-01-14)
-------------------

0.0.10 (2020-01-09)
-------------------
* Rename head front camera topic name
* Contributors: Victor Lopez

0.0.9 (2020-01-07)
------------------
* Merge branch 'restore-torso-back-camera-tf' into 'master'
  Restore torso back camera transform
  See merge request robots/ari_robot!10
* Restore torso back camera transform
* Contributors: Victor Lopez

0.0.8 (2019-12-17)
------------------
* Merge branch 'ari_back_camera' into 'master'
  Removed the torso back camera frames coordinates because it will be put in a...
  See merge request robots/ari_robot!9
* Removed the torso back camera frames coordinates because it will be put in a static transform in the torso_back_camera launch
* Contributors: Victor Lopez, alessandrodifava

0.0.7 (2019-12-10)
------------------

0.0.6 (2019-12-10)
------------------
* Merge branch 'realsense_description' into 'master'
  added URDF from realsense2_description and its dependency
  See merge request robots/ari_robot!3
* added URDF from realsense2_description and its dependency
* Contributors: Sai Kishor Kothakota, Victor Lopez

0.0.5 (2019-12-03)
------------------
* Added realsense gazebo plugin dependency
* Contributors: Jordan Palacios

0.0.4 (2019-11-15)
------------------
* Merge branch 'rpi_plugin' into 'master'
  Update Rpi camera plugin to use the parsed frame
  See merge request robots/ari_robot!5
* Update Rpi camera plugin to use the parsed frame
* Merge branch 'head_optic_frame' into 'master'
  added head_front_camera_optic_frame
  See merge request robots/ari_robot!4
* added head_front_camera_optic_frame
* Contributors: Sai Kishor Kothakota, Victor Lopez

0.0.3 (2019-11-14)
------------------
* Merge branch 'ari_moveit' into 'master'
  Ari moveit
  See merge request robots/ari_robot!1
* Revert "fix Raspi camera frame orientation"
  This reverts commit 1b4612c5b6826d16f8e8d936be78decd74e0ae8a.
* fix Raspi camera frame orientation
* Added the gazebo plugin for head_front_camera
* Invert right arm axis of rotation signs
* fix warnings with the meshes
* Contributors: Jordan Palacios, Luca Marchionni, Sai Kishor Kothakota

0.0.2 (2019-11-08)
------------------
* Remove dynamixel node
* Merge branch 'master' of gitlab:robots/ari_robot
* Added ari description test
* Contributors: Victor Lopez, alessandrodifava

0.0.1 (2019-11-06)
------------------
* Added also the right arm and tuned the config files for the arms
* Added the left arm
* Added the head limit and the microphone urdf
* Fixed bugs and added the camera launch in the bringup and the microphone urdf
* Added the caster wheels, modified the urdf files, fixed the problem with the head_1_joint, added the head_camera
* Fixed bugs and parameters
* Created the bringup and the controller configuration and added the t265 camera to the back of the torso
* Added the trasmission xacro files and the gazebo tags in the urdf files
* Added the urdf files for the robot and got a first version shown on rviz
* starting the package adding the metapackage
* Contributors: alessandrodifava
