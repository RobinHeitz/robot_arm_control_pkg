#! /usr/bin/env python
import rospy
import actionlib
from robot_arm_control_pkg.msg import ServoControlResult, ServoControlFeedback, ServoControlAction, ServoControlGoal


def feedback_cb(feedback):
    print('We got into feedback cb')
    print(feedback)




rospy.init_node("servo_control_client_node")
client = actionlib.SimpleActionClient("servo_controller_topic", ServoControlAction)
client.wait_for_server()

goal = ServoControlGoal()
goal.angle=123.456
goal.channel=789

client.send_goal(goal, feedback_cb=feedback_cb)
print("GOAL WAS SENT FROM CLIENT")
client.wait_for_result()

result = client.get_result()
print("RESULT IS:", result)