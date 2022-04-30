#!/usr/bin/python

import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def Function(x, y):	#Differential Equation

	#f = 1 + y**2 + x**3

	f = (x**2)*math.exp(-(y+1))

	return (f)

def RungeeKutta (xi, yi, h, a, xf, f):	#Function that solves Differential Equation by using Rungee-Kutta Method

	xArr = []
	yArr = []

	xInit = xi

	w1 = w2 = 1/2
	b = a

	for i in range(int(abs((xi-xf))/h) + 1):
		
		K1 = h * f(xi, yi)
		K2 = h * f(xi + a*h, yi + b*K1)

		yi = round(yi + w1*K1 + w2*K2, 6)
		xi = round(xInit + i*h, 2)

		xArr.append (xi)
		yArr.append (yi)


	return (yi, xArr, yArr)


def drawGraph(x, y):	#Function that draws measured points
	
	plt.plot(x, y)

	plt.xlabel("x")
	plt.ylabel("U (x)")

	plt.show()

xAxis = RungeeKutta(0, 1, 0.01, 1, 3, Function)[1]
yAxis = RungeeKutta(0, 1, 0.01, 1, 3, Function)[2]

for i in range (len(yAxis)):	#Loop That prints all of the U(x) values for each x, where x=[0,3]
	print("U(",xAxis[i],")", " = ", yAxis[i])

drawGraph(xAxis, yAxis)
