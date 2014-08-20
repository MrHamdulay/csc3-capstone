'''Program part of a game to push/add numbers together in a certain way
Matthew Bandama
BNDTAT003
01-May-2014'''

from util import print_grid

def remove_zeros(grid,choice):
	'''Function that removes zeros from lsit and returns on without 
	the zeros'''
	
	new_grid = []
	if choice == 'row':
		
		for i in range(4):
			list=[]
			for j in range(4):
			
				if grid[i][j] > 0:
					list.append(grid[i][j])
			new_grid.append(list)
	
		return(new_grid)
	
	elif choice == 'col':
		
		for z in range(4):
			list2 = []
			for x in range(4):
				
				if grid[x][z]>0:
					list2.append(grid[x][z])
			new_grid.append(list2)
		return(new_grid)

def make_len_four(grid,choice):
	'''Make the lists inside grid = length of 4 so i can work 
	uniformly with all the lists later'''
	for i in grid:
		
		if len(i)<4:
			
			for j in range(4-len(i)):
				
				if choice == 'append':
					i.append(0)
				
				elif choice == 'insert':
					i.insert(0,0)
	return(grid)


def add_list(grid,choice):
	'''Add lists respective numbers in a list'''
	
	if choice == 'left':
		
		for i in range(4):
			
			for j in range(3):
				
				if grid[i][j] == grid[i][j+1]:
					grid[i][j] = (grid[i][j])*2
					grid[i][j+1] = 0
					
		return(grid)

	elif choice == 'right':
		
		for z in range(3,-1,-1):
			
			for x in range(3,0,-1):
				
				if grid[z][x] == grid[z][x-1] and grid[z][x] != 0:
					grid[z][x] = (grid[z][x])*2
					grid[z][x-1] = 0
		return(grid)


def fix_list(grid):
	'''For the lists that i swaped the rows and columns so i coukd use the same function for both
	cases, but need to return original orientation'''
	my_list = []
	
	for i in range(4):
		list = []
		for j in range(4):
			list.append(grid[j][i])
		my_list.append(list)
	return(my_list)


# Now that i have all the functions i need i just need to 
# execute them in a way that gets me the required results

# Insert goes with right
# Append goes with left
# down = 'right'
# up = 'left'
# col is for up or down


def push_up(grid):
	
	grid_1 = remove_zeros(grid,'col')
	grid_2 = make_len_four(grid_1,'append')
	grid_3 = add_list(grid_2,'left')
	grid_4 = fix_list(grid_3)
	return(grid_4)

def push_down(grid):
	
	grid_1 = remove_zeros(grid,'col')
	grid_2 = make_len_four(grid_1,'insert')
	grid_3 = add_list(grid_2,'right')
	grid_4 = fix_list(grid_3)
	return(grid_4)


def push_left(grid):
	
	grid_1 = remove_zeros(grid,'row')
	grid_2 = make_len_four(grid_1,'append')
	grid_3 = add_list(grid_2,'left')
	grid_4 = remove_zeros(grid_3,'row')
	grid_5 = make_len_four(grid_4,'append')
	return(grid_5)

def push_right(grid):
	
	grid_1 = remove_zeros(grid,'row')
	grid_2 = make_len_four(grid_1,'insert')
	grid_3 = add_list(grid_2,'right')
	grid_4 = remove_zeros(grid_3,'row')
	grid_5 = make_len_four(grid_4,'insert')
	return(grid_5)

