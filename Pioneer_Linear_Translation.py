#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

if __name__ == '__main__' :
    print('Initializing ......')
    rospy.init_node("Velo_pub",anonymous='True')
    pub=rospy.Publisher("/RosAria/cmd_vel",Twist,queue_size=2)
    rate=rospy.Rate(10)
    linear_speed = float(input('What is the linear velocity of bot! = \n'))
    angular_speed = float(input('What is the angular velocity of bot! = \n'))
    seconds= time.time()
    print('Initial time',seconds)
    velo_msg = Twist()
    time_duration_1 = 5
    time_duration_2 = 5
    while not rospy.is_shutdown() :
        cur_time = time.time()
        print('Elapsed time',cur_time-seconds)
        if(linear_speed >=0.2):
            
             velo_msg.linear.x=0
             velo_msg.angular.z=0
          
        if(cur_time<=(seconds+time_duration_1)):
             velo_msg.linear.x=linear_speed
             velo_msg.angular.z=angular_speed
            
        else:
            if(seconds+time_duration_1<cur_time<=seconds+time_duration_1+time_duration_2):
                velo_msg.linear.x=-linear_speed
                velo_msg.angular.z=angular_speed

            velo_msg.linear.x=0
            velo_msg.angular.z=0
        pub.publish(velo_msg)
        rate.sleep()
        