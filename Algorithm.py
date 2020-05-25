import math
import random
def fact(n):
    return math.factorial(n)


def comb(p, v):
    return fact(p)/(fact(v)*fact(p-v))


CpiR = 0.2
CpiV = 0.02
Cw = 1
alpha = random.randint(85,95)
alpha = float(alpha/100)

Tser = float(input("Enter the time taken in series by a single processor to complete the task: "))
beta = float(input("Enter scalabilty(0 to 1) of the parallel systems:  "))
p = int(input("Enter constant number of processors you want to divide the task into: "))

Tpar = (beta * Tser) + ((1-beta) * Tser)/p

print("Time taken in parallel is ", Tpar)
C= 0
for j in range(p):
    R = (alpha ** j) * ((1-alpha)**(p-j)) * comb(p, j)
    C += ((Tpar * R) * ((p - j) * CpiR + j * CpiV))
C = C + Tpar * Cw
print("Optimized cost for doing this task in parallel using volatile and reserved resources is ", C)
