#!/usr/bin/python

import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

r = 1000
rarray = []
x = []
bins = 25

a = 0
b = 1

#Function of function that we want to Intagrate
def Function (y):

	f = math.exp(y)

	return(f)

#Function that applies Monte Carlo Method and find estimated solution of Integral
def MonteCarlo (f):

	for i in range(r):


		xn = np.random.uniform(a, b)
		rarray.append(float(xn))

	Sum = 0

	for i in range (r):

		Sum += f(rarray[i])

	Output = (abs(b-a)/r) * Sum

	rarray.clear()

	return(Output)

#Function for drawing graph of estimated values of Integral
def drawGraph (x):

	plt.hist(x, int(bins), alpha=0.8)

	plt.title("Monte Carlo")
	plt.xlabel("Estimate of Integral")
	plt.ylabel("Arbitrary Axis")

	plt.show()

xarr = []

#This loop finds all of the estimated Integrals and draw their graphs
for i in range (r):

	xarr.append(MonteCarlo(Function))

print(str(MonteCarlo(Function)) + u" \u00B1 " + str(1/(math.sqrt(r))))
drawGraph(xarr)

