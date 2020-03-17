^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ari_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
