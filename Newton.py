#!/usr/bin/python

import numpy as np
import math

Guess = 5
Tol = 0.001

def Derivative(x):#Function of Derivative

	d = (-1/2)*math.exp(-x/2)- (2*math.cos(x)) + (2*x*math.sin(x))
	
	return(d)

def Funct(x):#Funciton

	funct = math.exp(-x/2) - (2*x*math.cos(x)) + 5
	
	return(funct)

def Compute(x):#Function that computes value of the desired function

	Output = -Funct(x)/Derivative(x)

	return(Output)

while (Guess - Compute(Guess) > Tol):

	Guess = Compute(Guess)
	

print(Guess)
