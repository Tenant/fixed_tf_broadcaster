#!/usr/bin/env python2

import rospy
from tf.msg import tfMessage
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

def callback(msg):
    global roll, pitch, yaw
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    print "yaw: " + str(yaw)
    print "roll: " + str(roll)
    print "pitch: " + str(pitch)

  
if __name__ == '__main__':
  rospy.init_node('quaternion_subscriber')
  sub = rospy.Subscriber('/laser_odom_to_init',Odometry,callback)
  
  r = rospy.Rate(1)
  while not rospy.is_shutdown():
      r.sleep()
