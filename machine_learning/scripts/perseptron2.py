import numpy as np
import matplotlib.pyplot as plt
from sympy import  *
from mpl_toolkits.mplot3d import Axes3D
import sympy as sym
import rospy

def gradiate(x):
    print x

x = Symbol("x")
f = x**2 + sin(x) + cos(x)
print f


sym.init_printing()

Pi = sym.S.Pi
E = sym.S.Exp1
I = sym.S.ImaginaryUnit
oo = sym.oo

(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) = sym.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

print sym.limit(1/x,x,0)


#print dir(b)

#a = Rational(1,2)

#print a





gradiate(5)


#if __name__ == "__main__":
