import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#plt.switch_backend('agg')

x0 = 1
b = 0
w1 = 2
w2 = 20


#print 'x:{0}'.format(x)
#print 'w:{0}'.format(w)


def net_function(x1,x2):
    u = x0*b+x1*w1+x2*w2
    #print 'u={0}'.format(u)
    return u

def step_function(x):
    return np.int32(x >= 0)

if __name__ == "__main__":
    # execute only if run as a script
    ans = step_function(net_function(1,1))
    print 'ans={0}'.format(ans)
    x1 = np.arange(-3,3,0.25)
    x2 = np.arange(-3,3,0.25)
    X1,X2 = np.meshgrid(x1,x2)
    ANS = net_function(X1,X2)
    '''
    x1 = np.arange(-3,3,0.25)
    x2 = np.arange(-3,3,0.25)
    X1,X2 = np.meshgrid(x1,x2)
    ANS = step_function(net_function(X1,X2))
    '''
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(X1,X2,ANS)

    plt.show()

