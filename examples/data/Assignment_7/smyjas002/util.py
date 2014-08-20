#Jason Smythe
#CSC 1015
#SMYJAS002
#assignment 7
#question 2

def create_grid(grid):
	for i in range(4):
		grid.append([0,0,0,0])

def print_grid (grid):
	gridString = "+--------------------+\n"
	for i in range(4):
		gridString += "|"
		for j in range(4):
			value = str(grid[i][j])
			if value != "0":
				gridString += value
				gridString += " "*(5-len(value))
			else:
				gridString += " "*5
		gridString += "|\n"
	gridString += "+--------------------+"
	print(gridString)

def check_lost (grid):
	for i in range(3):
		if 0 in grid[i]:
			return False
		for j in range(3):
			value = grid[i][j]
			if value == grid[i][j+1]:
				return False
			if value == grid[i+1][j]:
				return False
	if 0 in grid[-1]:
		return False
	return True
	
def check_won (grid):
	for i in range(4):
		for j in range(4):
			if grid[i][j] >= 32:
				return True
	return False

def copy_grid (grid):
	newGrid = []
	create_grid(newGrid)
	for i in range(4):
		for j in range(4):
			newGrid[i][j] = grid[i][j]
	return newGrid
    
def grid_equal (grid1, grid2):
	for i in range(4):
		for j in range(4):
			if grid1[i][j] != grid2[i][j]:
				return False
	return True

"""
 Write a module of utility functions (called util.py) to manipulate 2-dimensional arrays of size 4x4.  
 These functions will be used in Question 3.

Use the question2.py test program to test your functions.  
This program takes a single integer input value and runs the corresponding test on your module.  
This is a variant of unit testing, where test cases are written in the form of a program that tests your program.  
You will learn more about unit testing in future CS courses.

Sample I/O:

2
+--------------------+
|2         2         |
|     4         8    |
|     16        128  |
|2    2    2    2    |
+--------------------+

Sample I/O:

7
True

Sample I/O:

9
True

Sample I/O:

17
4 4
16 16
2 2
64 4
64 16
64 2

Sample I/O:

18
True
"""
