Explanation of circle code: - 

This Python script utilises the ROS (Robot Operating System) framework to control a turtle robot in a simulated environment. Here's an explanation of the code and the keywords used:

1. **Shebang Line (`#!/usr/bin/env python3`):**
   - This line indicates the path to the Python3 interpreter that should be used to run the script.

2. **Import Statements:**
   - `import rospy`: Imports the rospy library, a Python client library for ROS.
   - `from geometry_msgs.msg import Twist`: Imports the Twist message type from the geometry_msgs package. Twist is commonly used to represent linear and angular velocities.
   - `from turtlesim.msg import Pose`: Imports the Pose message type from the turtlesim package. Pose represents the position and orientation of an object in 2D space.
   - `from math import pi`: Imports the mathematical constant pi.

3. **Class Definition (`CircleTurtle`):**
   - Defines a class named `CircleTurtle` to encapsulate the functionality for controlling a turtle in a circular motion.

4. **`__init__` Method:**
   - Initializes the `CircleTurtle` class. It sets up a ROS node, initialises a publisher to control the turtle's velocity, and subscribes to its pose to update its current position.

5. **`update_pose` Method:**
   - Updates the turtle's pose (position and orientation) based on the data received from the `/turtle1/pose` topic.

6. **`move_in_circle` Method:**
   - Contains the logic to make the turtle move in a circle. It continuously publishes Twist messages with a linear velocity on the x-axis and an angular velocity on the z-axis.

7. **`if __name__ == '__main__':` Block:**
   - Checks whether the script is being run as the main program.
   - If it is, it creates an instance of the `CircleTurtle` class and calls the `move_in_circle` method to make the turtle move in a circle.
   - Handles the `rospy.ROSInterruptException` to gracefully exit the script when a ROS interrupt exception occurs.

This script creates a ROS node that controls a turtle in a simulated environment, making it move in a circular path by publishing Twist messages with specific linear and angular velocities.

Final result:
![Circle](https://github.com/DevAnandGupta/Assignment-2/assets/158339161/1b280c90-3c6c-47e6-930d-2accd5845014)



Explanation of square code: -

1. **Shebang Line (`#!/usr/bin/env python3`):**
   - Indicates the path to the Python 3 interpreter that should be used to run the script.

2. **Import Statements:**
   - `import rospy`: Imports the rospy library, a Python client library for ROS.
   - `from geometry_msgs.msg import Twist`: Imports the Twist message type from the geometry_msgs package. Twist is used to control linear and angular velocities.
   - `import math`: Imports the math module for mathematical functions and constants.

3. **Function Definition (`move_in_square`):**
   - Defines a function named `move_in_square` to encapsulate the logic for making the turtle move in a square pattern.

4. **`rospy.init_node('move_turtle')`:**
   - Initializes a ROS node named 'move_turtle' using rospy.

5. **`rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)`:**
   - Creates a publisher for the '/turtle1/cmd_vel' topic, which is responsible for sending velocity commands to the turtle.

6. **`rospy.Rate(1)`:**
   - Creates a rate object set at 1 Hz, controlling the frequency of the loop execution.

7. **Variable Initialization:**
   - `vel_msg`: Initializes a Twist message to control the turtle's velocity.
   - `side_length`: Sets the length of each side of the square.
   - `angular_speed`: Sets the angular speed for rotation.
   - `linear_speed`: Sets the linear speed for forward motion.

8. **Loop to Move in a Square:**
   - A loop iterates four times, representing each side of the square.
   - For each iteration, the turtle moves forward, stops, rotates 90 degrees, and stops again.

9. **Velocity Control Loop:**
   - Uses time-based control to move the turtle forward and rotate. It calculates the distance or angle covered based on the elapsed time and updates the velocities accordingly.

10. **`rate.sleep()`:**
    - Pauses the loop execution to maintain the specified rate.

11. **`rospy.spin()`:**
    - Keeps the program from exiting until the ROS node is shut down.

12. **`if __name__ == '__main__':` Block:**
    - Checks whether the script is being run as the main program.
    - If it is, calls the `move_in_square` function.
    - Handles the `rospy.ROSInterruptException` to gracefully exit the script when a ROS interrupt exception occurs.

This script effectively controls the turtle robot to move in a square pattern by adjusting its linear and angular velocities using the ROS framework.

Final result:
![Square](https://github.com/DevAnandGupta/Assignment-2/assets/158339161/94bac830-ea9d-4aca-82eb-b50f9d5d0af8)
