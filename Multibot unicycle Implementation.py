#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
# import matplotlib.pyplot as plt 
import math

global x_coordinate_0, y_coordinate_0
global x_coordinate_1, y_coordinate_1

def odometryCb_0(data):
    global x_coordinate_0, y_coordinate_0
    x_coordinate_0=data.pose.pose.position.x 
    y_coordinate_0=data.pose.pose.position.y 

def odometryCb_1(data):
    global x_coordinate_1, y_coordinate_1
    x_coordinate_1=data.pose.pose.position.x 
    y_coordinate_1=data.pose.pose.position.y 

if __name__ == "__main__":
    file=open("/home/yashveer/Documents/pattern_data_multi.txt","w") #change file
    global x_coordinate_0, y_coordinate_0
    global x_coordinate_1, y_coordinate_1
    rospy.init_node('Velocity_Pub', anonymous=True)

    pub_0=rospy.Publisher('tb3_0/cmd_vel',Twist,queue_size=2)
    sub_0=rospy.Subscriber('tb3_0/odom',Odometry,odometryCb_0)
    pub_1=rospy.Publisher('tb3_1/cmd_vel',Twist,queue_size=2)
    sub_1=rospy.Subscriber('tb3_1/odom',Odometry,odometryCb_1)

    velo_msg_0= Twist()
    velo_msg_1= Twist()
    rate=rospy.Rate(40)

    eta_0=  float(input('What is the value of n_0:  '))
    mu_0=float(input('What is the value of u_0:  '))
    eta_1=  float(input('What is the value of n_1:  '))
    mu_1=float(input('What is the value of u_1:  '))    
    velo_msg_0.linear.x =float(input('what is the linear velocity of 0th bot:  '))
    velo_msg_1.linear.x=float(input('What is the linear velocity of 1st bot:    '))
    while not rospy.is_shutdown():
        x_0=x_coordinate_0
        y_0=y_coordinate_0
        x_1=x_coordinate_1
        y_1=y_coordinate_1 
        r= math.pow(x_1-x_0,2)+math.pow(y_1-y_0,2)
        velo_msg_1.angular.z = eta_1 * math.pow(r, mu_1/2)
        velo_msg_0.angular.z = eta_0 * math.pow(r, mu_0/2)
        file.write(str(x_coordinate_0))
        file.write(" " )
        file.write(str(y_coordinate_0))
        file.write(" ")
        file.write(str(x_coordinate_1))
        file.write(" " )
        file.write(str(y_coordinate_1))
        file.write("\n")
        
        pub_0.publish(velo_msg_0)
        pub_1.publish(velo_msg_1)
        rate.sleep()
    file.close()