#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def move_in_square():
    rospy.init_node('move_turtle')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(1)  # 1 Hz
    vel_msg = Twist()
    side_length = 2
    angular_speed = 0.2
    linear_speed = 0.2

    for _ in range(4):
        # Move forward
        vel_msg.linear.x = linear_speed
        vel_msg.angular.z = 0
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while current_distance < side_length:
            pub.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = linear_speed * (t1 - t0)

        # Stop
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        pub.publish(vel_msg)
        rate.sleep()

        # Rotate
        vel_msg.linear.x = 0
        vel_msg.angular.z = angular_speed
        t0 = rospy.Time.now().to_sec()
        current_angle = 0

        while current_angle < math.pi / 2:
            pub.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (t1 - t0)

        # Stop
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        pub.publish(vel_msg)
        rate.sleep()

    rospy.spin()

if __name__ == '__main__':
    try:
        move_in_square()
    except rospy.ROSInterruptException:
        pass
