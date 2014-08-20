#MSRGRA002
#Grant Meeser	
#15/05/2014

def checkRow(grid):
	for y in range(9):
		for x in range(9):
			for i in range(x+1,9-x):
				if grid[y][x]==grid[y][i] and x != i:
					return False
					
	return True


def checkCol(grid):
	for y in range(9):
		for x in range(9):
			for i in range(x+1,9-x):
				if grid[x][y]==grid[i][y] and x != i:
					return False
					
	return True


def checkSqr(grid):
	for a in range(0,7,3):
			for b in range(0,7,3):
				for y in range(a,3+a):
					for x in range(b,3+b):
						for j in range(a,3+a):
							for i in range(b,3+b):
								if grid[x][y]==grid[i][j] and j!=x and i!=x:
									return False
					
	return True
	
	


grid=[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]]
inputString=''
for i in range(9):
	inputString+=input()
for y in range(9):
	for x in range(9):
		grid[y][x]=inputString[0]
		inputString=inputString[1::]
		

if checkRow(grid) and checkCol(grid) and checkSqr(grid):
	print('Sudoku grid is valid')
else:
	print('Sudoku grid is not valid')

#print(checkRow(grid))
#print(checkCol(grid))
#print(checkSqr(grid))


