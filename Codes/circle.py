#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pi

class CircleTurtle:
    def __init__(self):
        rospy.init_node('circle_turtle', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()

    def update_pose(self, data):
        self.pose = data

    def move_in_circle(self):
        rate = rospy.Rate(10)
        twist = Twist()

        while not rospy.is_shutdown():
            # Move in a circle with constant twist velocity
            twist.linear.x = 5.0  # Linear velocity in the x-axis
            twist.angular.z = 2.0  # Angular velocity in the z-axis

            self.velocity_publisher.publish(twist)
            rate.sleep()

if __name__ == '__main__':
    try:
        circle_turtle = CircleTurtle()
        circle_turtle.move_in_circle()
    except rospy.ROSInterruptException:
        pass
