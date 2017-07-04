#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import matplotlib.pyplot as plt

x = tf.placeholder(tf.float32, shape=[None,1])
y = tf.placeholder(tf.float32, shape=[None,1])
a = tf.Variable(tf.random_normal(shape=[]))
b = tf.Variable(tf.random_normal(shape=[]))
n = tf.shape(x)[0]

xx = tf.matmul(tf.transpose(x),x)
yy = tf.matmul(tf.transpose(y),y)
xy = tf.matmul(tf.transpose(x),y)
sx = tf.reduce_sum(x,0)
sy = tf.reduce_sum(y,0)
E = (a*a*xx)+(tf.cast(n,tf.float32)*b*b)+yy+(2*a*b*sx)+(-2*a*xy)+(-2*b*sy)
opt = tf.train.GradientDescentOptimizer(0.0001)
step = opt.minimize(E)
session = tf.InteractiveSession()
session.run(tf.initialize_all_variables())
feed_dict={x:[[2],[5],[3],[3],[7],[9]],y:[[2],[3],[6],[4],[6],[8]]}
for i in range(30):
	print session.run(step, feed_dict=feed_dict)
	print session.run(E, feed_dict=feed_dict)
	a_,b_ = session.run([a,b], feed_dict=feed_dict)
	print [a_,b_]
	plt.clf()
	plt.scatter(feed_dict[x],feed_dict[y])
	plt.hold('on')
	plt.plot([-5,10],[a_*(-5)+b_,a_*10+b_])
	plt.pause(1.0)
