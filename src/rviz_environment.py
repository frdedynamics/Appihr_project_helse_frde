#! /usr/bin/env python3

import rospy
from visualization_msgs.msg import Marker


rospy.init_node('rviz_marker')

marker_pub = rospy.Publisher("/background_marker", Marker, queue_size = 100)

marker = Marker()

marker.header.frame_id = "world"
marker.header.stamp = rospy.Time.now()

# set shape, Arrow: 0; Cube: 1 ; Sphere: 2 ; Cylinder: 3
marker.type = 10
marker.id = 0
marker.mesh_resource = "package://appirh_project_helse_frde/urdf/meshes/hospital.dae"
marker.mesh_use_embedded_materials = True 

# Set the scale of the marker
marker.scale.x = 1.0
marker.scale.y = 4.0
marker.scale.z = 4.0


# Set the pose of the marker
marker.pose.position.x = -5
marker.pose.position.y = 0
marker.pose.position.z = 2
marker.pose.orientation.x = 0.0
marker.pose.orientation.y = 0.0
marker.pose.orientation.z = 0.0
marker.pose.orientation.w = 0.0

while not rospy.is_shutdown():
  marker_pub.publish(marker)
  rospy.rostime.wallsleep(1.0)