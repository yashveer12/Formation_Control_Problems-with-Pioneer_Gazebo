#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

def odometryCb(msg):
    print (msg.pose.pose.position.x)

if __name__ == "__main__":
    rospy.init_node('oodometry', anonymous=True) #make node
    
    rospy.Subscriber('odom',Odometry,odometryCb)
    rospy.spin()
