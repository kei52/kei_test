import numpy as np
import matplotlib.pyplot as plt
import math
import rospy
u = 0
def calc_u(x):
    global u
    print 'u:{}'.format(u)
    u = u + x
    #print 'u:{}'.format(u)
    return u
    
#a = calc_u(2)
#print type(a)
#print 'a:{}'.format(a)

for i in range(10):
    i = i+1
    print 'i:number"{}"'.format(i)
    b = calc_u(i)
    print 'b:{}'.format(b),'\n'

#print len(a)

