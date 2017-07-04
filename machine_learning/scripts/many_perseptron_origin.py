import numpy as np
import matplotlib
#matploli.use('WXAgg')
import matplotlib.pyplot as plt

# training data
N = 50

# learning persent
ETA = 0.1

#loop number
NUM_LOOP = 10000

# input unit number
NUM_INPUT = 2
# hidden unit number
NUM_HIDDEN = 4
# output unit number
NUM_OUTPUT = 1

# Squared error sum
#def spuares_error_sum(xli)

fig = plt.figure()
fig.suptitle('multilayer perceptron',fontsize=18)
#ax = fig.add_subplot(111)

# make training date
xlist = np.linspace(-1, 1, N).reshape(N, 1)
 
