#! /usr/bin/env python

import rospy

import time

import actionlib

from robot_arm_control_pkg.msg import ServoControlAction, ServoControlGoal, ServoControlResult, ServoControlFeedback

from scripts.servo_control_pkg.servo_controller import ServoController, ServoControllerFinishedMovementException





def move_servo(goal):
    channel = goal.channel
    angle = goal.angle

    print("Start doing goal...")

    servoController = ServoController()

    try:
        servoController.move_servo_to_degree(angle, channel)
    
    except ServoControllerFinishedMovementException as e:
        print(e)
        print("FINISHED MOVEMENT" )
        result = ServoControlResult()
        result.angle = 69
        server.set_succeeded(result)
        return

    
    

    
    time.sleep(15)
    print("Cancel goal")
    server.cancel_all_goals()


if __name__ == "__main__":
    rospy.init_node("servo_control_server_node")
    server = actionlib.SimpleActionServer("servo_controller_topic", ServoControlAction, move_servo, False)
    server.start()
    print("rospy spin now...")
    rospy.spin()