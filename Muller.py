#!/usr/bin/python

import numpy as np
import math

x0 = 4.5
x1 = 5.5
x2 = 5.0

initX0 = x0
initX1 = x1
initX2 = x2

def Funct(x):

	funct = (x**3) - (13*x) - (12)

	return(funct)
	
def Coeff(x0, x1, x2):

	h0 = x1 - x0
	h1 = x2 - x1

	Del0 = (Funct(x1) - Funct(x0)) / (x1 - x0)
	Del1 = (Funct(x2) - Funct(x1)) / (x2 - x1)

	a = (Del1 - Del0) / (h1 + h0)
	b = a * h1 + Del1
	c = Funct(x2)

	return(a, b, c)

def findRoots(x0, x1, x2, root):

	deNum = (Coeff(x0, x1, x2)[1] - ((Coeff(x0, x1, x2)[1])**2 - 4 * Coeff(x0, x1, x2)[0] * Coeff(x0, x1, x2)[2])**(1/2))

	if(root == "+"):
		Root = x2 + (-2 * Coeff(x0, x1, x2)[2]) / (Coeff(x0, x1, x2)[1] + ((Coeff(x0, x1, x2)[1])**2 - 4 * Coeff(x0, x1, x2)[0] * Coeff(x0, x1, x2)[2])**(1/2))

	if (root == "-" and deNum != 0):
		Root = x2 + (-2 * Coeff(x0, x1, x2)[2]) / (Coeff(x0, x1, x2)[1] - ((Coeff(x0, x1, x2)[1])**2 - 4 * Coeff(x0, x1, x2)[0] * Coeff(x0, x1, x2)[2])**(1/2))

	return(Root, deNum)
"""
def Muller(x, x0, x1, x2):

	if (abs(x - x0) > abs(x - x1) and abs(x - x0) > abs(x - x2)):
		x0 = x
	elif (abs(x - x1) > abs(x - x2) and abs(x - x1) > abs(x - x0)):
		x1 = x
	elif (abs(x - x2) > abs(x - x0) and abs(x - x2) > abs(x - x1)):
		x2 = x

	return(x0, x1, x2)
x = 0
while(x < 1):
	x0 = Muller(findRoots(x0, x1, x2)[0], x0, x1, x2)[0]
	x1 = Muller(findRoots(x0, x1, x2)[0], x0, x1, x2)[1]
	x2 = Muller(findRoots(x0, x1, x2)[0], x0, x1, x2)[2]
	x = x + 1
print(Muller(findRoots(x0, x1, x2)[0], x0, x1, x2))"""

def Roots(sign):

	global x0
	global x1
	global x2

	while(True):

		x = findRoots(x0, x1, x2, sign)[0]

		if (abs(x - x0) > abs(x - x1) and abs(x - x0) > abs(x - x2)):
			x0 = x
		elif (abs(x - x1) > abs(x - x2) and abs(x - x1) > abs(x - x0)):
			x1 = x
		elif (abs(x - x2) > abs(x - x0) and abs(x - x2) > abs(x - x1)):
			x2 = x
		if (x.imag == 0):
			x = x.real
		if ((x1 == x0) or (x1 == x2) or (x0 == x2)):
			break
	return(x)

def Reset():

	global x0
	global x1
	global x2

	x0 = initX0
	x1 = initX1
	x2 = initX2

def minusX():

	global x0
	global x1
	global x2

	x0 = -initX0
	x1 = -initX1
	x2 = -initX2

def Muller():

	roots = []

	roots.append(Roots("+"))

	Reset()
	
	roots.append(Roots("-"))

	return(roots)

print (Muller())
