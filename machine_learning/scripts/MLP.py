#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import matplotlib.pyplot as plt
from numpy.random import *
import numpy as np

def function(x,w,b):
	return x*w-b

#placeholderは後から値を入れれる関数
x = tf.placeholder(tf.float32, shape=[None,1])
y = tf.placeholder(tf.float32, shape=[None,1])
#Variableでa,bを変数で宣言
w = tf.Variable(tf.random_normal(shape=[]))
b = tf.Variable(tf.random_normal(shape=[]))
#平均の計算式
E = tf.reduce_mean((function(x,w,b)-y)**2,0)
#学習率の設定
opt = tf.train.GradientDescentOptimizer(0.01)
#最小値の計算を行う
step = opt.minimize(E)
session = tf.InteractiveSession()
session.run(tf.initialize_all_variables())
#元の関数にノイズを追加
wn = 1
xn = randn(100,1)
bn = 1
#feed_dictでx,yに与える値
feed_dict = {x:xn,y:function(xn,wn,bn)+randn(100,1)}
#200回行う，pltを使ってグラフを可視化
for i in range(200):
	print session.run(step, feed_dict)
	print session.run(E, feed_dict)
	wn,bn = session.run([wn,bn], feed_dict)
	print [wn,bn]
	'''
	plt.clf()
	plt.scatter(feed_dict[x],feed_dict[y])
	plt.hold('on')
	xi = np.linspace(-3,3,100)
	plt.plot(xi,np.array([function(xi,w,b),function(xi,wn,bn)]).transpose())
	plt.pause(0.001)
	'''
