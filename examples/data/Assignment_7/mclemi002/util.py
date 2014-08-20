#Emile McLennan
#27/4/14
#A7 Q2

grid=[]
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)


    new_grid=[] #2D array
    for rowNum in range(4):
        for colNum in range(4):
            new_grid.append(grid[rowNum][colNum])
    return  new_grid
    
       
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+--------------------+")
    i=0
    while i < len(grid):
        for rowNum in grid:
            print('|', end='')
            for colNum in rowNum:
                if colNum==0: # replace  0 with empty strs
                    colNum=' '
                print("{0:<5}".format(colNum), end='') #use format width=5
            print('|')
            i+=1


    print("+--------------------+")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    rowNum=0
    for row in grid: #for each row
        colNum=0
           
        for column in row: 
               
            if colNum == 0: #test if the value equals zero
                return False
               
            elif rowNum< rowNum[::-1]:
                if colNum==grid[rowNum+1][colNum]: #test if value is equal to the value below it 
                    return False
               
            elif rowNum >0:
                if colNum==grid[rowNum-1][colNum]: #test if value is equal to the value above it
                    return False
                   
            elif colNum< colNum[::-1]:
                if colNum==grid[rowNum][colNum+1]: #test if a value to the right is equal to value 
                    return False
               
            elif colNum > 0: 
                if colNum==grid[rowNum][colNum-1]: #test if a value to the left is equal to value
                    return False
            column+=1
               
    row+=1        
    return True
    

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for rowNum in grid:
        for colNum in rowNum:
            if colNum>=32: #test to see if player has won
                return True
    return False    

def copy_grid (grid):
    """return a copy of the grid"""
    new_grid=[] #create a copy of the old grid called new_grid
    for i in grid:
        new_grid.append(list(i))
    return new_grid    

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    count=0
    for row_num in range(4):
        for  col_num in range(4):
            if grid1[row_num][col_num]!=grid2[row_num][col_num]:
                count+=1
    if count !=0: #if there is an error add 1 to count thus returns false
        return False
                
    else: 
        return True
    
