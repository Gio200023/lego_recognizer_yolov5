# Lego Recognizer For Robotics Purpose

## Prerequisites: Ubuntu 20.04, ROS Noetic, Gazebo_ros, catkin_tools, PyTorch, yolov5 and dependencies.

Lego_recognizer is a project I made for Fundamentals of Robotics course. This is the vision component of the project [Fundamental Of Robotics]().
The purpose of this repo is to recognize which of the several different Lego Blocks is seen by the [Kinect Camera](https://github.com/Gio200023/lego_recognizer_yolov5/tree/main/Kinect_ros) in a Gazebo_ros simulation environment.

<hr>

## How it works
[YoloV5](https://github.com/ultralytics/yolov5) based its functionality on object detection algorithms that divides images into a grid system. Each cell in the grid is responsible for detecting objects within itself.

<hr>

## Environment Setup

Follow this [guide]() to setup the Gazebo_ros world and ros itself. 

Clone this repository:
````
git clone https://github.com/Gio200023/lego_recognizer_yolov5
````

After that you can now setup the catkin project.
````
cd lego_recognizer_yolov5
chmod u+x src/detect/nodes/detect_topic_counting.py
catkin build
source devel/setup.bash #or setup.zsh based on your shell
````
> (April 9 22): you need to change weights and yolov5 directory PATH inside detect_topic_counting.py script

## Start to recognize
Now you can launch this package and see the results:
````
rosrun detect detect_topic_counting.py
````

# Documentation
[yolov5](https://docs.ultralytics.com)

[Ros Noetic Installation Guide](https://wiki.ros.org/noetic/Installation/Ubuntu)

[PyTorch Installation](https://pytorch.org/get-started/locally/)
