#!/usr/bin/python

import numpy as np
import math

def Function(x):

	Int = math.exp(x) * math.cos(x)

	return (Int)

def GaussQuad(b, a, f):

	c1 = (b - a)/2
	c2 = (b - a)/2

	x1 = ((b - a)/2)*(-1/math.sqrt(3)) + (b + a)/2
	x2 = ((b - a)/2)*(1/math.sqrt(3)) + (b + a)/2

	return(c1*f(x1) + c2*f(x2))

print(GaussQuad(1.5, 0.5, Function))
