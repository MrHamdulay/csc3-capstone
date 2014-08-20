#Shane Horsley
#Program to check whether a sudoku grid is valid or not
#14 May 2014
grid = [] #grid filled by user via input
valid = True #acts as a flag
for i in range(9):
    grid.append(input())

for i in grid: #checking horizontally
    for z in range(1,10):
        if str(z) not in i:
            valid = False
for i in range(9): #check vertically
    downlist=[]
    for j in range(9):
        downlist.append(grid[j][i])
        #print(downlist) #tracing
    for z in range(1,10):
            if str(z) not in downlist:
                valid = False   
for j in range(3,10,3): #check 3x3 sub grids
    teststring=''
    for i in range(3):
        teststring+= grid[i][j-3:j]
    for l in range(1,10):
        if str(l) not in teststring:
            valid = False          
for j in range(3,10,3): #as above
    teststring=''
    for i in range(3,6):
        teststring+= grid[i][j-3:j]
    for l in range(1,10):
        if str(l) not in teststring:
            valid = False
for j in range(3,10,3):
    teststring=''
    for i in range(6,9):
        teststring+= grid[i][j-3:j]
    for l in range(1,10):
        if str(l) not in teststring:
            valid = False 
           
if valid== True: #never changes to false
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")

