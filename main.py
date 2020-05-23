from __future__ import division
import random
import math
from itertools import combinations
import matplotlib.pyplot as plt

def fact(n):
    return math.factorial(n)
    

def comb(p,v):
    return fact(p)/(fact(v)*fact(p-v))

alpha = random.randint(85,96)

#comb = combinations(p, v)
#R = alpha *v + (1-alpha) * (p-v) * 70
p = 128
CpiR = 0.2
CpiV = 0.02
Cw = 1
beta = 0.3
alpha = 0.85

Tpar = (beta * 12) + ((1-beta) * 12)/p

C = 0
P =[]
c = []

for i in range(1,p+1):
    P.append(i)
    for j in range(1,i+1):
        
        R = (alpha ** j) * ((1-alpha)**(i-j)) * comb(i,j)
        C += ((Tpar * R) * ((i - j) * CpiR + j * CpiV))
    C =C + Tpar * Cw
    c.append(C)

plt.plot(P,c)
plt.show()
plt.title('Cost for parallel computations with different scalabilty')
print(P)
print(c)
