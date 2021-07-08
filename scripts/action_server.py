#! /usr/bin/env python

import rospy

import actionlib

import Adafruit_PCA9685

import robot_arm_control_pkg.msg
# from robot_arm_control_pkg.msg import servoControlAction


class ServoControlAction:

    _feedback = robot_arm_control_pkg.msg.servo_controlFeedback()
    _result = robot_arm_control_pkg.msg.servo_controlResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(
            self._action_name, 
            robot_arm_control_pkg.msg.servo_controlAction, 
            execute=self.execute_cb, 
            auto_start=False,
            )
        self._as.start()

    def execute_cb(self, goal):
        r = rospy.Rate(1)
        success = True

        self._feedback.angel  = 69
 

if __name__ == "__main__":
    rospy.init_node("TestNode")
    server = TestServer(rospy.get_name())
    rospy.spin()