#!/usr/bin/python

import numpy as np
import math

xp = 5.1
xi = 5.0
E = 0.001
Roots = []

def Funct(x):#Function

	funct = math.exp(-x/2) - (2*x*math.cos(x)) + 5

	return(funct)

def findRoots(xi, xp):#Function that calculates roots

	xf = xp - (Funct(xi) * (xp - xi)) / (Funct(xp) - Funct(xi))

	return (xf)

def Secant():#Function that shifts values

	global xi
	global xp

	x1 = findRoots(xi, xp)
	x0 = xi

	xi = x1
	xp = x0

def Check():

	while(abs(findRoots(xi, xp) - xi) > E):
		Secant()
Check()
print(xi)
