#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random

count = 0
step = 1

class MLP:
    def __init__(self):
        """mlp using sigmoid
        mid_num: 中間層ノード数
        out_num: 出力層ノード数
        epochs: 学習回数
        r: 学習率
        a: シグモイド関数の定数
        """
        self.mid_num = 5
        self.out_num = 1
        self.epochs = 1000000
        self.r = 0.5
        self.a = 1

    def sigmoid(self, x):
        #print 'sigmoid:{}'.format(1 / (1 + np.exp(-self.a * x))),'\n'
        return 1 / (1 + np.exp(-self.a * x))

    def sigmoid_(self, x):
        """シグモイド関数微分"""
        #print 'sigmoid_:{}'.format(self.a * x * (1.0 - x))
        return self.a * x * (1.0 - x)

    def calc_out(self, w_vs, x_v):
        #print 'calc_out:{}'.format(self.sigmoid(np.dot(w_vs, x_v)))
        return self.sigmoid(np.dot(w_vs, x_v))

    def out_error(self, d_v, out_v):
        """出力層の誤差"""
        return (out_v - d_v) * self.sigmoid_(out_v)

    def mid_error(self, mid_v, eo_v):
        """中間層の誤差"""
        return np.dot(self.wo_vs.T, eo_v) * self.sigmoid_(mid_v)

    def w_update(self, w_vs, e_v, i_v):
        """重み更新"""
        e_v = np.atleast_2d(e_v)
        i_v = np.atleast_2d(i_v)
        return w_vs - self.r * np.dot(e_v.T, i_v)

    def add_bias(self, x_v):
        """バイアス項追加"""
        return np.append(x_v, 1)

    def fit(self, X, y):
        """
        学習
        X_train,y_trainを後々に入れる
        """
        print '\n===============step"1"==============='
        x_vs = X
        d_vs = y

        x_vs = [self.add_bias(x) for x in x_vs]
        x_vd = len(x_vs[0])

        # 重み
        self.wm_vs = np.random.uniform(-1, 1., (self.mid_num, x_vd))
        self.wo_vs = np.random.uniform(-1., 1., (self.out_num, self.mid_num))

        for n in range(self.epochs):
            for d_v, x_v in zip(d_vs, x_vs):
                global count
                count = count + 1
                print '\n-----count"{}"-----'.format(count)

                # forward phase
                # 中間層の結果
                mid_v = self.calc_out(self.wm_vs, x_v)
                mid_v[-1] = -1
                print 'hidden layer result:{}'.format(mid_v)
                # 出力層の結果
                out_v = self.calc_out(self.wo_vs, mid_v)
                print 'output layer result:{}'.format(out_v)
                # backward phase
                # 出力層の誤差
                eo_v = self.out_error(d_v, out_v)
                print 'output layer error:{}'.format(eo_v)
                # 中間層の誤差
                em_v = self.mid_error(mid_v,  eo_v)
                print 'hidden layer:{}'.format(em_v)
                #print len(em_v)

                # weight update
                # 中間層
                self.wm_vs = self.w_update(self.wm_vs, em_v, x_v)
                print 'wight update:{}'.format(self.wm_vs)
                #print len(self.wm_vs)

                # 出力層
                self.wo_vs = self.w_update(self.wo_vs, eo_v, mid_v)
                print 'wo_vs:{}'.format(self.wo_vs)

                global step
                if count % 4 == 0:
                   step = step + 1


    def predict(self, x_v):
        x_v = self.add_bias(x_v)
        mid_v = self.calc_out(self.wm_vs, x_v)
        out_v = self.calc_out(self.wo_vs, mid_v)
        return out_v




if __name__ == "__main__":

    # data
    X_train = [[0, 0], [1, 0], [0, 1], [1, 1]]
    y_train = [0, 1, 1, 0]


    mlp = MLP()
    mlp.fit(X_train, y_train)

    result = [mlp.predict(x) for x in X_train]

    #print 'mlp:{}'.format(mlp)
    print 'result:{}'.format(result)

    print '\n===============step"{}"==============='.format(step)
    #print 'X_train:{}'.format(X_train)
    #print 'y_train:{}'.format(y_train)
    #[print(r, ":", y) for r, y in zip(result, y_train)]
