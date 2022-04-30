#!/usr/bin/python

import numpy as np
import math

def Function(x):	#Function of data points

	Z = [2.5, 1.25, 0]
	T = [10, 12, 13.5]
	Output = 0

	for i in range (0, len(Z)):
		if (Z[i] == x):

			Output = T[i]

	#Output = -0.1 * x**4 - 0.15 * x**3 - 0.5 * x**2 - 0.25 * x + 1.2
	#Output = (math.cos(100*x**2))**5/(x**3)
	return(Output)

def ForwardDif(x, h, rank):	#Forward Difference Method function

	if (rank == 1):
		dif = (Function(x + h) - Function(x)) / (h)
	if (rank == 2):
		dif = (Function(x + 2*h) - 2 * Function(x + h) + Function(x)) / h**2

	return(dif)

def BackwardDif(x, h, rank):	#Backward Difference Method

	if (rank == 1):
		dif = (Function(x) - Function(x - h)) / (h)
	if (rank == 2):
		dif = (Function(x) - 2*Function(x - h) + Function(x - 2*h)) / h**2

	return(dif)

def CenteredDif(x, h, rank):	#Centered

	if (rank == 1):
		dif = (Function(x + h) - Function(x - h)) / (2 * h)
	if (rank == 2):
		dif = (Function(x + h) + Function(x - h) - 2 * Function(x)) / h**2

	return(dif)

def ModifiedFD(x, h):	#Modified Forward Difference Method Function

	dif = (- Function(x + 2*h) + 4*Function(x + h) - 3*Function(x))/ (2*h)

	return(dif)

def Richardson(x, h, end):	#Richardson Difference Method
	m = 1

	D0 = []
	
	for i in range (0, end + 1):
		D0.append(CenteredDif(x, h/(2**i), 1))

	for i in range (1, end + 1):

		DList = []

		for m in range (m, end + 1):

			for n in range (m, m+1):

				DList.append(D0[n-i+1] + (1/(4**m-1))*(D0[n-i+1] - D0[n-i]))
		
		D0 = DList
		m = i + 1

	return(DList[0])

def Solution(x):	#This function converts Temperature in to heat flux

	rho = 1800
	C = 840
	k = 3.5*10**(-7)

	q = -k * rho * C * x

	return(q)

"""print(ForwardDif(1, 0.1, 1))
print(BackwardDif(1, 0.1, 1))
print(CenteredDif(1, 0.1, 1))
print(ForwardDif(1, 0.1, 2))
print(BackwardDif(1, 0.1, 2))
print(CenteredDif(1, 0.1, 2))
print(CenteredDif(1.3, 1/4096, 1))
print(Richardson(1.3, 1/4096, 5))"""

print("Temperature is (Forward Difference Method): ", ForwardDif(0, 1.25, 1))
print("Heat Flux is (Forward Difference Method): ", Solution(ForwardDif(0, 1.25, 1)))
print("Temperature is (Modified Forward Difference Method): ", ModifiedFD(0, 1.25))
print("Heat Flux is (Modified Forward Difference Method): ", Solution(ModifiedFD(0, 1.25)))
