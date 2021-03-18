#! /usr/bin/python3

import rospy, turtlesim
from geometry_msgs.msg import TwistWithCovarianceStamped
from geometry_msgs.msg import Twist
#import turtlesim.srv #Tapa2. Joko koko turtlesim service, tai alempi missä vain Spawn
from turtlesim.srv import Spawn 

def cb(msg):
    twist_to_turtle2 = Twist()
    twist_to_turtle2.linear.x = msg.twist.twist.linear.x
    twist_to_turtle2.angular.z = msg.twist.twist.angular.z
    pub_twist.publish(twist_to_turtle2)

if __name__ == "__main__":
    rospy.wait_for_service("spawn")
    spawner = rospy.ServiceProxy("spawn", Spawn)
    #spawner = rospy.ServiceProxy("spawn", turtlesim.srp.Spawn) #tapa2
    spawner(5.544, 5.544, 0, "turtle2")
    rospy.init_node("turtle2")
    rospy.Subscriber("turtle1/sensor/twist", TwistWithCovarianceStamped, cb)
    pub_twist = rospy.Publisher("turtle2/cmd_vel", Twist, queue_size=1)
    rospy.spin()