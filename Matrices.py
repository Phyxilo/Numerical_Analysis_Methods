#!/usr/bin/python

import numpy as np
import math


#Matrix = [[6, -2, 2, 4], [12, -8, 6, 10], [3, -13, 9, 3], [-6, 4, 1, -18]]
#Solution = [16, 26, -19, -34]
#Matrix = [[1, -1, 2, 1], [3, 2, 1, 4], [5, -8, 6, 3], [4, 2, 5, 3]]
#Solution = [1, 1, 1, -1]

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

def triDeterminant(Matrix):	#Function that calculates determinant of the matrixs

	Det = 1

	for i in range (len(Matrix)):

		Det *= float(Matrix[i][i])

	return(Det)

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

			"""
			print("i: ",i)
			print("j: ",j)
			print("Matrix: ", Matrix[i][j]," Solution: ", Solution[j])
			print(Sum)
			"""

		Solution[i] = (Sln[i] - Sum) / Matrix[i][i]

	return(Solution)

def GaussElim(Matrix, Sln):	#Naive Gaussian Method (Working)

	for x in range(len(Matrix) - 1):

		Matrix = Elim(Matrix, Sln, x)[0]
		Solution = Elim(Matrix, Sln, x)[1]

	xSln = backSub(Matrix, Solution)

	return(Matrix, Solution, xSln)

#print(GaussElim(Matrix, Solution)[0])
#print(GaussElim(Matrix, Solution)[1])
print(GaussElim(Matrix, Solution)[2])

def GJElim(Matrix, Sln):	#Second part of the elimination function for the Gaussian-Jordan Method

	finalSolution = Sln
	Row = []

	for i in range (len(Matrix)):

		Row.append(0)

	for j in range(len(Matrix)):

		y = len(Matrix) - j - 1

		for i in range(len(Matrix)):

			Row[i] = (Matrix[i][y])

		for i in range(y):

			x = y + 1 - i
			Matrix[x-2] = rowSubtr(Matrix[x-2], rowConstMult(Matrix[y], (Row[x-2] / Row[y])))
			finalSolution[x-2] = Sln[x-2] - Sln[y] * (Row[x-2] / Row[y])
			"""
			print(y, x-2)
			print("Row: ", Matrix[x-2], " Sub: ", rowConstMult(Matrix[y], (Row[x-2] / Row[y])), " Mult: ", (Row[x-2] / Row[y]))
			print(Row)
			"""

	return(Matrix, finalSolution)

def GaussJordan(Matrix, Sln):	#Gaussian-Jordan Method (Working)

	for x in range(len(Matrix) - 1):

		Matrix = Elim(Matrix, Sln, x)[0]
		Solution = Elim(Matrix, Sln, x)[1]

	for i in range(len(Matrix)):

		Solution[i] = Solution[i] / Matrix[i][i]
		Matrix[i] = rowConstMult(Matrix[i], (1 / Matrix[i][i]))

	Matrix = GJElim(Matrix, Solution)[0]
	Solution = GJElim(Matrix, Solution)[1]

	return(Matrix, Solution)

def ScaleGauss(Matrix, Sln):	#Gaussian Elimination with Scaled Partial Pivoting Method (Not Working)

	firstClmn = []
	Ratio = []
	Scale = []
	newMatrix =[]

	for i in range (len(Matrix)):

		Scale.append(0)
		firstClmn.append(0)
		Ratio.append(0)
		newMatrix.append(0)

	for x in range (len(Matrix)):

		for i in range (x, len(Matrix)):

			Scale[i] = max(abs(j) for j in Matrix[i])
			firstClmn[i] = Matrix[i][x]
			Ratio[i] = [firstClmn[i] / Scale[i], i]

		#print(Scale)
		srtRat = Ratio
		srtRat.sort(reverse = True)
		print(srtRat)
		for i in range (x, len(Matrix)):
			newMatrix[i] = Matrix[srtRat[i][1]]

		for i in range (len(Matrix)):
			newMatrix[i] = Elim(newMatrix, Sln, x)[0][i]

		Matrix = newMatrix
		print("Matrix: ", Matrix)
		srtRat = [0,0,0,0]

	print(Matrix)
	return(Matrix)

#ScaleGauss(Matrix, Solution)	#Gaussian Elimination with Scaled Partial Pivoting Method (Not Working)
#print(GaussJordan(Matrix, Solution)[1]) #Gauss-Jordan Method
#print(GaussElim(Matrix, Solution)[2])	#Naive Gauss Method
