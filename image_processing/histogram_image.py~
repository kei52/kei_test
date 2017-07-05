#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import rospy
import cv2


def resize():
    img = cv2.imread('/home/roboworks/image_processing/img/elmo.jpg',cv2.IMREAD_COLOR)
    orgHeight, orgWidth = img.shape[:2]
    size = (orgHeight/2, orgWidth/2)
    
    #Create Half Size Image
    #halfImg = cv2.resize(img, (orgHeight / 2, orgWidth / 2))
    halfImg = cv2.resize(img, size)

    #Create 2 times big Image
    twiceImg = cv2.resize(img, None, fx = 2, fy = 2)
    cv2.imwrite('/home/roboworks/image_processing/img/half.jpg', halfImg)
    cv2.imwrite('/home/roboworks/image_processing/img/twiceImg.jpg', twiceImg)



def hst():
    im = Image.open('/home/roboworks/image_processing/img/twiceImg.jpg')
    #flattenとはバラバラのリストを一つのリストにすること
    r = np.array(im)[:,:,0].flatten()
    g = np.array(im)[:,:,1].flatten()
    b = np.array(im)[:,:,2].flatten()
    bins_range = range(0, 257, 8)
    xtics_range = range(0, 257, 32)

    plt.xlabel("Concentration value")
    plt.ylabel("Number of pixels")
    plt.hist((r,g,b),bins=bins_range,color=['r','g','b'], label=['Red','',''])
    plt.legend(loc=2)
    plt.grid(True)
    #axes([左, 下, 幅, 高さ])
    [xmin,xmax,ymin,ymax]=plt.axis()
    plt.axis([0,256,0,ymax])
    plt.xticks(xtics_range)
    plt.show()


    plt.savefig("img/matplotlib/histogram1.png")

resize()
hst()
'''
mu, sigma = 100, 15
print "mu:{0},sigma{1}".format(mu,sigma)

x = mu + sigma * np.random.randn(10000)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

#binsの設定
bins=50
ax.hist(x, bins, normed=True)
print "bins{0}".format(bins)
ax.set_title('third histogram $\mu=100,\ \sigma=15$')
ax.set_xlabel('x')
ax.set_ylabel('freq')
fig.show()
rospy.sleep(20)
'''
