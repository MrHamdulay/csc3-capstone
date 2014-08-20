#Jason Smythe
#CSC 1015
#SMYJAS002
#assignment 9
#question 3

#tests if a number appears more than once in a given row and returns true if each number 1 - 9 appears only once
def checkRows(grid):
	for i in range(9):
		for k in range(1,10):
			if grid[i].count(k) != 1:
				return False
	return True

#tests if a number appears more than once in a given column and returns true if each number 1 - 9 appears only once
def checkCols(grid):
	for i in range(9):
		#this creates a new list of elements that in the same column
		test = []
		for j in range(9):
			test.append( grid[j][i] )
		##print(test, "\n")
		for k in range(1,10):
			if test.count(k) != 1:
				return False
	return True

#tests if a number appears more than once in a given 3*3 square and returns true if each number 1 - 9 appears only once
def checkSquares(grid):
	#the 3*a and 3*b represent the top left hand corner of each of these elemntes
	for a in range(3):
		for b in range(3):
			#this creates a new list of elements that in the 3*3 square
			test = []
			for i in range(3*a, 3*a + 3):
				
				for j in range(3*b, 3*b + 3):
					test.append( grid[i][j] )
			##print(test, "\n")
			for k in range(1,10):
				if test.count(k) != 1:
					return False
	return True

#checks all the above criteria in one easily callable function
def checkAll(grid):
	return checkRows(grid) and checkCols(grid) and checkSquares(grid)



def main():
	grid = []
	#this creates the 2D array of the sudoku grid
	for i in range(9):
		row = input("")
		grid.append([int(x) for x in row])
	if checkAll(grid):
		print("Sudoku grid is valid")
	else:
		print("Sudoku grid is not valid")
		
main()

'''
grid = [[2,5,9,7,1,6,4,8,3],
		[8,6,7,3,4,5,9,1,2],
		[4,1,3,9,2,8,6,7,5],
		[3,9,8,5,7,4,1,2,6],
		[5,4,6,2,8,1,7,3,9],
		[1,7,2,6,3,9,5,4,8],
		[9,8,4,1,6,3,2,5,7],
		[6,2,1,8,5,7,3,9,4],
		[7,3,5,4,9,2,8,6,1]]	
'''	
""" Sample I/O:

359716482
867345912
413928675
398574126
546281739
172639548
984163257
621857394
735492861
Sudoku grid is not valid

Sample I/O:

259716483
867345912
413928675
398574126
546281739
172639548
984163257
621857394
735492861
Sudoku grid is valid
 Sample I/O:

Enter a message:
hello world
Encrypted message:
ifmmp xpsme
"""
