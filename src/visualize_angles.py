#!/usr/bin/env python3

import rospy, sys
import tf2_ros
from std_msgs.msg import String, Int16, Float32MultiArray
from geometry_msgs.msg import Pose, Quaternion
from Classes.MarkerBasics import MarkerBasics
from sensor_msgs.msg import JointState

class VisualizeMarkers:
    def __init__(self, rate=100):
        rospy.init_node("visualize_angles", anonymous=False)
        self.r = rospy.Rate(rate)
        self.human_joint_angles = JointState()
        self.human_angle_thresholds = JointState()
        self.left_arm_marker = MarkerBasics(topic_id="left_shoulder_virt_link_", type="arm")
        self.right_arm_marker = MarkerBasics(topic_id="right_shoulder_virt_link_", type="arm")
        self.ref_link = 'human_base_link'
        self.left_arm_th = 1.7 ##TODO: get from rosparam

        self.tfBuffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tfBuffer)


    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, rosnode deleted.')


    def init_subscribers_and_publishers(self):
        self.sub_human_joint_angles = rospy.Subscriber('/human/human_joint_states', JointState, self.human_joint_angles_cb)



    def update(self):
        try:
            left_shoulder_trans = self.tfBuffer.lookup_transform(self.ref_link, 'left_shoulder_virt_link_1', rospy.Time())
            right_shoulder_trans = self.tfBuffer.lookup_transform(self.ref_link, 'right_shoulder_virt_link_1', rospy.Time())

            self.left_arm_marker.marker_object.pose.position = left_shoulder_trans.transform.translation
            self.left_arm_marker.marker_object.pose.orientation = left_shoulder_trans.transform.rotation

            self.right_arm_marker.marker_object.pose.position = right_shoulder_trans.transform.translation
            self.right_arm_marker.marker_object.pose.orientation = right_shoulder_trans.transform.rotation

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            pass

        try:
            print("left")
            self.left_arm_marker.change_colour(R=VisualizeMarkers.map_angle(self.human_joint_angles.position[3]), 
                                            G=VisualizeMarkers.map_angle(self.human_joint_angles.position[4]), 
                                            B=VisualizeMarkers.map_angle(self.human_joint_angles.position[5]))
            self.right_arm_marker.change_colour(R=VisualizeMarkers.map_angle(self.human_joint_angles.position[6]), 
                                                G=VisualizeMarkers.map_angle(self.human_joint_angles.position[7]), 
                                                B=VisualizeMarkers.map_angle(self.human_joint_angles.position[8]))
            
            # self.left_arm_marker.set_visible()
            # self.right_arm_marker.set_visible()

        except IndexError as e:
            print(e)


        self.left_arm_marker.marker_objectlisher.publish(self.left_arm_marker.marker_object)
        self.right_arm_marker.marker_objectlisher.publish(self.right_arm_marker.marker_object)


    ## CALLBACKS
    def human_joint_angles_cb(self, msg):
        self.human_joint_angles = msg


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