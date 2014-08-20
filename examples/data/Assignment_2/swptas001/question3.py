# Assignment 2 - Question 3
# Tashiv Sewpersad
# 03 - 08 - 2014

# uses
import math

# declarations
def GetDenominator(iNumber):
	if iNumber == 1:
		iResult = 1
		return iResult
	else: 	
		iResult = 0.0
		for i in range(1,(iNumber),1):
			iResult = math.sqrt(2 + iResult)
		return iResult

def GetTerm(iNumber):
  iResult = 2
  iResult = iResult / GetDenominator(iNumber)
  return iResult	

# live code
# Approximating Pi
iCount = 1
Pi = 1
CurrentTerm = GetTerm(iCount)
while CurrentTerm != 1:
  Pi = Pi*CurrentTerm
  iCount += 1
  CurrentTerm = GetTerm(iCount)

# user interfacing
newPi = round(Pi,3)
print("Approximation of pi:",newPi)
iRadius = eval(input("Enter the radius:\n"))
iArea = Pi*((iRadius)**2)
print("Area:",round(iArea,3))
