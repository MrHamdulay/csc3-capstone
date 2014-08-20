#Grant Meeser
#MSRGRA002
#02/05/2014

def create_grid(grid):
	grid.append([0,0,0,0])
	grid.append([0,0,0,0])
	grid.append([0,0,0,0])
	grid.append([0,0,0,0])

def print_grid (grid):
	print('+'+'-'*20+'+')
	for y in range(4):
		print('|',end='')
		for x in range(4):
			if grid[y][x]==0:
				print(' '*5,end='')
			else:
				print(str(grid[y][x])+(' '*(5-len(str(grid[y][x])))),end='')
		print('|')	
	print('+'+'-'*20+'+')    

def check_lost (grid):
	result = True
	#check for copies in y direction
	for y in range(1,3):
		for x in range(4):
			if ((grid[y][x]==grid[y-1][x]) or (grid[y][x]==grid[y+1][x])) or (grid[y][x]==0):
				result=False
	
	#check for copies in x direction
	for y in range(4):
		for x in range(1,3):
			if ((grid[y][x]==grid[y][x-1]) or (grid[y][x]==grid[y][x+1])) or (grid[y][x]==0):
				result=False
	return result

def check_won (grid):
	for y in range(4):
		for x in range(4):
			if grid[y][x]>=32: return True
	return False

def copy_grid (grid):
	copy =[]
	create_grid(copy)
	for y in range(4):
		for x in range(4):
			copy[y][x]=grid[y][x]
	return copy

def grid_equal (grid1, grid2):
	for y in range(4):
		for x in range(4):
			if grid1[y][x]!=grid2[y][x]:
				return False
	return True
