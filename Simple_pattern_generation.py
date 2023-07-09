#!/usr/bin/env python

# For alphabet=0 the bot will trace S character and for alphabet=1 the bot will trace 8 character

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import time

file=open("/home/odroid/catkin_ws/src/my_pkg/src/pattern_data_8.txt","w") #change file

def odometryCb(msg):    
    file.write(str(msg.pose.pose.position.x))
    file.write(" " )
    file.write(str(msg.pose.pose.position.y))
    file.write("\n")

if __name__ == '__main__':
    
    rospy.init_node('Velocity_publisher', anonymous=True)
    # changes in /cmd_vel
    pub = rospy.Publisher('RosAria/cmd_vel', Twist, queue_size=2)

    rate = rospy.Rate(50)
    alphabet = float(input('What alphabet do you want?'))

    velo_msg = Twist()
    start_time=time.time()
    i=0
    while not rospy.is_shutdown():
        cur_time=time.time()
        if(alphabet==2):
            if(cur_time<start_time+10):
                velo_msg.linear.x=0.1
                velo_msg.angular.z=0.314
            if(start_time+10<cur_time<start_time+20):
                velo_msg.linear.x=0.1                 
                velo_msg.angular.z=-0.314
            if(cur_time>start_time+20):
                if(cur_time>start_time+20+i):
                    print("I am at rest!!!")
                    i+=2
                velo_msg.linear.x=0
                velo_msg.angular.z=0
        
        if(alphabet==8):
            if(cur_time<start_time+30):
                velo_msg.linear.x=0.1
                velo_msg.angular.z=0.314
            if(start_time+30<cur_time<start_time+50):
                velo_msg.linear.x=0.1
                velo_msg.angular.z=-0.314
            if(cur_time>start_time+50):
                if(cur_time>start_time+50+i):
                    print("I am at rest!!!")
                    i+=2
                velo_msg.linear.x=0
                velo_msg.angular.z=0


        pub.publish(velo_msg)
        #changes in odom 
        rospy.Subscriber('RosAria/pose',Odometry,odometryCb)
        rate.sleep()