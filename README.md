# Appirh_project_helse_frde
APPIRH is a project in collaboration with Helse Førde.


## Prerequisite
Awindamonitor ROS package: https://github.com/fjnn/xsense-awinda

## How to run
1. Start ROS: `roscore`
2. Start reading data from IMUs: `rosrun awindamonitor awindamonitor`
3. IMU data to human joint data: `roslaunch appirh_project_helse_frde human.launch`
