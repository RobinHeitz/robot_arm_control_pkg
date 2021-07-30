#! /usr/bin/env python

import rospy

import time

import actionlib

from robot_arm_control_pkg.msg import ServoControlAction, ServoControlGoal, ServoControlResult, ServoControlFeedback

#from scripts.servo_control_pkg.servo_controller import ServoController, ServoControllerFinishedMovementException


def do_action(goal):

    print("do_action_callback")
    channel = goal.channel
    angle = goal.angle
    print('channel: {} angle:{}'.format(channel, angle))

    feedback = ServoControlFeedback()
    feedback.angle = 123
    server.publish_feedback(feedback)
    time.sleep(5)
    result = ServoControlResult()
    result.angle = 456
    server.set_succeeded(result)



    
# def do_action(goal):
#     channel = goal.channel
#     angle = goal.angle

#     print("Start doing goal...")


#     servoController = ServoController(channel)
#     servoController.move_servo_to_degree(angle)
#     time.sleep(5)
#     print("FINISHED MOVEMENT")
#     result = ServoControlResult()
#     result.angle = 69
#     server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node("servo_control_server_node")
    server = actionlib.SimpleActionServer("servo_controller_topic", ServoControlAction, do_action, False)
    server.start()
    print("rospy spin now...")
    rospy.spin()
