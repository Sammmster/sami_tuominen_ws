#! /usr/bin/python3

import rospy
# Rospy is a pure Python client library for ROS. The rospy client API enables Python
# programmers to quickly interface with ROS Topics, Services and Parameters.
from geometry_msgs.msg import Twist
# Geometry_msgs provides messages for common geometric primitives such as points, vectors
# and poses.
# Huom, on todella monia viesti tyyppejä tuon lisäksi.
# Tässä on käytetty geometry_msgs alaisuudesta Twist tyyppiä.
# Twist: This expresses velocity in free space into its linear and angular parts:
# Vector3   linear
# Vector3   angular
from turtlesim.msg import Pose
import random

def callback(data):
    vel_msg = Twist()
    pose = data
    if pose.x > 10: #10
        #vel_msg.angular.z = random.randint(-50,50)
        vel_msg.angular.z = 10 #0
        vel_msg.linear.x = -30 #-2
        print("oikea seinä")
    elif pose.x < 1: #1
        vel_msg.angular.z = 0 #0
        vel_msg.linear.x = -2 #-2
        print("vasen seinä")
    elif pose.y > 10: #10
        vel_msg.angular.z = 0 #0
        vel_msg.linear.x = -2 #-2
        print("katto")
    elif pose.y < 1: #1
        vel_msg.angular.z = 0 #0
        vel_msg.linear.x = -2 #-2
        print("lattia")
    else:
        #vel_msg.angular.z = 0
        vel_msg.angular.z = random.randint(-2,2) #-2,2
        # randint tarvitsee 2 parametriä, molemmat end points
        vel_msg.linear.x = random.randint(0,4) #0,2
        #vel_msg.linear.x = 2
        
        # orggis rivit #
        # vel_msg.angular.z = random.randint (-2,2)
        # vel_msg.linear.x = random.randint (0,2)
        # orggis rivit #
    
    velocity_publisher.publish(vel_msg)


rospy.init_node("turtlebot_auto", anonymous=True)
# ylempänä tehdään uusi node nimeltään turtlebot_auto
velocity_publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=1)
# Tehdään julkaisija. ylempänä missä halutaan julkaista viestejä. Twist julkaisee
pose_subscriber = rospy.Subscriber("turtle1/pose", Pose, callback)
# Tehdään kuuntelija. Ylempi kuuntelee viestejä. Pose kuuntelee, callback on funktion nimi.
# Tämän jälkeen määrittele def callback(data): ylemmäs

while not rospy.is_shutdown():
    rospy.spin()
