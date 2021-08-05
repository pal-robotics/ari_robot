cmake_minimum_required(VERSION 2.8.3)
project(ari_bringup)
find_package(catkin REQUIRED)
catkin_package()

foreach(dir config launch bin)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir}
	USE_SOURCE_PERMISSIONS
    )
endforeach(dir)
