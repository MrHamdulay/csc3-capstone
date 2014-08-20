"""prgramme to be tested in question2
rama raphalalani
29-04-2014"""


#create a 4x4 grid
def create_grid(grid):
    height=4
    for j in range(height):
        grid.append([0]*4)

#print out a 4x4 grid in 5-width columns within a box
def print_grid(grid):
    print("+","-"*20,"+",sep="") 
    height=4
    for j in range(height):
        grid.append([0]*4) 
    for row in range(height):
        print("|",end="") 
        for column in range(height):
            if grid[row][column]==0: 
                print(" ".ljust(5),end="") 
            else:
                print(str((grid[row][column])).ljust(5),end="") 
        print("|",end="") 
        print()
    
    print("+","-"*20,"+",sep="") 

#return True if there are no 0 values and no adjacent values which are equal, else False
def check_lost(grid):
    #print(grid)
    for row in range(4):
        for column in range(4):
            if grid[row][column]==0: #if there is a space in the grid, can still carry on playing
                return False
            else:
                if row-1 >= 0: 
                    if grid[row-1][column]==grid[row][column]: 
                        return False
                if row+1<=3: 
                    if grid[row+1][column]==grid[row][column]:  
                        return False
                if column-1>=0:
                    if grid[row][column-1]==grid[row][column]: 
                        return False
                if column+1<=3: 
                    if grid[row][column+1]==grid[row][column]: 
                        return False
    return True #if all conditions are met, then you have lost

#return True if a value>=32 is found in the grid, otherwise False
def check_won(grid):
    #print(grid)
    for row in range(4):
        for column in range(4):
            if grid[row][column]>=32: 
                return True
    return False 


#return a copy of the grid
def copy_grid(grid):
    gridNew=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #make grid with temporary values
    for row in range(4):
        for column in range(4):
            gridNew[row][column] = grid[row][column] #every value which is in the current grid should be changed to correspond to what it should be as according to grid given
    return gridNew #grid is now a copy of the first grid

#check if 2 grids are equal- return boolean value
def grid_equal(grid1,grid2):
    if grid1==grid2:
        return True
    else:
        return False
            
    
    

                