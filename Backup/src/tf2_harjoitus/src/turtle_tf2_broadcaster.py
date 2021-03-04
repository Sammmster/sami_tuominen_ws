#! /usr/bin/python3

import rospy
import tf_conversions # Muuttaa euler kulmat quarteneiksi
import tf2_ros
from turtlesim.msg import Pose
import geometry_msgs.msg

def handle_turtle_pose(msg, turtlename):
    br = tf2_ros.TransformBroadcaster()
    transform = geometry_msgs.msg.TransformStamped()

    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "world"
    transform.child_frame_id = turtlename
    transform.transform.translation.x = msg.x
    transform.transform.translation.y = msg.y
    transform.transform.translation.z = 0.0
    quaternion = tf_conversions.transformations.quaternion_from_euler(0,0,msg.theta)
    transform.transform.rotation.x =quaternion[0]
    transform.transform.rotation.y =quaternion[1]
    transform.transform.rotation.z =quaternion[2]
    transform.transform.rotation.w =quaternion[3]

    br.sendTransform(transform)

if __name__ == "__main__":
    rospy.init_node("tf2_turtle_broadcaster")
    turtlename = rospy.get_param("~turtle")
    rospy.Subscriber("/%s/pose" % turtlename,
                    Pose,
                    handle_turtle_pose,
                    turtlename)
    rospy.spin()
    # Tuo spin pyörittää ohjelmaa pitkään