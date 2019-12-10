^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ari_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------

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
