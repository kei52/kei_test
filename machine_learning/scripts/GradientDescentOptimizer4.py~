#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow as tf
import matplotlib.pyplot as plt
from numpy.random import *
import numpy as np

def function(x,a,b,c,d):
	return a*x**3+b*x**2+c*x+d

#placeholderは後から値を入れれる関数
x = tf.placeholder(tf.float32, shape=[None,1])
y = tf.placeholder(tf.float32, shape=[None,1])
#Variableでa,bを変数で宣言
a = tf.Variable(tf.random_normal(shape=[]))
b = tf.Variable(tf.random_normal(shape=[]))
c = tf.Variable(tf.random_normal(shape=[]))
d = tf.Variable(tf.random_normal(shape=[]))
#castでfloat32に変換
n = tf.cast(tf.shape(x)[0], tf.float32)
xx = tf.matmul(tf.transpose(x),x)
yy = tf.matmul(tf.transpose(y),y)
xy = tf.matmul(tf.transpose(x),y)
#xのベクトルの作成
sx = tf.reduce_sum(x,0)
sy = tf.reduce_sum(y,0)
#平均の計算式
E = tf.reduce_mean((function(x,a,b,c,d)-y)**2,0)

#学習率の設定
opt = tf.train.GradientDescentOptimizer(0.01)
#最小値の計算を行う
step = opt.minimize(E)
session = tf.InteractiveSession()
session.run(tf.initialize_all_variables())
#元の関数にノイズを追加
an = 1
bn = 2
cn = 1
dn = 2
xn = randn(100,1)
#feed_dictでx,yに与える値
feed_dict = {x:xn,y:function(xn,an,bn,cn,dn)+randn(100,1)}
#200回行う，pltを使ってグラフを可視化
for i in range(200):
	print session.run(step, feed_dict)
	print session.run(E, feed_dict)
	a_,b_,c_,d_ = session.run([a,b,c,d], feed_dict)
	print [a_,b_,c_,d_]
	plt.clf()
	plt.scatter(feed_dict[x],feed_dict[y])
	plt.hold('on')
	xi = np.linspace(-3,3,100)
	plt.plot(xi,np.array([function(xi,a_,b_,c_,d_),function(xi,an,bn,cn,dn)]).transpose())
	plt.pause(0.001)
