import rospy

from rosutils.node import Node, SerialNode

def now():
    return rospy.Time.now()