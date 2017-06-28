#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import matplotlib.pyplot as plt
from numpy.random import *

#placeholderは後から値を入れれる関数
x = tf.placeholder(tf.float32, shape=[None,1])
y = tf.placeholder(tf.float32, shape=[None,1])
#Variableでa,bを変数で宣言
a = tf.Variable(tf.random_normal(shape=[]))
b = tf.Variable(tf.random_normal(shape=[]))
#castでfloat32に変換
n = tf.cast(tf.shape(x)[0], tf.float32)
xx = tf.matmul(tf.transpose(x),x)
yy = tf.matmul(tf.transpose(y),y)
xy = tf.matmul(tf.transpose(x),y)
#xのベクトルの作成
sx = tf.reduce_sum(x,0)
sy = tf.reduce_sum(y,0)
#平均の計算式
E = tf.reduce_mean((a*x+b-y)**2,0)

#学習率の設定
opt = tf.train.GradientDescentOptimizer(0.1)
#最小値の計算を行う
step = opt.minimize(E)
session = tf.InteractiveSession()
session.run(tf.initialize_all_variables())
#元の関数にノイズを追加
an = 1
bn = 2
xn = randn(1000,1)
#feed_dictでx,yに与える値
feed_dict = {x:xn,y:an*xn+bn+randn(1000,1)}
#200回行う，pltを使ってグラフを可視化
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
