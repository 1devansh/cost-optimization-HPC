import random
from itertools import combinations

p = 8
r = 4
v = 4

Tpar = 10

alpha = random.randint(85,96)
#comb = combinations(p, v)
R = alpha *v + (1-alpha) * (p-v) * 70

C = 0
CpiR = 0.2

CpiV = 0.02
Cw = 1
beta = 0.1
alpha = 0.85
Tpar = (beta * 12) + ((1-beta) * 12)/p
for i in range(p):
    C += ((Tpar * R) * ((p - i) * CpiR + i * CpiV)) + Tpar * Cw

print(C)