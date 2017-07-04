import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#plt.switch_backend('agg')

'''
x0 = 1
b = 0
w1 = 2
w2 = 20
'''

#print 'x:{0}'.format(x)
#print 'w:{0}'.format(w)

class Perseptron():

    def __init__(self, b=0, w1=2, w2=20):
        self.x0 = 1
        self.b = b
        self.w1 = w1
        self.w2 = w2

    def net_function(self,x1,x2):
        u = self.x0 * self.b + x1 * self.w1 + x2 * self.w2
        #print 'u={0}'.format(u)
        return u

    def step_function(self,x):
        return np.int32(x >= 0)


def main():
    pr = Perseptron()
    # execute only if run as a script
    net_f = pr.net_function(1,1)
    ans = pr.step_function(net_f)
    print 'ans={0}'.format(ans)
    x1 = np.arange(-3,3,0.25)
    x2 = np.arange(-3,3,0.25)
    X1,X2 = np.meshgrid(x1,x2)
    print X1,X2 
    ANS = pr.net_function(X1,X2)
    '''
    x1 = np.arange(-1,1,0.1)
    x2 = np.arange(-,1,0.1)
    X1,X2 = np.meshgrid(x1,x2)
    ANS = step_function(net_function(X1,X2))
    '''
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(X1,X2,ANS)

    plt.show()

if __name__ == "__main__":
    main()
