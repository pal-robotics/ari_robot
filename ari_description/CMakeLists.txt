cmake_minimum_required(VERSION 3.8)
project(ari_description)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()


#############
## Testing ##
#############

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  foreach(robot_model v1 v2)
      foreach(end_effector_left ari-hand no-hand)
          foreach(end_effector_right ari-hand no-hand)
              add_launch_test(
                test/test_description.launch.py
                TARGET "ari_description_${end_effector_right}_${end_effector_left}_${robot_model}"
                ARGS "end_effector_right:=${end_effector_right}" "end_effector_left:=${end_effector_left}" "robot_model:=${robot_model}"
              )
        endforeach()
    endforeach()
  endforeach()
endif()

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config gazebo launch meshes robots ros2_control urdf)
