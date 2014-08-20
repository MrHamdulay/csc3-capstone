#Grant Meeser
#MSRGRA002
#02/05/2014

import util

def condence(row):
	try:
		while row[0]==0: 
			row.pop(0)
	except:
		try:
			while row.index(0):
				row.pop(row.index(0))
		except:
			while len(row)!=4:
				row.append(0)
	try:
		while row.index(0):
			row.pop(row.index(0))
	except:
		while len(row)!=4:
			row.append(0)

	while len(row)!=4:
		row.append(0)
	
		
		
				

def invert(invert,grid):
	for y in range(4):
		for x in range(4):
			invert[x][y]=grid[y][x]

def push_up (grid):
	invgrid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	invert(invgrid,grid)
	for y in range(4):
		condence(invgrid[y])
		for x in range(4):
			if invgrid[y][x]==invgrid[y][x-1] :
				invgrid[y][x]*=2.001
				invgrid[y][x-1]=0
		for x in range(4):
			invgrid[y][x]=round(invgrid[y][x])
	for y in range(4):
		condence(invgrid[y])
	invert(grid,invgrid)
	

def push_down (grid):
	invgrid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	grid.reverse()
	invert(invgrid,grid)
	for y in range(4):
		condence(invgrid[y])
		for x in range(4):
			if invgrid[y][x]==invgrid[y][x-1] :
				invgrid[y][x]*=2.001
				invgrid[y][x-1]=0
		for x in range(4):
			invgrid[y][x]=round(invgrid[y][x])
	for y in range(4):
		condence(invgrid[y])
	invert(grid,invgrid)
	grid.reverse()
	

def push_left (grid):
	for y in range(4):
		condence(grid[y])
		for x in range(4):
			if grid[y][x]==grid[y][x-1] :
				grid[y][x]*=2.001
				grid[y][x-1]=0
		for x in range(4):
			grid[y][x]=round(grid[y][x])
	for y in range(4):
		condence(grid[y])

def push_right (grid):
	for y in range(4):
		grid[y].reverse()
		condence(grid[y])
		for x in range(4):
			if grid[y][x]==grid[y][x-1] :
				grid[y][x]*=2.001
				grid[y][x-1]=0
		for x in range(4):
			grid[y][x]=round(grid[y][x])
	for y in range(4):
		condence(grid[y])
		grid[y].reverse()  


