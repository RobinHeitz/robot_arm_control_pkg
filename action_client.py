#! /usr/bin/env python
import rospy
import actionlib
from robot_arm_control_pkg.msg import ServoControlResult, ServoControlFeedback, ServoControlAction, ServoControlGoal

rospy.init_node("servo_control_server_node")
client = actionlib.SimpleActionClient("servo_controller_topic", ServoControlAction)
client.wait_for_server()

goal = ServoControlGoal()
goal.angle=123.456
goal.channel=789

client.send_goal(goal)
client.wait_for_result()

result = client.get_result()
print("RESULT IS:", result)