#!/usr/bin/env python3

"""
Gui's ROS related things got over this class. TEST for now

"""

import rospy
from std_msgs.msg import String, Int16

import datetime

class GUInode:
    def __init__(self, rate=30):
        """Initializes the GUI node.
        @param rate: ROS node spin rate"""
        rospy.init_node("hrc_gui_training", anonymous=False)
        self.r = rospy.Rate(rate)

        self.now = String()
        self.now.data = str(datetime.datetime.now())
        self.test_pub_data = Int16()
        self.test_pub_data.data = 5
        self.test_sub_data = Int16()

        rospy.set_param('/ros_node_started', False)
        print("ros_node_param", rospy.get_param('/ros_node_started'))

    
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, rosnode deleted.')


    def init_subscribers_and_publishers(self):
        self.test_pub = rospy.Publisher('/test_pub_data', Int16, queue_size=1)
        self.test_sub = rospy.Subscriber('/test_sub_data', Int16, self.test_sub_cb)

    def set_params(self):
        pass

    def update(self):
        for i in range(100):
            self.test_pub_data = i
            self.test_pub.publish(self.test_pub_data)
            self.r.sleep()

    ## CALLBACKS
    def test_sub_cb(self, msg):
        self.test_sub_data = msg