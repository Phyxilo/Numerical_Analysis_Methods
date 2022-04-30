#!/usr/bin/python

import numpy as np
import math

def Function(x):

	funct = x**2 + 10*x - 23

	return(funct)

def rootEstimate(xU, xL):

	xR = (xL * Function(xU) - xU * Function(xL)) / (Function(xU) - Function(xL))

	return(xR)


xU = xU
Roots.append(rootEstimate(xU, xL))

xU = -xU
Roots.append(rootEstimate(xU, xL))
