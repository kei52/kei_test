#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import matplotlib.pyplot as plt
from numpy.random import *

x = tf.placeholder(tf.float32, shape=[None,1])
y = tf.placeholder(tf.float32, shape=[None,1])
a = tf.Variable(tf.random_normal(shape=[]))
b = tf.Variable(tf.random_normal(shape=[]))
n = tf.cast(tf.shape(x)[0], tf.float32)
xx = tf.matmul(tf.transpose(x),x)
yy = tf.matmul(tf.transpose(y),y)
xy = tf.matmul(tf.transpose(x),y)
sx = tf.reduce_sum(x,0)
sy = tf.reduce_sum(y,0)
E = ((a*a*xx)+(n*b*b)+yy+(2*a*b*sx)+(-2*a*xy)+(-2*b*sy))/n
opt = tf.train.GradientDescentOptimizer(0.1)
step = opt.minimize(E)
session = tf.InteractiveSession()
session.run(tf.initialize_all_variables())
an = 2
bn = 5
xn = randn(10,1)
feed_dict = {x:xn,y:an*xn+bn+rand(10,1)}
for i in range(200):
	print session.run(step, feed_dict)
	print session.run(E, feed_dict)
	a_,b_ = session.run([a,b], feed_dict)
	print [a_,b_]
	plt.clf()
	plt.scatter(feed_dict[x],feed_dict[y])
	plt.hold('on')
	plt.plot([-3,3],[[a_*(-3)+b_,an*(-3)+bn],[a_*3+b_,an*3+bn]])
	plt.pause(0.001)

plt.savefig('Gradient')

