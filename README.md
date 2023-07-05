# Appirh_project_helse_frde
APPIRH is a project in collaboration with Helse Førde.


## Prerequisite
Awindamonitor ROS package: https://github.com/fjnn/xsense-awinda
PyQT5: `pip install PyQt5`
(For developers only: https://build-system.fman.io/qt-designer-download)


## How to run
1. Start ROS: `roscore`
2. Start reading data from IMUs: `rosrun awindamonitor awindamonitor`
3. IMU data to human joint data: `roslaunch appirh_project_helse_frde human.launch`


## Current test procedure:
1. Start ROS: `roscore`
2. Go to package directory: `roscd appirh_project_helse_frde/src`
3. Run the gui: `./main.py`
4. Record Data > Add to existing patient > Select "gizem" > Next (Progress) > Load Older Data > Select one random data in the dropdown menu > Assign values for this session > Start Sensor Module
5. To start progress bars: `rosrun appirh_project_helse_frde visualize_progress.py`
6. To start background: `rosrun appirh_project_helse_frde rviz_environment.py `


This procedure will start simulation from a recorded bag. To measure real-time you need to change `def start_awindamonitor(self)` in the **main.py**.

- Comment out `self.proc_bag = subprocess.Popen(["rosbag", "play", "-l", "bag/human_measure_long_wait.bag"])
        self.start_human_launch()`
- Comment in `self.add_rosnode("awindamonitor", "awindamonitor", "awindamonitor")`. But you need to be quick in clicking the "Start Measurement" button :D
