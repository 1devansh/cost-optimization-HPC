from __future__ import division
import random
import math
from itertools import combinations


p = 128
r = 64
v = 64


def fact(n):
    return math.factorial(n)
    

def comb(p,v):
    return fact(p)/(fact(v)*fact(p-v))

alpha = random.randint(85,96)

#comb = combinations(p, v)
#R = alpha *v + (1-alpha) * (p-v) * 70


CpiR = 0.2
CpiV = 0.02
Cw = 1

beta = 0.3

alpha = 0.85

Tpar = (beta * 12) + ((1-beta) * 12)/p


C = 0
for i in range(p):
    R = (alpha ** i) * ((1-alpha)**(p-i)) * comb(p,i)
    C += ((Tpar * R) * ((p - i) * CpiR + i * CpiV))

C =C + Tpar * Cw
print(C)
