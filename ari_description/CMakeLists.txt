cmake_minimum_required(VERSION 2.8.3)
project(ari_description)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir config gazebo meshes robots urdf)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  foreach(version v1 v2)
    foreach(end_effector_left ari-hand False)
      	foreach(end_effector_right ari-hand False)
      		add_rostest(test/test_ari.test ARGS end_effector_right:=${end_effector_right} end_effector_left:=${end_effector_left} version:=${version})
      	endforeach(end_effector_right)		
    endforeach(end_effector_left)
  endforeach(version)
endif()
