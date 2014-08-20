# Anna Borysova
# ass7,q2
# 2014-05-01

def create_grid(grid):
	for i in range(4):
		grid.append([0,0,0,0])

def print_grid(grid):
	print("+--------------------+")
	for i in range(len(grid)):
		print("|", end="")
		for j in range(len(grid[i])):
			if grid[i][j] == 0:
				print("{: <5}".format(" "),end="")
			else:
				print("{: <5}".format(grid[i][j]),sep="",end="")
		print("|")
	print("+--------------------+")

def check_lost(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == 0:
				return False

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if i != 3 and grid[i][j] == grid[i+1][j]:
				return False
			elif i != 0 and grid[i][j] == grid[i-1][j]:
				return False
			elif j != 3 and grid[i][j] == grid[i][j+1]:
				return False
			elif j != 0 and grid[i][j] == grid[i][j-1]:
				return False
	return True

def check_won(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] >= 32:
				return True
	return False

def copy_grid(grid):
	copy_grid = []
	for i in range(len(grid)):
		copy_grid.append(grid[i][:])
	return copy_grid

def grid_equal(grid1, grid2):
	if grid1 == grid2:
		return True
	else:
		return False
	
