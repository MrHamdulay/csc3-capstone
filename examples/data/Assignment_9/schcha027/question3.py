#CHARLES SCHLEICH
#SCHCHA027
grid=[]
for i in range(9):
    inGrid=input("")
    tempgrid=[]
    for j in inGrid:
        tempgrid.append(eval(j))
    grid.append(tempgrid)


#checks the rows for equal numbers
def row_check(grid):
    for i in range(9):
        for j in range(9):
            for k in range(j+1, 9-j):
                if grid[i][j]==grid[i][k]:
                    return False
    return True

#checks the collums for equal numbers
def col_check(grid):
    for i in range(9):
        for j in range(9):
            for k in range(i+1, 9-i):
                if grid[i][j]==grid[k][j]:
                    return False
    return True
#checks the smaller 3 by 3 grids for equal numbers

def check_3by3(grid):
    for i in range(3):
        for p in range(3):
            subgrid1=[grid[i*3][p*3],grid[i*3][(p*3)+1],grid[i*3][(p*3)+2],    grid[(i*3)+1][(p*3)],grid[(i*3)+1][(p*3)+1],grid[(i*3)+1][(p*3)+2]  , grid[(i*3)+2][(p*3)], grid[(i*3)+2][(p*3)+1],grid[(i*3)+2][(p*3)+2]]
            
            for j in range(9):
                for k in range(j+1,9):
                    if subgrid1[j]==subgrid1[k]:
                        return False
    return True

#checks controller
if row_check(grid)==False:
    print("Sudoku grid is not valid")
elif col_check(grid)==False:
    print("Sudoku grid is not valid")
elif check_3by3(grid)==False:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")