### Tashiv Sewpersad (SWPTAS001)
### CSC1015F - Assignment 9 - Q3
### 11 / 05 /2014

## Declarations
def isValid(aLine):
	'''A function for determining if a sudoku set of numbers are valid'''
	for val in range(1,10):
		try:				# index is efficient method as it stops when it finds a match
			Line.index(val) # Checks for each number ...
		except:				# by logic since there are only 9 numbers
			return True		# if any number is missing it can be assumed
	return False			# that there is a double/triple/... of another number in the set 

## Live Code
Grid = []
bFault = False
# input
for i in range(9):
	Line = []
	for Number in input().strip():
		Line.append(int(Number))
	Grid.append(Line)

# Row Check - Special Loading Method
for row in range(9):
	if bFault == True:
		break
	bFault = isValid(Grid[row])

# Column Checking - Special Loading Method
for Column in range(9):
	if bFault == True: # for effeciency
		break
	Line = [] 
	for Row in range(9): # special column style loading
		Line.append(Grid[Row][Column])
	bFault = isValid(Line)

# 3x3 sub-grid test - Special Loading Method
for y in range(3):
	if bFault == True: # iteration for main grid in 3's vertically
		break
	for x in range(3): # iteration for main grid in 3's horizontally
		Line = []
		for row in range(3): # iteration for sub-grid vertically
			for col in range(3): # iteration for sub-grid horizontally
				Line.append(Grid[y*3+row][x*3+col]) # Builds line set for validity testing
	bFault = isValid(Line)
	
# The result
if bFault == True:
	print("Sudoku grid is not valid")
else:
	print("Sudoku grid is valid")	
