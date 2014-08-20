"""check if a complete Sudoku grid is valid or not
Lauren Denny
11 May 2014"""

#create 9x9 grid
grid=[]
for i in range(9):
    grid.append([0]*9)

#populate grid with 81 inputted values
for i in range(9):
    row=input() #get row of inputted values 9 times
    for j in range(9):
        grid[i][j]=eval(row[j]) #change string value to an integer

def check_row(grid):
    """return True if 2 numbers in any row are the same, otherwise return False"""
    for i in range(9):
        for j in range(9):
            if grid[i].count(j+1)>1: #if there is more than 1 of a number from 1-9 in a row, return True
                return True
    else:
        return False
    
def check_col(grid):
    """return True if 2 numbers in any column are the same, otherwise return False"""
    new_grid=[]
    for i in range(9):
        new_grid.append([0]*9)   #create new 9x9 grid 
    for i in range(9):
        for j in range(9):
            new_grid[i][j]=grid[j][i] #swop rows and columns of grid
    return check_row(new_grid) #check if there 2 of any number in any of the new rows i.e. old columns

def check_condition(grid,condition):
    """return True if a number occurs more than once in 1 of the 9 specified (condition) 3x3 grids in the sudoku, otherwise return False"""
    sub_grid=[]
    for i in range(9):
        for j in range(9):
            if eval(condition): #if the condition regarding i and j holds, add grid[i][j] to the new sub_grid list
                sub_grid.append(grid[i][j])
    for k in range(9): #if a number occurs more than once in the sub_grid, return True
        if sub_grid.count(k+1)>1:
            return True  
    else:
        return False
    
def check_3x3(grid):
    """return True if any of the 3x3 grids contains a number that occurs more than once"""
    conditions=["i//3==0 and j//3==0","i//3==0 and j//3==1","i//3==0 and j//3==2","i//3==1 and j//3==0","i//3==1 and j//3==1","i//3==1 and j//3==2","i//3==2 and j//3==0","i//3==2 and j//3==1","i//3==2 and j//3==2"] #list of conditions corresponding to the 9 3x3 grids in a sudoku
    for condition in conditions:    
        if check_condition(grid,condition)==True:
            return True #if any of the 3x3 grids has a value that occurs more than once, return true
    else:
        return False  

if check_row(grid)==False and check_col(grid)==False and check_3x3(grid)==False: #if there are no repeated values in any of the rows, columns or 3x3 grids, the grid is valid
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")

    