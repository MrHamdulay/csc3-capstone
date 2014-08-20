"""program of functions
vuyolwethu nkosi
30 april 2014"""

#create a 4x4 grid
def create_grid(grid):
    ht=4
    for j in range(ht):
        grid.append([0]*4)

#print out a 4x4 grid in 5-width columns within a box
def print_grid(grid):
    print("+","-"*20,"+",sep="") #frame of box
    ht=4
    for j in range(ht):
        grid.append([0]*4) #fill space with zeros
    for row in range(ht):
        print("|",end="") #printing | of frame of box
        for column in range(ht):
            if grid[row][column]==0: #if grid space is a zero
                print(" ".ljust(5),end="") #print a space
            else:
                print(str((grid[row][column])).ljust(5),end="") #or else print the value inputted
        print("|",end="") #print | of frame of box
        print()
    
    print("+","-"*20,"+",sep="") #frame of box

#return True if there are no 0 values and no adjacent values which are equal, else False
def check_lost(grid):
    #print(grid)
    for row in range(4):
        for column in range(4):
            if grid[row][column]==0: #if there is a space in the grid, can still carry on playing
                return False
            else:
                if row-1 >= 0: #check boundary values, if they are valid
                    if grid[row-1][column]==grid[row][column]: #if number above is the same as the number in current position, can still carry on playing
                        return False
                if row+1<=3: #check boundary values
                    if grid[row+1][column]==grid[row][column]: #if number below is the same as the number in current position, can still carry on playing 
                        return False
                if column-1>=0: #check boundary values
                    if grid[row][column-1]==grid[row][column]: #if number to the left is the same as the number in current position, can still carry on playing
                        return False
                if column+1<=3: #check boundary values
                    if grid[row][column+1]==grid[row][column]: #if number to the right is the same as the number in current position, can still carry on playing
                        return False
    return True #if all conditions are met, then you have lost

#return True if a value>=32 is found in the grid, otherwise False
def check_won(grid):
    #print(grid)
    for row in range(4):
        for column in range(4):
            if grid[row][column]>=32: #if a value in the grid is >=32, the person has won
                return True
    return False #should always check every value in grid before concluding

#return a copy of the grid
def copy_grid(grid):
    grid_2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #make grid with temporary values
    for row in range(4):
        for column in range(4):
            grid_2[row][column] = grid[row][column] #every value which is in the current grid should be changed to correspond to what it should be as according to grid given
    return grid_2 #grid is now a copy of the first grid

#check if 2 grids are equal- return boolean value
def grid_equal(grid1,grid2):
    if grid1==grid2:
        return True
    else:
        return False
            
    
    

                