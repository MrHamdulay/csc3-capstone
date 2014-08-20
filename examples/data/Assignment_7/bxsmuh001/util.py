#Assignment 7, Question 2
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Created: 28/05/2014; [Date Modified: 29/05/2014(Some more functions added); 30/04/2014(Completed); 01/05/2014(Addition of comments)]

#Creates a 4x4 grid.
def create_grid(grid):
    updatedGrid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]    
    if(grid == []):
            grid.extend(updatedGrid)
    return(grid)        

#Prints the grid with each element of a row having column width of 5.
def print_grid(grid):
    frame = "+--------------------+"    
    print(frame)    
    for i in range(len(grid)):
        print("|",end="")
        for j in range (len(grid[i])):  
            if(grid[i][j] != 0):
                print ("{:<5}".format(grid[i][j]), sep="",end ="") #Giving width of 5.
            else:
                print ("{:<5}".format(""), sep="",end ="")
        print("|")
    print(frame)

#Checking if user lost.
def check_lost(grid):    
    #This inner function checks for the boundary values and returns true or false accordingly.
    def checkRange(x,y):
        if x < 0 or x >= len(grid): return False
        if y < 0 or y >= len(grid): return False
        return True
    
    #Checks if user lost. return True if there are no 0 values and no adjacent values that are equal; otherwise False
    def checkLost(grid):
        b = False
        a = True
        for i in range(len(grid)):
            for j in range(len(grid)):
                value = grid[j][i]
                if checkRange(i+1,j) and grid[j][i+1] == value: a =  False
                if checkRange(i-1,j) and grid[j][i-1] == value: a =  False
                if checkRange(i,j+1) and grid[j+1][i] == value: a =  False
                if checkRange(i,j-1) and grid[j-1][i] == value: a =  False
        for i in range(len(grid)):
            for j in range(len(grid)):
                if(grid[i][j] == 0): b = True
        if(a == True and b == False ):
            return True  
        else:
            return False
    return checkLost(grid)
    
#Check if user won. return True if a value>=32 is found in the grid; otherwise False
def check_won(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] >=32):
                return True
    return False

#Copies the grid.
def copy_grid (grid):
    gridCopy = []
    for row in range(len(grid)):
        gridRowCopy = grid[row][:] #Slices a row to create a shallow copy.
        gridCopy.append(gridRowCopy) #Appends the row to the gridCopy.
    return(gridCopy)

#Checks if 2 grids are equal
def grid_equal (grid1, grid2):
    if (grid1 == grid2):
        return True
    return False

    
       



    
