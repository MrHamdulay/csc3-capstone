'''Program to manipulate 2-dimensional arrays
Matthew Bandma
BNDTAT003
28-April-2014'''

def create_grid(grid):
	''' create a 4 by 4 grid'''
	
	for i in range(4):
		grid.append([0]*4)
	return(grid)



def print_grid(grid):
	
	print('+--------------------+')
	for i in range(4):
		print('|',end='')
		for j in range(4):
			if grid[i][j] == 0: 
				print('{0:<5}'.format(' '),end='')
			else:
				print('{0:<5}'.format(grid[i][j]),end='')
			
		print('|',end='')
		print()
	print('+--------------------+')


def check_lost(grid):
	
	for d in range(4):
		
		for a in range(4):
			
			if grid[d][a] == 0:
				return(False)
			
			if a>0:
				if grid[d][a] == grid[d][a-1]:
					return(False)
			
			if d>0:
				if grid[d][a] == grid[d-1][a]:
					return(False)
	return(True)


def check_won(grid):
	
	for d in range(4):
		
		for a in range(4):
			
			if grid[d][a] >= 32:
				return(True)
	return(False)

def copy_grid(grid):
	
	new_grid = []
	for i in range(4):
		small_grid = []
		for j in range(4):
			small_grid.append(grid[i][j])
		new_grid.append(small_grid)
	
	return(new_grid)

def grid_equal(grid1,grid2):
	
	for i in range(4):
		
		for j in range(4):
			
			if grid1[i][j] != grid2[i][j]:
				return(False)
		
	return(True)  

