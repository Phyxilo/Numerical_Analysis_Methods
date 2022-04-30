#!/usr/bin/python

import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def Function(y1, y2):	#Differential Equation

	f = []

	#f1 = y2
	#f2 = 1 - y1

	f1 = y2
	f2 = 1 - 3*y2- 6*y1

	f.append(f1)
	f.append(f2)

	return (f)

def Boundaries(xi1, yi1, xi2, yi2):	#Function of Boundary values

	xi = []
	yi = []
	xf = []

	xi.append(xi1)
	xi.append(xi2)
	yi.append(yi1)
	yi.append(yi2)

	return(xi, yi)

def RungeeKutta (bound ,h ,xf , f):	#Function that solves Differential Equation by using Rungee-Kutta Method

	Sln = []
	y = []

	K1 = []
	K2 = []

	xArr = []
	yArr = []

	w1 = w2 = 1/2
	a = 1
	b = a

	xi1 = bound[0][0]
	xi2 = bound[0][1]
	yi1 = bound[1][0]
	yi2 = bound[1][1]

	for i in range(int(abs(xf-xi1)/h)+1):
	
		K1.clear()
		K2.clear()		

		K1.append(h * f(0, yi2)[0])
		K1.append(h * f(yi1, 0)[1])

		K2.append(round(h * (f(0, yi2 + K1[0])[0] + h), 4))
		K2.append(round(h * (f(yi1 + K1[1], 0)[1] + h), 4))

		yi1 = yi1 + w1*(K1[0]+K2[0])
		yi2 = yi2 + w1*(K1[1]+K2[1])

		xArr.append(round(i*h, 3))
		yArr.append(round(yi1, 3))

	y.append(yi1)
	y.append(yi2)

	return (xArr, yArr)

def drawGraph(x, y):	#Function that draws measured points
	
	plt.plot(x, y)

	plt.xlabel("t")
	plt.ylabel("x")

	plt.show()

xAxis = RungeeKutta(Boundaries(0, 4, 0, 1), 0.1, 1, Function)[0]
yAxis = RungeeKutta(Boundaries(0, 4, 0, 1), 0.1, 1, Function)[1]


for i in range (len(yAxis)):	#Loop That prints all of the U(x) values for each t, where x=[0,1]
	print(xAxis[i], " = ", yAxis[i])

drawGraph(xAxis, yAxis)
