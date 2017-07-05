#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import rospy

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
