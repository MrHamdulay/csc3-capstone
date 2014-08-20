'''Program for sudoku
Julian Albert
16-05-2014'''

#column check
def Column(grid):
	for y in range(9): #range of 9x9
		for x in range(9): #range of 9x9
			for i in range(x+1,9-x):
				if grid[x][y] == grid[i][y] and x != i:
					return False
					
	return True
#row check
def Row(grid):
	for y in range(9): #range of 9x9
		for x in range(9): #range of 9x9
			for i in range(x+1,9-x):
				if grid[y][x] == grid[y][i] and x != i:
					return False
					
	return True
#block check
def Block(grid):
	for a in range(0,7,3):
			for b in range(0,7,3):
				for y in range(a,3+a):
					for x in range(b,3+b):
						for j in range(a,3+a):
							for i in range(b,3+b):
								if grid[x][y] == grid[i][j] and j!=x and i!=x:
									return False
					
	return True
	

grid=[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]]
input_value=''

for i in range(9):
	input_value += input()
for y in range(9):
	for x in range(9):
		grid[y][x] = input_value[0]
		input_value = input_value[1::]
		

if Column(grid) and Row(grid) and Block(grid): 
	print('Sudoku grid is valid')
else:
	print('Sudoku grid is not valid')




