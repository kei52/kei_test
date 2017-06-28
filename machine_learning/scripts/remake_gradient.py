import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# common

x = tf.placeholder(tf.float32, shape=[None,1])
print x
print type(x)

y = tf.placeholder(tf.float32, shape=[None,1])
print y

a = tf.Variable(tf.random_normal(shape=[]))
print 'a:{0}'.format(a)

b = tf.Variable(tf.random_normal(shape=[]))
print 'b:{0}'.format(b)


