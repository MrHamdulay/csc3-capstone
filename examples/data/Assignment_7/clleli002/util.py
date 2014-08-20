"""utility functions to manipulate a 2D array of size 4x4
27/04/2013
Elizabeth Cilliers"""

size=4
grid=[]

def create_grid(grid):
    """create a 4x4 grid"""
    
    for i in range (size):
        grid.append ([0] * size)
  

def print_grid (grid):
    """print grid"""
    print("+--------------------+")
    for row in range (size):
        for col in range (size):
            value=grid[row][col] #each value in the grid
            if value==0: #if the value is zero, change the zero to an empty space
                value=" "
            if col==0: #for first column, make width 5 and add line at start.
                value='{0:<5}'.format(value)
                print("|", value,end="",sep="")
            elif col==3: #for last column make width 5 and add line at end
                
                value='{0:<5}'.format(value)
                print (value,"|",end="",sep="")                
            else:
                # make all other columns just width 5.
                value='{0:<5}'.format(value)
                print (value,end="",sep="")
        print()
    print("+--------------------+")

        
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    
    for row in range(size):
        for col in range (size):        
            
            
            if grid[row][col]== " ": #if the value in grid is empty space (zero) return false
                return False
            
            #checking row below
            elif (row+1)<=3: #row+1 cannot be more than 3
                if grid[row][col]==grid[row+1][col]: #if values above and below are equal return false else return true.
                    return False
                
            #checking row above
           # elif (row-1)>=0: #row-1 cannot be less than zero
            #    if grid[row][col]==grid[row-1][col]: #if values above and below are equal return false else return true.
             #       return False  
            
            #checking col to right
            elif (col+1)<=3: #col+1 cannot be more that 3
                if grid[row][col]==grid[row][col+1]: #if values on left and right equal return false else return true.
                    return False
              
            #checking col to the left
            #elif (col-1)>=0: #col-1 cannot be less than zero
            #    if grid[row][col]==grid[row][col-1]: #if values on left and right equal return false else return true.
            #        return False
            else:
                return True
  
            

def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    maximum=0 #initialise max counter
    for row in range(size):
            for col in range (size):
                if grid[row][col]>=maximum: #if value in grid is more than max make max equal to the new value.
                    maximum=grid[row][col]
    if maximum>=32: #if the max is greater or equal to 32 return true or else false.
        return True
    else:
        return False

def copy_grid (grid):
    """return a copy of the grid"""
    copy=[] #make a blank 4x4 grid
    for i in range (size):
            copy.append ([] * size)    
    
    
    for row in range(size):
        for col in range (size):
            copy[row].append(grid[row][col]) #append each element in initial grid into the new copy grid and return copy.
    return copy

def grid_equal (grid1,grid2):
    """check if 2 grids are equal - return boolean value"""
    for row in range(size):
        for col in range (size): 
            if grid1[row][col]!=grid2[row][col]: #check if each corresponding element in grid1 and grid2 are equal. if they are not then return false.
                return False
    else:
        return True
                
    
                 
    
                