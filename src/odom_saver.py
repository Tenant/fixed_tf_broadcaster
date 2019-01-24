#!/usr/bin/env python2

import rospy
from tf.msg import tfMessage
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

def callback(msg):
    global x, y, z
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z

    #print(msg.pose.pose)
    #information = str(msg.header.stamp) +" " + str(x)+" "+str(y) + " " + str(z) + " {:.5f} {:.5f} {:.5f} {:.5f}".format(msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    information = str(msg.header.stamp) + " " + str(x) + " " + str(y) + " " + str(z) + " " + str(roll) + " " + str(pitch) + " " + str(yaw)
    file = open("/home/sukie/Desktop/data/odometry.txt","a")
    file.write(information + '\n')
    file.close()
    print(information)
 

  
if __name__ == '__main__':
  rospy.init_node('odometry_save_subscriber')
  sub = rospy.Subscriber('/laser_odom_to_init',Odometry,callback)
  
  r = rospy.Rate(1)
  while not rospy.is_shutdown():
      r.sleep()
