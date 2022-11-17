^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ari_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.50 (2022-11-17)
-------------------

0.0.49 (2022-10-24)
-------------------
* Merge branch 'feat/robust-odometry-integration' into 'ferrum-devel'
  disabled odom tf publication
  See merge request robots/ari_robot!55
* disabled odom tf publication
* Contributors: josegarcia

0.0.48 (2022-07-27)
-------------------
* Merge branch 'approach_planner_v2' into 'ferrum-devel'
  Modify the approach_planner config for ARI v2
  See merge request robots/ari_robot!49
* Modify the approach_planner config for ARI v2
* Contributors: davidfernandez, saikishor

0.0.47 (2022-06-27)
-------------------

0.0.46 (2022-06-09)
-------------------

0.0.45 (2022-06-08)
-------------------
* Merge branch 'update-shake-left-motion' into 'ferrum-devel'
  update shake-left
  See merge request robots/ari_robot!45
* update shake-left
* Contributors: David ter Kuile, davidfernandez

0.0.44 (2022-06-07)
-------------------

0.0.43 (2022-05-30)
-------------------
* Merge branch 'ari-v2' into 'ferrum-devel'
  Ari v2
  See merge request robots/ari_robot!42
* update joint limits
* update motions for new joint limits of ari-v2
* Update rviz and change arg order in test_ari.test
* Update launch files and add meshes
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

0.0.40 (2021-10-05)
-------------------

0.0.39 (2021-08-19)
-------------------

0.0.38 (2021-08-19)
-------------------
* Merge branch 'add-spring-cameras' into 'ferrum-devel'
  Add spring cameras
  See merge request robots/ari_robot!38
* Fix Node name
* Use separated fisheye params
* receive spring cameras param
* Contributors: Sara Cooper, davidfernandez, saikishor

0.0.37 (2021-08-16)
-------------------

0.0.36 (2021-08-05)
-------------------
* Merge branch 'load_motions' into 'ferrum-devel'
  Load motions created in .pal
  See merge request robots/ari_robot!31
* Load motions created in .pal
* Merge branch 'remove_joystick' into 'ferrum-devel'
  Do not autostart joystick
  See merge request robots/ari_robot!36
* Do not autostart joystick
* Contributors: davidfernandez, saikishor

0.0.35 (2021-07-28)
-------------------
* Merge branch 'fixing_laser_model' into 'ferrum-devel'
  fixing laser_model set default false
  See merge request robots/ari_robot!35
* Rename camera param and pass laser
* fixing laser_model set default false
* Contributors: antoniobrandi, davidfernandez, saikishor

0.0.34 (2021-05-20)
-------------------
* Merge branch 'ari_laser_new' into 'ferrum-devel'
  Added laser_model dependencies
  See merge request robots/ari_robot!34
* Remove config
* Update ari_bringup/launch/ari.launch
* Added laser_model dependencies
* Added laser_model dependencies
* Added laser_model dependencies
* Contributors: davidfernandez, sergiomoyano

0.0.33 (2021-04-07)
-------------------
* Merge branch 'head-realsense' into 'ferrum-devel'
  Head realsense optional camera
  See merge request robots/ari_robot!33
* Modify URDF to include optional head realsense camera, location still to be defined
* Contributors: Sara Cooper, davidfernandez

0.0.32 (2021-03-16)
-------------------

0.0.31 (2020-11-09)
-------------------

0.0.30 (2020-10-05)
-------------------
* Merge branch 'show_left_motion' into 'ferrum-devel'
  tune arm_right_2_joint in show_left motion
  See merge request robots/ari_robot!27
* replicate show_left motion values on show_right motion
* tune arm_right_2_joint in show_left motion
* Contributors: YueErro, victor

0.0.29 (2020-09-21)
-------------------

0.0.28 (2020-08-31)
-------------------

0.0.27 (2020-08-17)
-------------------

0.0.26 (2020-08-17)
-------------------

0.0.25 (2020-07-30)
-------------------

0.0.24 (2020-07-16)
-------------------
* Fix load of mobile base controller
* Contributors: Victor Lopez

0.0.23 (2020-07-14)
-------------------
* Update ari rviz config
* Contributors: Victor Lopez

0.0.22 (2020-07-10)
-------------------
* Fix error using multiplier_dir variable
* Contributors: Victor Lopez

0.0.21 (2020-07-10)
-------------------
* Integrate ari_wheel_controller_configuration
* Contributors: Victor Lopez

0.0.20 (2020-06-16)
-------------------
* Remap joystick diagnostics
  We don't want them on main topic since we don't use joystick
* Contributors: Victor Lopez

0.0.19 (2020-06-16)
-------------------
* Do throttle inside qr detector
* Contributors: Victor Lopez

0.0.18 (2020-05-29)
-------------------

0.0.17 (2020-05-19)
-------------------

0.0.16 (2020-03-24)
-------------------
* Merge branch 'actuated_hand_fix' into 'ferrum-devel'
  Actuated hand fix
  See merge request robots/ari_robot!20
* Separate both end effectors
* Add parameter for end_effector
* Contributors: davidfernandez

0.0.15 (2020-03-17)
-------------------
* Merge branch 'cleaned-up-ari-robot' into 'ferrum-devel'
  Clean up ari robot package
  See merge request robots/ari_robot!18
* Clean up ari robot package
* Contributors: alessandrodifava, saracooper

0.0.14 (2020-02-12)
-------------------

0.0.13 (2020-02-04)
-------------------

0.0.12 (2020-01-22)
-------------------

0.0.11 (2020-01-14)
-------------------
* Fix head front camera topic name
* Contributors: Victor Lopez

0.0.10 (2020-01-09)
-------------------

0.0.9 (2020-01-07)
------------------

0.0.8 (2019-12-17)
------------------

0.0.7 (2019-12-10)
------------------
* Merge branch 'qr_detector' into 'master'
  added qr detector application launch
  See merge request robots/ari_robot!7
* added qr detector application launch
* Contributors: Sai Kishor Kothakota, Victor Lopez

0.0.6 (2019-12-10)
------------------

0.0.5 (2019-12-03)
------------------

0.0.4 (2019-11-15)
------------------

0.0.3 (2019-11-14)
------------------
* Merge branch 'ari_moveit' into 'master'
  Ari moveit
  See merge request robots/ari_robot!1
* Add motions
* added play_motion launch and moveit_config dependency
* Contributors: Jordan Palacios, Sai Kishor Kothakota, davidfernandez

0.0.2 (2019-11-08)
------------------
* Remove dynamixel node
* Merge branch 'master' of gitlab:robots/ari_robot
* Contributors: Victor Lopez, alessandrodifava

0.0.1 (2019-11-06)
------------------
* Added also the right arm and tuned the config files for the arms
* Added the head limit and the microphone urdf
* Fixed bugs and added the camera launch in the bringup and the microphone urdf
* Fixed bugs and parameters
* Created the bringup and the controller configuration and added the t265 camera to the back of the torso
* Contributors: alessandrodifava
