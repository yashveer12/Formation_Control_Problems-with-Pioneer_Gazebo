#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
# import matplotlib.pyplot as plt 
import math

global x_coordinate, y_coordinate

def odometryCb(data):
    global x_coordinate, y_coordinate
    x_coordinate=data.pose.pose.position.x 
    y_coordinate=data.pose.pose.position.y 

if __name__ == "__main__":
    # file=open("/home/yashveer/Documents/patterdata.txt","w")   Change file name
    global x_coordinate, y_coordinate
    rospy.init_node('Velocity_Pub', anonymous=True)

    pub=rospy.Publisher('RosAria/cmd_vel',Twist,queue_size=2)
    sub=rospy.Subscriber('RosAria/pose',Odometry,odometryCb )

    velo_msg = Twist()
    rate=rospy.Rate(10)

    eta=  float(input('What is the value of n:  '))
    mu=float(input('What is the value of u:  '))
    x_T=float(input('What is the value of x-coordinate:  '))
    y_T=float(input('What is the value of y-coordinate:  '))
    velo_msg.linear.x =float(input('what is the linear velocity:  '))

    while not rospy.is_shutdown():
        r= math.pow(x_coordinate-x_T,2)+math.pow(y_coordinate-y_T,2)
        velo_msg.angular.z = eta * math.pow(r, mu/2)
        # file.write("x=" )
        file.write(str(x_coordinate))
        file.write(" " )
        file.write(str(y_coordinate))
        file.write("\n")
    ## loop
        if(velo_msg.angular.z>0.5 ):
            print("High Angular Velocity Warning!!!!\nAngular velocity is set to ZERO!!!\n")
            velo_msg.angular.z=0
        
        if(velo_msg.linear.x>=0.2):
            print("High Linear Velocity Warning!!!!\nLinear Velocity is set to 0.05\n")

        if(velo_msg.linear.x<=-0.2):
            print("High Linear Velocity Warning!!!1\nLinear Velocity is set to 0.05\n")
            velo_msg.linear.x=0.05
        pub.publish(velo_msg)
        rate.sleep()
        
    file.close()
    
    
   

