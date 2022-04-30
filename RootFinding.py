#!/usr/bin/python

import numpy as np
import math

xU = 5
xL = 0

Roots = []

Tolerance = 0.000001

def Function(x):	#Fuction that we want to find roots

	funct = x**2 -3

	return(funct)

def SignCheck(x1, x2):	#This function finds sign of the multplication of xU and xL

	Mult = 0
	signNeg = False

	Mult = Function(x1) * Function(x2)

	if(Mult > 0):
		signNeg = False
	else:
		signNeg = True

	return(signNeg, Mult)

def xCheck(xU, xL):	#This function checks sign of xU and xL while getting closer to the roots

	xULim = 0
	xLLim = 0

	while (SignCheck(xU, xL)[0] == True):

		xU = (xL + xU)/2
		xULim = 2*xU - xL
	
	xU = xULim


	while (SignCheck(xU, xL)[0] == True ):

		xL = (xL + xU)/2
		xLLim = 2*xL - xU
		
	xL = xLLim


	return(xU, xL)

def rootEstimate(xU, xL):	#This Function estimate root value for False Position Method(Not Working!)


	xULim = 0
	xLLim = 0
	U = True
	L = True
	xR = ((xL * Function(xU)) - (xU * Function(xL))) / (Function(xU) - Function(xL))

	if(Function(xL) < 0 and Function(xU) > 0):
		
		if(Function(xR) < 0 and L == True):	
			xL = xR
			L = False
			U = True

		if(Function(xR) > 0 and U == True):
			xU = xR
			U = False
			L = True

	return(xU, xL, xR)



def findRoot(xU, xL):	#This function finds root until xU - xL reach tolerance

	root = False

	while(abs(xCheck(xU, xL)[0] - xCheck(xU, xL)[1]) >= Tolerance):

		xU = xCheck(xU, xL)[0]
		xL = xCheck(xU, xL)[1]

		xCheck(xU, xL)
		root = True

	return(xU, xL, root)

def findRoot_FalsePos(xU, xL):	#This function calculates root by using False Position Method(Not Working!)

	while(abs(rootEstimate(xU, xL)[0] - rootEstimate(xU, xL)[1]) >= 3):

		xU = rootEstimate(xU, xL)[0]
		xL = rootEstimate(xU, xL)[1]

		rootEstimate(xU, xL)
		#print(abs(rootEstimate(xU, xL)[0] - rootEstimate(xU, xL)[1]))

	return(xU, xL)

#These codes calculates both of the roots and append it into Roots list

xU = xU
Roots.append(findRoot(xU, xL)[0])

xU = -xU
Roots.append(findRoot(xU, xL)[0])

print(Roots)
