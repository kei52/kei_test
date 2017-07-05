#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import print_function

import rospy
import numpy as np
import cv2
import roslib
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridge, CvBridgeError
import controller_manager_msgs.srv
import rospy
import trajectory_msgs.msg
from std_msgs.msg import ColorRGBA

_LED_INPUT_DATA_SIZE = 256
#ColorRGBA(r=0.0,g=0.0,b=0.0)
_RED_COLOR = ColorRGBA(r=1.0,g=0.0, b=0.0)
_GREEN_COLOR = ColorRGBA(r=0.0,g=1.0, b=0.0)
_BLUE_COLOR = ColorRGBA(r=0.0,g=0.0, b=1.0)

def Rled():
    status_led_topic = '/hsrb/command_status_led_rgb'
    led_pub = rospy.Publisher(status_led_topic,ColorRGBA, queue_size=100)
    led_pub.publish(_RED_COLOR)
def Gled():
    status_led_topic = '/hsrb/command_status_led_rgb'
    led_pub = rospy.Publisher(status_led_topic,ColorRGBA, queue_size=100)
    led_pub.publish(_GREEN_COLOR)
def Bled():
    status_led_topic = '/hsrb/command_status_led_rgb'
    led_pub = rospy.Publisher(status_led_topic,ColorRGBA, queue_size=100)
    #led_r = _RED_COLOR
    led_pub.publish(_BLUE_COLOR)

#def find_color(image):
class image_converter:
  def __init__(self):
      self.image_pub = rospy.Publisher("image_topic", Image, queue_size=1)
      self.bridge = CvBridge()
     #self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.callback)
      self.image_sub = rospy.Subscriber("/hsrb/head_rgbd_sensor/rgb/image_raw", Image, self.callback)
      self.red_found = False
      self.green_found = False
      self.blue_found = False

  def callback(self,data):
      try:
          cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      except CvBridgeError as e:
          print e

      hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
       #閾値の設定
      r_min_1 = np.array([150,70,150])
      r_max_1 = np.array([180,255,255])
      r_min_2 = np.array([0,100,150])
      r_max_2 = np.array([10,255,255])

      g_min = np.array([40,70,150])
      g_max = np.array([80,255,255])

      b_min = np.array([100,100,150])
      b_max = np.array([140,255,255])

      #マスクの作成
      r_mask_range1 = cv2.inRange(hsv_image, r_min_1, r_max_1);
      r_mask_range2 = cv2.inRange(hsv_image, r_min_2, r_max_2);
      r_mask = cv2.bitwise_or(r_mask_range1, r_mask_range2)
      r_image = cv2.bitwise_and(cv_image, cv_image, mask=r_mask)

      g_mask_range = cv2.inRange(hsv_image, g_min, g_max);
      g_image = cv2.bitwise_and(cv_image,cv_image,mask=g_mask_range)     

      b_mask_range = cv2.inRange(hsv_image, b_min, b_max);
      b_image = cv2.bitwise_and(cv_image,cv_image,mask=b_mask_range)



      #cv_image2 = cv2.bitwise_and(cv_image, cv_image, mask=r_mask)
      #cv2.imshow("test2",cv_image2)
      #count_r = []
      count_r = np.count_nonzero(r_image)
      count_g = np.count_nonzero(g_image)
      count_b = np.count_nonzero(b_image)


      print count_r
      if count_r > 5000:
         print 'detect_red'
         self.red_found = True
      else:
	       self.red_found = False

      print count_g
      if count_g > 5000:
         print 'detect_green'
         self.green_found = True
      else:
	       self.green_found = False

      print count_b
      if count_b > 5000:
         print 'detect_blue'
         self.blue_found = True
      else:
	       self.blue_found = False

      print "\n"
      '''
      color = (0,255,0)
      centor = (100,100)
      radius = 20
      cv2.circle(cv_image2, centor, radius, color)
      '''
      cv_half_image = cv2.resize(cv_image,(0,0),fx=0.5,fy=0.5)
      r_half_image = cv2.resize(r_image,(0,0),fx=0.5,fy=0.5)
      g_half_image = cv2.resize(g_image,(0,0),fx=0.5,fy=0.5)
      b_half_image = cv2.resize(b_image,(0,0),fx=0.5,fy=0.5)
      #print color_mask_1
      #cv2.imshow("test", color_mask_1)
      cv2.imshow("Red Image", r_half_image)
      cv2.imshow("Green Image", g_half_image)
      cv2.imshow("Blue Image", b_half_image)
      cv2.imshow("Result Image", cv_half_image)
      cv2.waitKey(1)


def main(args):
    ic = image_converter()
    #anonymousは匿名か匿名じゃないか
    rospy.init_node('image_converter', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        if ic.red_found:
             Rled()
        if ic.green_found:
             Gled()
        if ic.blue_found:
             Bled()
    cv2.destroyAllWindows()

if __name__ == '__main__':
   main(sys.argv)
