#!/usr/bin/python

import numpy as np
import math

def Function(x, functNum):	#Functions

	funct = 0

	if (functNum == 1):
		funct = math.sin(x)

	if (functNum == 2):
		funct = 1/(2**(1/2))*math.exp(-x**2)

	if (functNum == 3):
		funct = (3/2)*(x**(1/2))

	return (funct)

def CenteredDif(x, h, rank):	#Centered Differentiation Method. I used this method to find second derivative of the functions.

	if (rank == 1):
		dif = (Function(x + h) - Function(x - h)) / (2 * h)
	if (rank == 2):
		dif = (Function(x + h) + Function(x - h) - 2 * Function(x)) / h**2

	return(dif)

def MidPoint(Min, Max, n, functNum):	#Mid Point Method

	Sum = 0
	dx = (Max-Min)/n

	for i in range (n):

		Sum += Function(Min, functNum)*dx
		Min += dx

	return (Sum)

def Trapezoid(Min, Max, n, functNum):	#Trapezoid Method

	Sum = 0
	x0 = Min
	sln = 0
	specialSum = 0
	dx = (Max-Min)/n

	for i in range (n):

		Sum += dx*(Function(Min + dx, functNum) + Function(Min, functNum))/2
		Min += dx

	#Special Case for Trapezoid Method
	"""
	for i in range (int((Max-Min)/dx)-1):

		specialSum += Function(Min)
		Sum = dx*(specialSum + (1/2)*Function(x0) + Function(Max))
		Min += dx
	"""
	return (Sum)

def Simpson(Min, Max, n, functNum):	#Simpson Method

	fMid = 0
	dx = (Max-Min)/n

	for i in range (1, n):

		if (i % 2 == 0):

			fMid += 2*Function(Min + i*dx, functNum)
		else:

			fMid += 4*Function(Min + i*dx, functNum)

	Parab = (dx/3) * (Function(Min, functNum) + fMid + Function(Max, functNum))

	return(Parab)

def Interval(Min, Max, h, err):	#Function that calculates minimum interval value for wanted accuracy (for Trapezoid Method)

	dif = 0
	x0 = Min

	for i in range (int((Max-Min)/h)):	

		if (dif < CenteredDif(Min, h, 2)):

			dif = CenteredDif(Min, h, 2)

		Min += h

	dx = (Max-x0)/((((Max-x0)/12)*dif/err)**(-1/2))

	return (dx)

print("Mid Point Method(Function 1): ", MidPoint(0, math.pi, 10, 1))
print("Trapezoid Method(Function 1): ", Trapezoid(0, math.pi, 10, 1))
print("Simpson Method(Function 1): ", Simpson(0, math.pi, 10, 1))
print("")
print("Mid Point Method(Function 2): ", MidPoint(-5, 5, 10, 2))
print("Trapezoid Method(Function 2): ", Trapezoid(-5, 5, 10, 2))
print("Simpson Method(Function 2): ", Simpson(-5, 5, 10, 2))
print("")
print("Mid Point Method(Function 3): ", MidPoint(0, 1, 10, 3))
print("Trapezoid Method(Function 3): ", Trapezoid(0, 1, 10, 3))
print("Simpson Method(Function 3): ", Simpson(0, 1, 10, 3))
