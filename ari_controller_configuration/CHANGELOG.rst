^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ari_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.59 (2023-06-21)
-------------------

0.0.58 (2023-05-24)
-------------------

0.0.57 (2023-05-22)
-------------------

0.0.56 (2023-05-02)
-------------------

0.0.55 (2023-04-24)
-------------------

0.0.54 (2023-04-18)
-------------------

0.0.53 (2023-04-18)
-------------------

0.0.52 (2023-01-23)
-------------------

0.0.51 (2022-12-15)
-------------------

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

0.0.47 (2022-06-27)
-------------------

0.0.46 (2022-06-09)
-------------------
* Merge branch 'ari-v2' into 'ferrum-devel'
  Ari v2
  See merge request robots/ari_robot!46
* Fix ari base simulation wheels/caster
* Contributors: Luca Marchionni, davidfernandez

0.0.45 (2022-06-08)
-------------------

0.0.44 (2022-06-07)
-------------------

0.0.43 (2022-05-30)
-------------------
* Merge branch 'ari-v2' into 'ferrum-devel'
  Ari v2
  See merge request robots/ari_robot!42
* update motions for new joint limits of ari-v2
* Update launch files and add meshes
* Contributors: David ter Kuile, davidfernandez

0.0.42 (2021-11-02)
-------------------

0.0.41 (2021-10-05)
-------------------

0.0.40 (2021-10-05)
-------------------

0.0.39 (2021-08-19)
-------------------

0.0.38 (2021-08-19)
-------------------

0.0.37 (2021-08-16)
-------------------

0.0.36 (2021-08-05)
-------------------

0.0.35 (2021-07-28)
-------------------
* Merge branch 'fixing_laser_model' into 'ferrum-devel'
  fixing laser_model set default false
  See merge request robots/ari_robot!35
* Rename camera param and pass laser
* Contributors: davidfernandez, saikishor

0.0.34 (2021-05-20)
-------------------
* Added laser_model dependencies
* Contributors: sergiomoyano

0.0.33 (2021-04-07)
-------------------

0.0.32 (2021-03-16)
-------------------

0.0.31 (2020-11-09)
-------------------

0.0.30 (2020-10-05)
-------------------

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

0.0.17 (2020-05-19)
-------------------

0.0.16 (2020-03-24)
-------------------
* Merge branch 'actuated_hand_fix' into 'ferrum-devel'
  Actuated hand fix
  See merge request robots/ari_robot!20
* Separate both end effectors
* Add parameter for end_effector
* add hand joints and transmission for underactuation
* Contributors: Luca Marchionni, davidfernandez

0.0.15 (2020-03-17)
-------------------
* added missing deps play_motion and actionlib
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
* Merge branch 'actuated_hand' into 'master'
  Actuated hand
  See merge request robots/ari_robot!11
* add hand joints and transmission for underactuation
* Contributors: Luca Marchionni, Procópio Stein

0.0.13 (2020-02-04)
-------------------

0.0.12 (2020-01-22)
-------------------

0.0.11 (2020-01-14)
-------------------

0.0.10 (2020-01-09)
-------------------

0.0.9 (2020-01-07)
------------------

0.0.8 (2019-12-17)
------------------

0.0.7 (2019-12-10)
------------------

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
* added play_motion launch and moveit_config dependency
* Contributors: Jordan Palacios, Sai Kishor Kothakota

0.0.2 (2019-11-08)
------------------
* Merge branch 'master' of gitlab:robots/ari_robot
* Contributors: alessandrodifava

0.0.1 (2019-11-06)
------------------
* Added also the right arm and tuned the config files for the arms
* Fixed bugs and added the camera launch in the bringup and the microphone urdf
* Added the caster wheels, modified the urdf files, fixed the problem with the head_1_joint, added the head_camera
* Fixed bugs and parameters
* Created the bringup and the controller configuration and added the t265 camera to the back of the torso
* Contributors: alessandrodifava
