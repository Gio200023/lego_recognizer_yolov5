#!/usr/bin/env python3
import rospy #client library for ROS
from sensor_msgs.msg import Image
from std_msgs.msg import Float32
from cv_bridge import CvBridge
import random as rng
import cv2
import numpy as np
import os
import time
import torch
from detect.msg import cord
from PIL import ImageGrab
from pathlib import Path

path = Path(__file__).parent.absolute()
best=str(path)+'/../usiamo_questi.pt'
model = torch.hub.load(str(path)+'/../yolov5','custom',path=best, source='local')
model.cuda()
#model.cpu() #if without cuda
model.conf = 0.6


pub = rospy.Publisher('/kinects/coordinate',cord, queue_size=100)

def process_image(msg):
    try:
        mess = cord()
        bridge = CvBridge()
        orig = bridge.imgmsg_to_cv2(msg, "bgr8")
        print("avvio riconoscimento\n")
        
        results = model(orig, size=640)
        pandino=results.pandas().xyxy[0].to_dict(orient="records")
        for pand in pandino:
            cs = float(pand['class'])
            x1 = float(pand['xmin'])
            y1 = float(pand['ymin'])
            x2 = float(pand['xmax'])
            y2 = float(pand['ymax'])
            xc = float(((x2-x1)/2)+x1)
            yc = float(((y2-y1)/2)+y1)
            mess.coordinate=[cs,xc,yc]
            print(str(mess.coordinate))
            try:
                print("pubblico\n")
                pub.publish(mess)
            except Exception as err:
                print(err)
        print("finito")

    except Exception as err:
        print(err)
    

def start_node():
    rospy.init_node('detect_topic')
    rospy.loginfo('Aspetto l\'immagine')
    rospy.Subscriber("/camera/color/image_raw", Image, process_image) #si iscrive al topic del kinect
    rospy.spin() #Continua a ciclare, evita la chiusura del nodo
    
if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
