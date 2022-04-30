#!/usr/bin/python

import numpy as np
import math

def Function(x, y, Order):

	if (Order == 1):

		#dif = 1 + x**2
		dif = 1 - 2*(y**2) - x

	if (Order == 2):

		#dif = 2*x
		dif = (-1 - 4*y*(1 - 2*(y**2) - x))


	return(dif)


def EulerMethod(Pnt, x0, y0, h):

	y = y0	

	for i in range(int(abs(Pnt-x0)/h)):

		x = x0 + i*h

		y = y + h * Function(x, y, 1)

	return(y)

def TaylorMethod(Pnt, x0, y0, h):

	y = y0

	for i in range(int(abs(Pnt-x0)/h)):

		x = x0 + i*h

		y = y + h * Function(x, y, 1) + ((h**2)/2) * Function(x, y, 2)

	return(y)

#print(EulerMethod(1.03, 1, -4, 0.01))
#print(TaylorMethod(1.03, 1, -4, 0.01))

print(EulerMethod(0.03, 0, 1, 0.01))
print(TaylorMethod(0.03, 0, 1, 0.01))
