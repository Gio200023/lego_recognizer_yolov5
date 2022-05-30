#!/usr/bin/python3
from gazebo_msgs.srv import SpawnModel
from gazebo_msgs.srv import DeleteModel
from geometry_msgs.msg import *
import rospy
import numpy as np

#Array containing all lego blocks names
blocks = ['X1-Y1-Z2', 'X1-Y2-Z1', 'X1-Y2-Z2', 'X1-Y2-Z2-CHAMFER', 'X1-Y2-Z2-TWINFILLET', 'X1-Y3-Z2', 'X1-Y3-Z2-FILLET', 'X1-Y4-Z1', 'X1-Y4-Z2', 'X2-Y2-Z2', 'X2-Y2-Z2-FILLET']
global brick_number

def remove():
    brick_number
    for i in range(11):
        for m in range(brick_number[i]):
            delete_model_client = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
            delete_model_client(str(blocks[i]))
