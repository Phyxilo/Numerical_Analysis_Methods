#!/usr/bin/python

import numpy as np
import math
import matplotlib.pyplot as plt

xAxis = []
xInit = 0
L = 20
h = 0.1

for i in range (int(L/h) + 1):	#X Axis

	xAxis.append(xInit + round(i*h, 2))

def Function(x, t):

	L = 20
	a = 10

	phi = math.exp(-a*(x-(1/2)*L)**2)	
	psi = 0

	return(phi, psi)

def Wave(x, t, k, h, f):	#Solution of the Wave Equation

	s = (k**2)/(h**2)

	u = (1/2)*s*(f(x + h, t)[0] + f(x - h, t)[0]) + (1 - s)*f(x, t)[0] + k*f(x, t)[1]
	
	return(u)

U = []
UExact = []
UInit = []


for i in range (len(xAxis)):	#Array of Initial Condition, Numerical solution and Exact solution

	UInit.append(Function(xAxis[i], 0)[0])
	U.append(Wave(xAxis[i], 1, h, h*(0.9**(1/2)), Function))
	UExact.append((1/2)*(Function(xAxis[i]+1, 1)[0]+Function(xAxis[i]-1, 1)[0]))


plt.plot(xAxis, UInit)
plt.plot(xAxis, U)
plt.show()

