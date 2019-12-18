#!/usr/bin/env python

import rospy
import sys
import tf
import tf2_ros
import geometry_msgs.msg

# setup the transform
rospy.init_node("rpicam_static_tf_pub")
broadcaster = tf2_ros.StaticTransformBroadcaster()
static_transformStamped = geometry_msgs.msg.TransformStamped()
static_transformStamped.header.stamp = rospy.Time.now()
static_transformStamped.header.frame_id = "base_scan"
static_transformStamped.child_frame_id = "raspicam"

# translational components
static_transformStamped.transform.translation.x = 0.075
static_transformStamped.transform.translation.y = 0.0
static_transformStamped.transform.translation.z = -0.06

# angular components
angle_incl = 50 # degrees
angle_incl_rad = (270.0 - angle_incl) / 360.0
quat = tf.transformations.quaternion_from_euler(0.5 * 6.283185, angle_incl_rad * 6.283185, 0.0)
static_transformStamped.transform.rotation.x = quat[0]
static_transformStamped.transform.rotation.y = quat[1]
static_transformStamped.transform.rotation.z = quat[2]
static_transformStamped.transform.rotation.w = quat[3]

# transform only sent once because it is static
broadcaster.sendTransform(static_transformStamped)
# spin until shutdown, so the node stays online
rospy.spin()