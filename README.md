# walker_rosys
This package contains the URDF file of a diff drive walker and launch files to launch it in gazebo and rviz.

## Usage
1. Create the ROS2 workspace:
   ```bash
   mkdir  easywalk_ws/src -p  
   cd easywalk_ws  
   colcon build --symlink-install  
   source install/local_setup.bash
   ```

2. Clone this repository to your ROS2 workspace:
   ```bash
   cd src \
   git clone https://github.com/walker_rosys.git
   ```

3. Build the ROS2 package:
   ```bash
   cd  easywalk_ws  
   colcon build --symlink-install  
   source install/local_setup.bash
   ```

4.    Launch the robot in RVIZ2
   ```bash
   ros2 launch walker_rosys display.launch.py
   ```

5. Launch the robot in Gazebo
   ```bash
   ros2 launch walker_rosys gazebo.launch.py
   ```

6. Open another terminal and use
   ```bash
   ros2 run teleop_twist_keyboard teleop_twist_keyboard
   ```
   Move your robot around

## License
This project is licensed under the RoSys Group License.
