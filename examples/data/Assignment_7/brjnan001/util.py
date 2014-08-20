"""Manipulating 2D arrays of sizw 4x4
Nandani Birjanund
assignment 7 Q2, game 2048"""

height = 4

def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (height): #creates an empty grid
        grid.append([0]*4) #adds on
    return grid
    
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    width = 5          #creates and populates the grid
    print("+","-"*20,"+",sep="")# at the top of grid
       
    for row in range (height):
        print("|",end="")       #side of the grid
        for col in range (height):
            
            row_x = len(str(grid[row][col]))#getting length of row
            x = int(row_x)     
               
            if "0" in str(grid[row][col]):#print "    " if 0      
                print("     ",end="") 
            else:
                print (grid[row][col],end=(" "*(width-x))) #to get correct spacing use width-length calculated
        print("|")     #side of the grid
    print("+","-"*20,"+",sep="")#bottom of the grid    
       

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    flag = True       
    for col in range (3):       #checking column and rows for 0 and equal values (to replace)
        for row in range (4): 
            if (str(grid[row][col]) == "0"): #checks if there are 0s
                flag = False
            elif (grid[row][col] == grid[row][col+1]): #checks if equal then simply double 
                flag = False    
                    
    for row in range (3):
        for col in range (4): 
            if (str(grid[row][col]) == "0"): #checks if there are 0s
                    flag = False
            elif (grid[row][col] == grid[row+1][col]): #checks if they are equal to double
                    flag = False
            
    return flag                 #returns the flag value

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    flag = True   #declaring boolean value for flag
    for row in range (height):
        for col in range (height):
            x = grid[row][col] #varible for each value
            if (x>=32):   #checks varible (x)
                flag = True
                if flag:
                    return flag
            else:
                flag = False
    return flag        #returns flag
            
def copy_grid (grid):       
    """return a copy of the grid"""
    grid_copy = []      #creates an empty array"[]"
    for i in range(height):
        grid_copy.append(grid[i][:]) #adds on to array
    return grid_copy   
            

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    flag = True               #boolean value
    for row in range (height):
        for col in range (height):          
            if not (grid1[row][col]) == (grid2[row][col]): #check if they are not equal, then adds 0s     
                return False

    return flag               
    