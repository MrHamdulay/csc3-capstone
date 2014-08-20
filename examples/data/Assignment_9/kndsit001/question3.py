"""Program to check if a complete Sudoku grid is valid or not
Sithasibanzi Kondleka
16 May 2014"""

grid = []
smallergrid = [] #creating empty grids
line = ""

for i in range (9): 
    line = input()
    for j in range(9):
        smallergrid.append(int(line[j])) #putting together the input numbers to the small grid
    grid.append(smallergrid)
    smallergrid = []
    
column = []

for i in range(9):
    smallergrid = []
    for j in range(9):
        smallergrid.append(grid[j][i]) 
    
    column.append(smallergrid)
    
x = "Valid" #checker variable

for i in range(9):
    for j in range(9):
        if grid[i].count(j+1) != 1:
            x = "Invalid" #checking
            break
        if column[i].count(j+1) != 1:
            x = "Invalid" #checking
            break

#checkin the first row        
mylist = []
for i in range(3):
    for j in range(3):
        mylist.append(grid[i][j])

for k in range(9):
    if mylist.count(j+1) != 1:
        x = "Invalid" #checking
        break
    
mylist = []    
for i in range(3):
    for j in range(3, 6):
        mylist.append(grid[i][j])
        
for k in range(9):
    if mylist.count(j+1) != 1:
        x = "Invalid" #checking
        break
    
mylist = []
for i in range(3):
    for j in range(6, 9):
        mylist.append(grid[i][j])

for k in range(9):
    if mylist.count(j+1) != 1:
        x = "Invalid" #checking
        break
    
    
#checking the second row
mylist = []
for i in range(3,6):
    for j in range(3):
        mylist.append(grid[i][j])

for k in range(9):
    if mylist.count(j+1) != 1:
        x = "Invalid" #checking
        break
        
mylist = []    
for i in range(3, 6):
    for j in range(3):
        mylist.append(grid[i][j])
        
for k in range(9):
    if mylist.count(j+1) != 1:
        x = "Invalid" #checking
        break
    
mylist = []
for i in range(3,6):
    for j in range(3):
        mylist.append(grid[i][j])

for k in range(9):
    if mylist.count(j+1) != 1:
        x = "Invalid" #checking
        break

#checking the third row
mylist = []
for i in range(6,9):
    for j in range(3):
        mylist.append(grid[i][j])

for k in range(9):
    if mylist.count(j+1) != 1:
        x = "Invalid" #checking
        break
    
mylist = []    
for i in range(6,9):
    for j in range(3,6):
        mylist.append(grid[i][j])
        
for k in range(9):
    if mylist.count(j+1) != 1:
        x = "Invalid" #checking
        break
    
mylist = []
for i in range(6, 9):
    for j in range(6,9):
        mylist.append(grid[i][j])

for k in range(9):
    if mylist.count(j+1) != 1:
        x = "Invalid" #checking
        break

if x == "Invalid":
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")