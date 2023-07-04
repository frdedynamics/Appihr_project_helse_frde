#!/usr/bin/env python3

import rospy, sys
import tf2_ros
from std_msgs.msg import String, Int16, Float32MultiArray
from geometry_msgs.msg import Pose, Quaternion
from Classes.MarkerBasics import MarkerBasics
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


    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, rosnode deleted.')


    def init_subscribers_and_publishers(self):
        self.sub_human_joint_angles = rospy.Subscriber('/human/human_joint_states', JointState, self.human_joint_angles_cb)

        self.left_arm_progress_score_marker.change_position(0.0, 1.0, 2.0)
        self.left_arm_progress_bar_marker.change_position(0.0, 1.0, 1.0)



    def update(self):

        self.left_arm_progress_score_marker.update_str_marker(str(self.left_progress_str))

        self.left_arm_progress_bar_marker.change_scale(s_z=self.left_progress_score/90)


        self.left_arm_progress_score_marker.marker_objectlisher.publish(self.left_arm_progress_score_marker.marker_object)
        self.left_arm_progress_bar_marker.marker_objectlisher.publish(self.left_arm_progress_bar_marker.marker_object)


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