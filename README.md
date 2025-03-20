 

 

# ARI Robot

**ARI Robot** is a ROS-based software framework developed by PAL Robotics for operating and simulating the ARI social robot. The repository is organized into multiple ROS packages that together provide:
  
- **Robot Bringup:** Initialization of hardware interfaces and sensor drivers.  
- **Controller Configuration:** Setup of controllers (joint, current limit, state, etc.) to enable safe and coordinated motion.  
- **Robot Description:** Mechanical, kinematic, and visual description (URDF, meshes, collision data) for simulation and visualization.  
- **Core Integration:** High-level integration for managing the system.

> **Note:** This repository is maintained on the `melodic-devel` branch and is targeted for ROS Melodic.

---

## Table of Contents

- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Development and Contributing](#development-and-contributing)
- [Changelog](#changelog)


---

## Repository Structure

- **ari_bringup**  
  Contains the launch files and configuration for starting the ARI robot system. Key launch files include:  
  - `ari.launch` – A high-level launch file (commonly used for simulation or complete system startup).  
  - `ari_bringup.launch` – Specifically used for bringing up the robot hardware and interfaces.  
  - Additional launch files such as `joystick_teleop.launch`, `play_motion.launch`, `qr_detector.launch`, `torso_back_camera.launch`, `torso_front_camera.launch`, and `twist_mux.launch`.

- **ari_controller_configuration**  
  Provides the configuration for the robot’s controllers. The launch directory contains:  
  - `ari_controllers.launch` – Launches the overall controller configuration.  
  - `current_limit_controllers.launch` – Configures current limit controllers.  
  - `default_controllers.launch` – Loads the default set of controllers.  
  - `joint_state_controller.launch` – Starts the joint state publisher for sensor data.

- **ari_description**  
  Contains the URDF, meshes, collision models, and simulation files that define ARI’s physical properties.

- **ari_robot**  
  The core package tying together the bringup, controller configuration, and description components. It contains build configuration files (`CMakeLists.txt`, `package.xml`) and a changelog.

---

## Prerequisites

Before building and running the ARI Robot packages, ensure you have:

- **Ubuntu 16.04 (Xenial)** or a compatible version, as ROS Melodic is supported on this platform.  
- **ROS Melodic:** Installed from the official ROS repositories.  
- **Catkin Tools:** For building the workspace (e.g., `catkin_make` or `catkin build`).  
- All additional ROS dependencies listed in the `package.xml` files of each package.

---

## Installation

1. **Clone the Repository:**

   ```bash
   cd ~/catkin_ws/src
   git clone -b melodic-devel https://github.com/pal-robotics/ari_robot.git
   ```

2. **Install Dependencies:**

   Use `rosdep` to install required dependencies:

   ```bash
   cd ~/catkin_ws
   rosdep install --from-paths src --ignore-src -r -y
   ```

3. **Build the Workspace:**

   ```bash
   cd ~/catkin_ws
   catkin_make
   # or, if you prefer catkin tools:
   # catkin build
   ```

4. **Source the Workspace:**

   ```bash
   source ~/catkin_ws/devel/setup.bash
   ```

---

## Usage

### Launching the Robot Bringup

To initialize the robot’s hardware interfaces (sensors, drivers, and low-level nodes), run the bringup launch file from the `ari_bringup` package:

```bash
roslaunch ari_bringup ari_bringup.launch
```

This file starts all essential nodes for interfacing with ARI’s hardware.

### Launching the Controller Configuration

To configure and start the controllers (for joint motion, safety limits, etc.), use the launch file from the `ari_controller_configuration` package:

```bash
roslaunch ari_controller_configuration ari_controllers.launch
```

Other controller-related launch files (like `default_controllers.launch` or `joint_state_controller.launch`) can be used as needed for additional configuration.

### Launching the Simulation

For simulation purposes (e.g., running the robot in Gazebo or RViz), you can launch the complete system using the high-level launch file from the `ari_bringup` package:

```bash
roslaunch ari_bringup ari.launch
```

This launch file is designed to work with simulation environments by setting appropriate parameters for visualizing ARI in Gazebo and RViz.

*Tip:* Additional launch files such as `play_motion.launch` (for motion playback) or `joystick_teleop.launch` (for teleoperation) are also available and can be run independently as required.

---

## Development and Contributing

Contributions to enhance functionality, documentation, and performance are welcome. Please adhere to the following guidelines:

- **Coding Standards:** Follow standard ROS, C++, and Python conventions.  
- **Commit Messages:** Write clear, concise commit messages that describe your changes.  
- **Issue Reporting:** Report bugs or request features via GitHub Issues.  
- **Pull Requests:** Ensure your pull requests are well-documented and pass all CI tests.  
- **Documentation:** Update this README and in-code documentation as needed.

For further details, consider adding a `CONTRIBUTING.md` file to guide new contributors.

---

## Changelog

Each package maintains its own changelog (e.g., `CHANGELOG.rst`). Please refer to these files for a detailed history of changes and updates.

---

