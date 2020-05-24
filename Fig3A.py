from __future__ import division
import random
import math
from mpl_toolkits import mplot3d
from itertools import combinations
import matplotlib.pyplot as plt


def fact(n):
    return math.factorial(n)


def comb(p, v):
    return fact(p)/(fact(v)*fact(p-v))


def graph(p, beta, alpha, CpiR, CpiV, Cw):
    P = []
    c = []
    alph =[]
    f = alpha
    for i in range(1, p+1):
        C = 0
        P.append(i)
        alph.append(alpha)
        
        Tpar = (beta[temp] * 12) + ((1-beta[temp]) * 12)/i

        for j in range(i):
            R = (alpha ** j) * ((1-alpha)**(i-j)) * comb(i, j)
            C += ((Tpar * R) * ((i - j) * CpiR + j * CpiV))
        C = C + Tpar * Cw
        c.append(C)
    return P, c, alph


temp = 4

p = 128
CpiR = 0.2
CpiV = 0.02
Cw = 1
beta = [0.01, 0.05, 0.1, 0.2, 0.3]
alpha = 1
fig = plt.figure()
one = plt.axes(projection="3d")
f = alpha
while alpha >0:
    alpha = alpha - f/128
    L, M, A = graph(p, beta, alpha, CpiR, CpiV, Cw)
    one.plot3D(L, A, M)


fig.suptitle(
    'Cost for parallel computations with volatile process of different availability')
one.set_ylabel('Alpha')
one.set_xlabel('No. of processors (P)')
one.set_zlabel('Cost(p)')
one.legend()
plt.show()
