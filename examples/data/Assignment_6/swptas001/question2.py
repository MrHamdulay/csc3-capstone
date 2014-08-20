### Tashiv Sewpersad (SWPTAS001)
### Assignment 6 - Question 2
### 2014 - 04 - 20

## Uses
import math

## Declaration
def AddVectors(Vector1, Vector2):
	__doc__ = "A function that adds two vectors and returns the result"
	VectorResult = []
	iLen = len(Vector1) #assumes the vectors are of equal length
	for i in range(iLen):
		iResult = Vector1[i] + Vector2[i]
		VectorResult.append(iResult)
	return VectorResult	

def DotVectors(Vector1, Vector2):
	__doc__ = "A function that returns the dot product of two vectors"
	DotResult = 0
	iLen = len(Vector1) #assumes the vectors are of equal length
	for i in range(iLen):
		iResult = Vector1[i] * Vector2[i]
		DotResult += iResult 
	return DotResult
	
def Normalise(Vector):
	__doc__ = "A function that returns the value of a normalised vector"
	Result = 0
	for i in Vector:
		Result += i**2
	FinalResult = math.sqrt(Result)
	return FinalResult

def ExtractVector(StrVals):
	__doc__ = "A function that outputs a vector in list form"
	result = []
	for i in StrVals:
		iPoint = int(i)
		result.append(iPoint)
	return result	

## Live Code
# Get Input
Output = "{0:.2F}" # normalised vector output formatting
# Get input
VectorA = ExtractVector(input("Enter vector A:\n").split())
VectorB = ExtractVector(input("Enter vector B:\n").split())
# print output
print("A+B =",AddVectors(VectorA,VectorB))
print("A.B =",DotVectors(VectorA,VectorB))
print("|A| =",Output.format(Normalise(VectorA)))
print("|B| =",Output.format(Normalise(VectorB)))
