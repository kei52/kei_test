import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#plt.switch_backend('agg')
print '"learning weight"'

class Perseptron():

    def __init__(self, w0=0):
        #self.x0 = 1
        self.w0 = w0
        self.wn = np.array([[2,1]])

        print 'weight1:{}'.format(self.wn)

    def net_function(self,x_in):
        self.x_in = np.array(x_in)
        wn_t = self.wn.T

        print type(self.x_in)
        print type(wn_t)


        print self.x_in.shape
        print wn_t
        u = np.dot(self.x_in,wn_t)
        print 'u={0}'.format(u)
        return u

    def step_function(self,x):
        return np.int32(x >= 0)


def main():
    pr = Perseptron()
    # execute only if run as a script
    xv_in = np.array([[1,1]])
    net_f = pr.net_function(xv_in)
    ans = pr.step_function(net_f)
    print 'ans={0}'.format(ans)
    #x1 = np.arange(-3,3,0.25)
    #x2 = np.arange(-3,3,0.25)
    #X1,X2 = np.meshgrid(x1,x2)
    #ANS = pr.net_function(X1,X2)

    #fig = plt.figure()
    #ax = Axes3D(fig)
    #ax.plot_wireframe(X1,X2,ANS)

    #ax.set_xlabel('x1')
    #ax.set_ylabel('x2')
    #ax.set_zlabel('ANS')

    #plt.title('perseptron5.py')
    
    #plt.show()

if __name__ == "__main__":
    main()
