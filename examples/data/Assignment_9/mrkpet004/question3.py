"""program to check if a complete Sudoku grid is valid or not
peter m muriuki
16/05/14"""

grid=[] #initialize an array to use later
newgrid=[] #initialize an array to use later
for r in range (9):
        values=input("")  #get the input
        grid.append(list(values))  #add the input into the initialised array

for c in range(9):
        nlist=[] 
        for r in range (9):
                nlist.append(grid[r][c]) # switch the rows and columns in grid and append to newgrid
        newgrid.append(nlist)

# check if a value in each row in grid has been repeated
answer=1
for item in grid:
        for o in item:
                if (item.count(o))>1:
                        answer=0
                else:
                        continue
# check if a value in each row in newgrid(column in grid) has been repeated                
answer=1
for item in newgrid:
        for o in item:
                if (item.count(o))>1:
                        answer=0
                else:
                        continue           
# check if a value in each of the 3x3 non-overlapping subgrids has been repeated
for i in range (len(grid)):
        for j in range (len(grid[i])):
                if i<3 and j<3:
                        if (grid[i].count(grid[i][j]))>1:
                                answer=0
                if i<3 and 3<=j<=5:
                        if (grid[i].count(grid[i][j]))>1:
                                answer=0  
                if i<3 and 6<=j<=8:
                        if (grid[i].count(grid[i][j]))>1:
                                answer=0  
                if 3<=i<=5 and j<3:
                        if (grid[i].count(grid[i][j]))>1:
                                answer=0                                  
                if 3<=i<=5 and 3<=j<=5:
                        if (grid[i].count(grid[i][j]))>1:
                                answer=0                                           
                if 3<=i<=5 and 6<=j<=8:
                        if (grid[i].count(grid[i][j]))>1:
                                answer=0  
                if 6<=i<=8 and j<3:
                        if (grid[i].count(grid[i][j]))>1:
                                answer=0                                  
                if 6<=i<=8 and 3<=j<=5:
                        if (grid[i].count(grid[i][j]))>1:
                                answer=0                                           
                if 6<=i<=8 and 6<=j<=8:
                        if (grid[i].count(grid[i][j]))>1:
                                answer=0   
                else:
                        continue
# if final answer is 0 the grid is not valid and if 1 the grid is valid          
if answer ==1:  
        print("Sudoku grid is valid")
else:
        print("Sudoku grid is not valid")
