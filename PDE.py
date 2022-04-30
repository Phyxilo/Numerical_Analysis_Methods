#!/usr/bin/python

import numpy as np
import math

def Function(x, y):

	funct = math.sin(math.pi * x)

	return(funct)

def explicitMethod(x, t, k, h, funct):

	a = k/(h**2)

	T = a*funct(x-h, t) + (1 - 2*a) * funct(x, t) + a*funct(x+h, t)

	return(T)

def CrankNicolsonMethod(x, t, k, h, funct):

	a = k/(h**2)

	

#-------Matrix Calculation Part-------

	Matrix = [[9, -4, 0], [-4, 9, -4], [0, -4, 9]]
	Solution = [math.sin(0.25 * math.pi), math.sin(0.5 * math.pi), math.sin(0.75 * math.pi)]


	def rowSubtr(rowX, rowY):	#Subtracting two rows

		Output = []

		for x in range(len(rowX)):

			Output.append(rowX[x] - rowY[x])

		return(Output)

	def rowConstMult(row, const):	#Multpling row with a constant

		Output = []

		for x in range(len(row)):

			Output.append(const * row[x])

		return(Output)


	def Elim(Matrix, Sln, x):	#Elimination Function

		Row = []
		intRow = []
		finalMatrix = Matrix
		finalSolution = Sln

		for i in range(len(Matrix)):

			Row.append(Matrix[i][x])

		for i in range(len(Matrix) - (x + 1)):
		
			intRow = rowSubtr(Matrix[x+i+1], rowConstMult(Matrix[x], (Row[x+i+1] / Row[x])))
			intSln = Sln[x+i+1] - Sln[x] * (Row[x+i+1] / Row[x])

			finalMatrix[x+i+1] = intRow
			finalSolution[x+i+1] = intSln

		return(finalMatrix, finalSolution)

	def backSub(Matrix, Sln):	#Backward Substitution function

		Sum = 0
		Solution = []
		for x in range(len(Matrix)):
			Solution.append(0)

		Solution[len(Matrix)-1] = Sln[len(Matrix)-1] / Matrix[len(Matrix)-1][len(Matrix)-1]
		
		for x in range(1, len(Matrix)):

			Sum = 0
			i = len(Matrix) - x - 1

			for j in range(i+1, len(Matrix)):
				
				Sum += Matrix[i][j] * Solution[j]

			Solution[i] = (Sln[i] - Sum) / Matrix[i][i]

		return(Solution)

	def GaussElim(Matrix, Sln):	#Naive Gaussian Method

		for x in range(len(Matrix) - 1):

			Matrix = Elim(Matrix, Sln, x)[0]
			Solution = Elim(Matrix, Sln, x)[1]

		xSln = backSub(Matrix, Solution)

		return(Matrix, Solution, xSln)
#----------------------------------

	return(GaussElim(Matrix, Solution)[2])

print(explicitMethod(0.25, 0.25, 0.25, 0.25, Function))
print(CrankNicolsonMethod(0.25, 0.25, 0.25, 0.25, Function))


