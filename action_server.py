#! /usr/bin/env python

import rospy

import actionlib

from robot_arm_control_pkg.msg import ServoControlAction, ServoControlGoal, ServoControlResult, ServoControlFeedback

from scripts.servo_controller import ServoController, ServoControllerFinishedMovementException





def do_action(goal):
    channel = goal.channel
    angle = goal.angle

    servoController = ServoController(channel)
    try:
        servoController.move_servo_to_degree(angle)

    except ServoControllerFinishedMovementException as e:

        print("FINISHED MOVEMENT", e)

        result = ServoControlResult()
        result.angle = 69
        server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node("servo_control_server_node")
    server = actionlib.SimpleActionServer("servo_controller_topic", ServoControlAction, do_action, False)
    server.start()
    rospy.spin()