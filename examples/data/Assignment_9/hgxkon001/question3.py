#Konrad Hugo
#Assignment 9 question 3




def horizontal(sudoku):
	for y in range(9): #checks for sudoku correctness in row
		for x in range(9): 
			for i in range(x+1,9-x):
				if sudoku[y][x] == sudoku[y][i] and x != i:
					return False
					
	return True


def vertical(sudoku): #checks for sudoku correctness in column
	for y in range(9): 
		for x in range(9):
			for i in range(x+1,9-x):
				if sudoku[x][y] == sudoku[i][y] and x != i:
					return False
					
	return True

def threebythree(sudoku): #checks for sudoku correctness within 3x3s
	for a in range(0,7,3):
			for b in range(0,7,3):
				for y in range(a,3+a):
					for x in range(b,3+b):
						for l in range(a,3+a):
							for k in range(b,3+b):
								if sudoku[x][y] == sudoku[k][l] and l!=x and k!=x:
									return False
					
	return True
	
#Actual grid
sudoku=[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]]


insert=''

for i in range(9):
	insert += input()
for y in range(9):
	for x in range(9):
		sudoku[y][x] = insert[0]
		insert = insert[1:]
		

if horizontal(sudoku) and vertical(sudoku) and threebythree(sudoku): 
	print('Sudoku grid is valid') #if all three conditions are true
else:
	print('Sudoku grid is not valid')





    
        

        
        
        
        
        
    
    

    




