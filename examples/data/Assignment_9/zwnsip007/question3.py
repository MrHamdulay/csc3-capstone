'''Siphesihle Zwane 
Soduko Checker
16/05/14'''
grid=[]
for create in range (9):
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0]) # creating grid

i = 0
while i != 9:
    line = input()
    
    for j in range(0, 9):
        grid[i][j] = line[j: j+1]
        
    i += 1
        
valid = True
#checking rows and columns 
for i in range(9):      
    for j in range(9):
        for k in range(j+1, 9):
            if grid[i][j] == grid[i][k]:
                valid = False
  

for i in range(9):
    for j in range(9):
        for k in range(j+1, 9):
            if grid[j][i] == grid[k][i]:
                valid = False

#breaking into smaller grids and checking 
sgrid=[]
for s in range(3):            
    sgrid.append([0, 0, 0]) 

for l in range(3):
    for k in range(3):
        for i in range(3):
            for j in range(3):
                sgrid[i][j] = grid[i+l*3][j+k*3]
       
        for r in range(3):
            if sgrid[0][r] in sgrid[1] or sgrid[0][r] in sgrid[2] or sgrid[2][r] in sgrid[1]:
                valid = False

if valid:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
                
