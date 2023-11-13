# ARI robot

This package contains the description, controllers and bringup for the PAL RObotics ARI robot.

The URDF templates are written using [empy](https://pypi.org/project/empy/) and have the extension `.em`. 

To regenerate a group of files, you must execute `ros2 run ari_bringup regen_em_file.py EM_FILE_NAME` from the directory where the `.em` file is.
