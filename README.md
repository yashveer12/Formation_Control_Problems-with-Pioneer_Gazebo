# Formation_Control_Problems-with-Pioneer_Gazebo
This was an Under-Graduate Project(UGP) done under the supervision of Prof. Twinkle Tripathy ,Assistant Professor, Department of Electrical Engineering ,IIT-Kanpur. Here formation control laws were validated using simulation on turtlebot-3 in Gazebo and with simulation on Pioneer-3 in real world.  

## Introduction
The primary objective of this project was to explore and study autonomous swarm behavior using ROS and Gazebo. The project involves both simulation-based experiments and real-time implementations using the Pioneer 3DX mobile robot. The simulations are conducted in Gazebo, a powerful robotics simulator, to test and fine-tune the algorithms governing swarm behavior.

## Dependencies
To successfully run this project, the following dependencies need to be installed:

* Robot Operating System (ROS)
* Gazebo simulator
* Python programming language
* ROS packages for TurtleBot and Pioneer 3DX mobile robot (if applicable)
* Additional Python libraries (as required by specific algorithms)

## Simulations
Learning ROS and Gazebo: Initially, we learnt the basics of ROS and Gazebo. This includes understanding ROS concepts, creating ROS nodes and packages, and launching simulations in Gazebo using the TurtleBot model.

Algorithm Development: Algorithms were implemented in Python to govern the autonomous agents. These algorithms focused on achieving desired patterns such as flocking, formation, and cooperative tasks. The implementation includes handling sensor data, decision-making, and control logic.

Simulation in Gazebo: The developed algorithms are then integrated with Gazebo to simulate the swarm behavior. Multiple instances of the TurtleBot model are used to represent the swarm. The simulations wererun in Gazebo, enabling visualization and analysis using tool like Rviz.

Real-Time Implementations
Pioneer 3DX Mobile Robot: The real-time implementations involved utilizing the Pioneer 3DX mobile robot. The developed algorithms are ported to the Pioneer 3DX platform to achieve similar swarm behavior observed in simulations.

Multiple Robot Formation Patterns: The implementations focused on achieving different multiple robot formation patterns using the Pioneer 3DX robots. These patterns included line formation, circle formation, or custom formations defined by the algorithms.

References

https://www.ros.org/
https://www.turtlebot.com/

