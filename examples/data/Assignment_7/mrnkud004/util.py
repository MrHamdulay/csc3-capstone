"""Utility Class for 2048 Grid
Kennedy Muranda
1 May 2014"""

#create a 4x4 grid
def create_grid(grid):
    
    for i in range(4):
        grid.append([0]*4)

#print out a 4x4 grid in 5-width columns within a box
def print_grid (grid):
    print("+--------------------+")
    for i in range (4):#Loop through array (each line of box)
        print("|",end="")
        for x in grid[i]:#Go through the current line and print the appropriate character
            if x != 0:
                print(str(x)+(5-len(str(x)))*" ",end="")
            else :
                print("     ",end="")
        print("|")
    print("+--------------------+")
        
    
    

#return True if there are no 0 values and no adjacent values that are equal; otherwise False
def check_lost (grid):
    
    for i in range(4):#Go through every value in the array
        for j in range(4):
            if(grid[i][j]==0):#If value is 0 return false 
                return False
            elif i==3 and j==3:#If its the bottom corner we are done
                return True
            elif i==3:
                if((grid[i][j]==grid[i][j+1])):#if last column then only check below
                    return False
            elif j==3:
                if(grid[i][j]==grid[i+1][j]):#if last row only check right
                    return False
                
            elif(grid[i][j]==grid[i+1][j] or grid[i][j]==grid[i][j+1]):#if in 3x3 array top left corner then check right and down
                return False
    

#return True if a value>=32 is found in the grid; otherwise False
def check_won (grid):
    
    for i in grid:#Go through each column
        for j in i:#Through each row
            if j>=32:#check if value is greater or equal to 32
                return True
    return False
            
        
#return a copy of the grid
def copy_grid (grid):
    
    gridCop=[]#Create empty grid
    for i in range (4):
        appendage=[]#Go through given grid and copy each individual value into the corresponding point in copy
        for j in range(4):
            appendage.append(grid[i][j])
        gridCop.append(appendage)
    return gridCop
    

#check if 2 grids are equal - return boolean value
def grid_equal (grid1, grid2):
    
    for i in range (4):#Go through given grids and check each point to make sure they are the same, if not return false
            for j in range(4):
                if(grid1[i][j]!=grid2[i][j]):
                    return False
    return True
          