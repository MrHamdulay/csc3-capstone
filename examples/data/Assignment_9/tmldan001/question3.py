'''program to check if a complete Sudoku grid is valid or not.
Daniel M. Tamale
TMLDAN001
2014-05-16'''

'''i and j are Sudoku rows and columns respectively'''  
step=[]
for i in range(9):
    step.append([])
    list=input('')
    for j in range(9):
        step[-1].append(int(list[j:j+1]))

'''Boolean value for validity of grid'''        
valid=True
for i in range(9):
    grid=[0]*9
    for j in range(9):
        grid[step[i][j]-1]=1
    for k in range(9):
        if grid[k]==0:
            valid=False
            
for j in range(9):
    grid=[0]*9
    for i in range(9):
        grid[step[i][j]-1]=1
    for k in range(9):
        if grid[k]==0:
            valid=False

'''variables row and col for larger Sudoku rows and columns respectively'''            
for row in range(0,9,3):
    for col in range(0,9,3):
        grid=[0]*9
        for i in range(3):
            for j in range(3):
                grid[step[i+row][j+col]-1]=1
        for k in range(9):
            if grid[k]==0:
                valid=False
                    
if valid:
    print('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')