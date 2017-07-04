import numpy as np
import random

class MLP:

    def __init__(self, mid_num, out_num, epochs, r=0.5, a=1):
        '''
        mid_num: middle layer number
        out_num: output layer number
        epochs: learning number
        r: learning
        a: constant by sigmoid function
        '''

        self.mid_num = mid_num
        self.out_num = out_num
        self.epochs = epochs
        self.r = r
        self.a = a

    # sigmoid function
    def sigmoid(self, x):
        return 1/(1+np.exp(-self.a*x))

    # sigmoid differentiating
    def sigmoid_diff(self, x):
        return self.a * x * (1.0 - x)


    def calc_out(self, w_vs, x_v):
        return self.sigmoid(np.dot(w_vs, x_v))

    def out_error(self, d_v, out_v):
        # output layer error
        return (out_v - d_v) * self.sigmoid_diff(out_v)

    def mid_error(self, mid_v, eo_v):
        # middle layer error
        return np.dot(self.wo_vs.T,eo_v) * self.sigmoid_diff(mid_v)

    def w_update():
        # weight update
        e_v = np.atleast_2d(e_v)
        i_v = np.atleast_






if __name__ == '__main__':
    x_train = [[0,0],[1,0],[0,1],[1,1]]
    y_train = [0,1,1,0]

    mid_num = 5
    out_num = 1
    epochs = 10000

   mlp = MLP(mid_num, out_num, epochs)
   mlp.fit(x_train, y_train)

   result = [mlp.predict(x) for x in x_train]

   [print (r,":",y) for r, y in zip(result, y_train)]
