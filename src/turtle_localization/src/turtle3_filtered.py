#! /usr/bin/python3
import rospy, turtlesim
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
#import turtlesim.srv #Tapa2. Joko koko turtlesim service, tai alempi missä vain Spawn
from turtlesim.srv import Spawn 

def cb(msg):
    twist_to_turtle3 = Twist()
    twist_to_turtle3.linear.x = msg.twist.twist.linear.x
    twist_to_turtle3.angular.z = msg.twist.twist.angular.z
    pub_twist.publish(twist_to_turtle3)

if __name__ == "__main__":
    rospy.wait_for_service("spawn")
    spawner = rospy.ServiceProxy("spawn", Spawn)
    #spawner = rospy.ServiceProxy("spawn", turtlesim.srp.Spawn) #tapa2
    spawner(5.544, 5.544, 0, "turtle3")
    rospy.init_node("turtle3")
    rospy.Subscriber("odometry/filtered_twist", Odometry, cb)
    pub_twist = rospy.Publisher("turtle3/cmd_vel", Twist, queue_size=1)
    rospy.spin()