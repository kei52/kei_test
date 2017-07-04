import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.random import *
import tensorflow as tf
import rospy
#spam mail system

class Perseptron():
    def __init__(self,session=1000,opt=0.00005,):
        # session number
        self.session = session
        # input data
        self.x1 = [1,1]
        self.x2 = [1,0]
        self.x3 = [0,1]
        self.x4 = [0,0]
        # learning
        self.opt = tf.train.GradientDescentOptimizer(opt)

    def calc_E(self):
        E = self.yi - self.fu
        return E

    def calc_u(self):
        self.u = xj_i * wj_i - b
        return self.u

    '''    
    def calc_J(self):
        J = self
        return J
    '''

    def sig_func(self, x):
        sig_f = 1 / (1+math.exp(-x)) 
        return sig_f

    def sig_grd(self, x):
        sig_g = (1-self.sig_func(x)) * self.sig_func(x)
        return sig_g

    def matmul(x,w):
        u = tf.matmul(x,tf.transpose(w))
        print 'u:{}'.format(u)
        return u

def main():
    # add noise
    pr = Perseptron()
    session = tf.InteractiveSession()
    session.run(tf.initialize_all_variables())
    for i in range(200):
        i = i +1
        #print i
  	#plt.clf()
	  #plt.scatter(feed_dict[x],feed_dict[y])
	  #plt.hold('on')
	  #xi = np.linspace(-3,3,100)
	  #plt.plot(xi,np.array([function(xi,a_,b_,c_,d_),
    #function(xi,an,bn,cn,dn)]).transpose())
	  #plt.pause(0.001)  

if __name__ == '__main__':
    main()
    
