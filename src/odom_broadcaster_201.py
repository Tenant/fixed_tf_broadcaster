#!/usr/bin/env python2  
import roslib
roslib.load_manifest('fixed_tf_broadcaster')

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('camera_init_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        br.sendTransform((0.0, 0.0, 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "camera_init",
                         "odom")
        rate.sleep()
