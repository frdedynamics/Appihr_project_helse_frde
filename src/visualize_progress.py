#!/usr/bin/env python3

import rospy, sys
import tf2_ros
from std_msgs.msg import String, Int16, Float32MultiArray
from geometry_msgs.msg import Pose, Quaternion
from Classes.MarkerBasics import MarkerBasics
from visualization_msgs.msg import Marker
from sensor_msgs.msg import JointState
from math import degrees as r2d

class VisualizeMarkers:
    def __init__(self, rate=100):
        rospy.init_node("visualize_angles", anonymous=False)
        self.r = rospy.Rate(rate)
        self.human_joint_angles = JointState()
        self.human_angle_thresholds = JointState()
        self.left_arm_progress_score_marker = MarkerBasics(topic_id="left_shoulder_progress_score_", type="regular_str")
        self.left_progress_str = "***"
        self.left_progress_score = 0
        self.left_arm_progress_bar_marker = MarkerBasics(topic_id="left_shoulder_progress_bar_", type="progress_bar")
        self.ref_link = 'world'
        self.left_arm_th = 1.7 ##TODO: get from rosparam

        self.tfBuffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tfBuffer)

        ## TODO: pull these data from patient yaml as ros_param and parametrize variable names accordingly.
        ## Dummy progress bars for now.
        self.prev_progress_bars = []
        self.first_progress_bar_marker = MarkerBasics(topic_id="first_progress_bar_", type="progress_bar")
        self.prev_progress_bars.append(self.first_progress_bar_marker)
        self.second_progress_bar_marker = MarkerBasics(topic_id="second_progress_bar_", type="progress_bar")
        self.prev_progress_bars.append(self.second_progress_bar_marker)
        self.third_progress_bar_marker = MarkerBasics(topic_id="third_progress_bar_", type="progress_bar")
        self.prev_progress_bars.append(self.third_progress_bar_marker)
        self.forth_progress_bar_marker = MarkerBasics(topic_id="forth_progress_bar_", type="progress_bar")
        self.prev_progress_bars.append(self.forth_progress_bar_marker)
        self.fifth_progress_bar_marker = MarkerBasics(topic_id="fifth_progress_bar_", type="progress_bar")
        self.prev_progress_bars.append(self.fifth_progress_bar_marker)

        self.active_progress_bar = "fifth"
        self.th_height = 0
        


    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, rosnode deleted.')


    def init_subscribers_and_publishers(self):
        self.sub_human_joint_angles = rospy.Subscriber('/human/human_joint_states', JointState, self.human_joint_angles_cb)

        self.left_arm_progress_score_marker.change_position(0.0, 1.0, 2.0)
        self.left_arm_progress_bar_marker.change_position(0.0, 1.0, 1.0)


        for i in range(0,5):
            self.prev_progress_bars[i].change_position(0.0, 1.5+i*0.5, 1.0)
            self.prev_progress_bars[i].change_scale(s_x=0.3, s_y=0.3, s_z=0.15*(5-i))
            if i == 0:
                self.prev_progress_bars[i].change_colour(0.0, 0.0, 255)
                self.th_height = 0.15*(5-i)
                print(self.th_height)
            else:
                self.prev_progress_bars[i].change_colour(192, 192, 192, 0.7)


    def update(self):

        self.left_arm_progress_score_marker.update_str_marker(str(self.left_progress_str))

        height_bar = self.left_progress_score/90
        g_bar = 255*height_bar

        self.left_arm_progress_bar_marker.change_scale(s_z=height_bar)
        if height_bar < self.th_height:
            self.left_arm_progress_bar_marker.change_colour(R=255, G=g_bar, B=0)
        else:
            self.left_arm_progress_bar_marker.change_colour(R=0, G=255, B=0)
        # self.left_arm_progress_bar_marker.change_colour(R=255, G=165, B=0)
        print(height_bar)


        self.left_arm_progress_score_marker.marker_objectlisher.publish(self.left_arm_progress_score_marker.marker_object)
        self.left_arm_progress_bar_marker.marker_objectlisher.publish(self.left_arm_progress_bar_marker.marker_object)

        for i in range(0,5):
            self.prev_progress_bars[i].marker_objectlisher.publish(self.prev_progress_bars[i].marker_object)


    ## CALLBACKS
    def human_joint_angles_cb(self, msg):
        self.human_joint_angles = msg
        self.left_progress_score = round(r2d(-msg.position[4]), 2)
        self.left_progress_str = str(self.left_progress_score)
        


    @staticmethod
    def map_angle(angle):
        min_value = -1
        max_value = 1
        min_output = 0
        max_output = 255

        mapped_value = ((angle - min_value) / (max_value - min_value)) * (max_output - min_output) + min_output
        mapped_value = int(round(mapped_value))
        mapped_value = max(min_output, min(mapped_value, max_output))

        return mapped_value
    

if __name__ == "__main__":
    ros_node = VisualizeMarkers()
    ros_node.init_subscribers_and_publishers()
    # while not ros_node.runflag:
    while not rospy.is_shutdown():
        ros_node.update()
        ros_node.r.sleep()