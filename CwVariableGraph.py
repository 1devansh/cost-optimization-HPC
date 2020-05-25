from __future__ import division
import random
import math
from itertools import combinations
import matplotlib.pyplot as plt


def fact(n):
    return math.factorial(n)


def comb(p, v):
    return fact(p)/(fact(v)*fact(p-v))


def graph(p, beta, alpha, CpiR, CpiV, Cw, temp):
    P = []
    c = []
    for i in range(1, p+1):
        C = 0
        P.append(i)
        Tpar = (beta * 12) + ((1-beta) * 12)/i

        for j in range(i):
            R = (alpha ** j) * ((1-alpha)**(i-j)) * comb(i, j)
            C += ((Tpar * R) * ((i - j) * CpiR + j * CpiV))
        C = C + Tpar * Cw[temp]
        c.append(C)
    return P, c


p = 128
CpiR = 0.2
CpiV = 0.02
Cw = [0,1,2,5,10]
beta = 0.1
alpha = 0.85
fig, (one) = plt.subplots(1, 1)

for temp in range(5):
    L, M = graph(p, beta, alpha, CpiR, CpiV, Cw, temp)
    one.plot(L, M, label='Cw = '+str(Cw[temp]))


fig.suptitle(
    'Cost for parallel computations with different opportunity cost till p = 128')
one.set_ylabel('Cost(p)')
one.set_xlabel('No. of processors (P)')
one.legend()
plt.show()
