cmake_minimum_required(VERSION 3.0.2)
project(robot_arm_control_pkg)

find_package(catkin REQUIRED
    actionlib_msgs
)

# add_action_files(
#     DIRECTORY action 
#     FILES ServoControl.action
     
#     )
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )


# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
add_action_files(
    DIRECTORY action
    FILES ServoControl.action
    )
    
## Generate added messages and services with any dependencies listed here
generate_messages(
    DEPENDENCIES
    actionlib_msgs
    std_msgs 
    )
        
catkin_package(
    CATKIN_DEPENDS 
    actionlib_msgs
)

