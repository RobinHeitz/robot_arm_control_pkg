#! /usr/bin/env python

import rospy

import actionlib

import Adafruit_PCA9685

class TestServer:

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name)


if __name__ == "__main__":
    rospy.init_node("TestNode")
    server = TestServer(rospy.get_name())
    rospy.spin()