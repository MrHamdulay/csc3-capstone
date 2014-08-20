#Program to check if a complete Sudoku grid is valid or not
#13 May 2014
#Kiran Desraj


#create empty grids to store values

grid = [ ]
for i in range(9):
    grid.append(input())
empty = [ ]

for i in range(9):
    
    empty.append(grid[i][0:3])
    
for i in range(9):
    
    empty.append(grid[i][3:6])
    
for i in range(9):
    
    empty.append(grid[i][6:9])
    
x=0

while( x < (len(empty)-0)):
    empty[x]=empty[x]+empty[x+(0+1)]+empty[x+(0+2)]
    empty.remove(empty[x+(0+1)])
    empty.remove(empty[x+(0+1)])
    x+=1


sudoku_box = [[],[],[],[],[],[],[],[],[]]


#search columns, rows, and boxes for repetition
sudoku = ''


for i in range(9):
    for j in range(9):
        sudoku_box[i].append(grid[j][i])
        
for i in range(9):
    for j in range(9):
        if empty[i].index(empty[i][j])!=j:
            sudoku = 'bad'
            
            
for i in range(9):
    for j in range(9):
        if sudoku_box[i].index(sudoku_box[i][j])!=j:
            sudoku = 'bad'

for i in range(9):
    for j in range(9):
        if grid[i].index(grid[i][j])!=j:
            sudoku = 'bad'
            
      

if sudoku == 'bad':
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")