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
_RED_COLOR = ColorRGBA(r=0.0,g=0.0, b=1.0)


def led():
    # Create Publisher to change status led color
    status_led_topic = '/hsrb/command_status_led_rgb'
#    global led_pub
    led_pub = rospy.Publisher(status_led_topic,ColorRGBA, queue_size=100)
    #led_r = _RED_COLOR
    led_pub.publish(_RED_COLOR)

#def find_color(image):
class image_converter:
  def __init__(self):
      self.image_pub = rospy.Publisher("image_topic", Image, queue_size=1)
      #led_pub.publish(_RED_COLOR)
      self.bridge = CvBridge()
     #self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.callback)
      self.image_sub = rospy.Subscriber("/hsrb/head_rgbd_sensor/rgb/image_raw", Image, self.callback)
      self.red_found = False

  def callback(self,data):
      try:
          cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      except CvBridgeError as e:
          print e

      hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
       #閾値の設定
      color_min_1 = np.array([150,70,150])
      color_max_1 = np.array([180,255,255])
      color_min_2 = np.array([0,100,150])
      color_max_2 = np.array([40,255,255])

      color_mask_1 = cv2.inRange(hsv_image, color_min_1, color_max_1);
      color_mask_2 = cv2.inRange(hsv_image, color_min_1, color_max_2);
      color_mask = cv2.bitwise_or(color_mask_1, color_mask_2)
      #cv2.imshow("test",color_mask)
      cv_image2 = cv2.bitwise_and(cv_image, cv_image, mask=color_mask)
      #cv2.imshow("test2",cv_image2)
      #print color_mask
      #np.cpunt_nonzero(color_mask)
      #print np.count_nonzero(color_mask)
      #count_r = []
      count_r = np.count_nonzero(color_mask)
      print count_r
      if count_r > 5000:
         print 'detect_red'
         self.red_found = True
      else:
	       self.red_found = False
      #print len(np.where(color_mask!=255)[0])
      print "\n"

      #type(color_mask)
      #print len(color_mask)=480

      '''
      color = (0,255,0)
      centor = (100,100)
      radius = 20
      cv2.circle(cv_image2, centor, radius, color)
      '''
      cv_half_image = cv2.resize(cv_image,(0,0),fx=0.5,fy=0.5)
      cv_half_image2 = cv2.resize(cv_image2,(0,0),fx=0.5,fy=0.5)
      #print color_mask_1
      #cv2.imshow("test", color_mask_1)
      cv2.imshow("Origin Image", cv_half_image)
      cv2.imshow("Result Image", cv_half_image2)
      cv2.waitKey(2)


def main(args):
    ic = image_converter()
    rospy.init_node('image_converter', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        if ic.red_found:
             led()
        rate.sleep()
    cv2.destroyAllWindows()

if __name__ == '__main__':
   main(sys.argv)
