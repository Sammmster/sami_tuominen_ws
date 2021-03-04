#! /usr/bin/python3

import rospy
import math
import tf2_ros
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

if __name__== "__main__":
    rospy.init_node("tf2_turtle_listener")
    tf_buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tf_buffer)

    rospy.wait_for_service("spawn")
    spawner = rospy.ServiceProxy("spawn", Spawn)
    turtle_name = rospy.get_param("turtle", "turtle2")
    #turtle_name = rospy.get_param("turtle", "turtle2", "turtle3")
    spawner(4,2,0,turtle_name)
    

    turtle_vel = rospy.Publisher("%s/cmd_vel" % turtle_name, Twist, queue_size=1)
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            trans = tf_buffer.lookup_transform(turtle_name, "turtle1", rospy.Time())
        except(tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()            
            continue
        msg = Twist()
        msg.angular.z = 4 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)
        msg.linear.x = 0.5 * math.sqrt(trans.transform.translation.x**2 + trans.transform.translation.y**2)
        turtle_vel.publish(msg)
        rate.sleep()
