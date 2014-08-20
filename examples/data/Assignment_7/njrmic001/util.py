#A Python module to manipulate 2-D arrays of size 4x4
#Author: Michelle Njoroge
#Date: 30 April 2014

def create_grid(grid):
    """create a 4x4 grid"""
    box=""
    for i in range (4):
        #add a list of 4 0's to grid 
        grid.append ([0] * 4)
    #loops through the entire grid list
    for a in range(len(grid)):
    #loop through the list in position a of the grid 
        for b in range(len(grid[a])):
        #adds the character at grid[a][b] to the string box
            box+=str(grid[a][b])
            if b==3: #if the loop gets to the end of any inner list
                box+="\n" #move the following items to a new line
            else: pass
    return box

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    box="" 
    print("+"+"-"*20+"+")
    #loop through the row and columns
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col==0:
                box+="|"
            if grid[row][col]!=0:
            #print the number at this position + a space equal to 5 less the number of characters in the number
                box+=str(grid[row][col])+" "*(5-len(str(grid[row][col])))
            else:
                box+=" "*5
            if col==3:
                box+="|"+"\n"
            else: pass            
    print(box+"+"+"-"*20+"+",end=" ")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]==0:
                    return False
                if row<3: #if not at the last row
                    if grid[row+1][col]==grid[row][col]: #check whether the number is equal to a number below it 
                        return False
                if col<3: # if not at the last column
                    if grid[row][col+1]==grid[row][col]: #check whether the number is equal to a number to the right of it
                        return False
                if row>0: #if not at the first row
                    if grid[row-1][col]==grid[row][col]: #check whether the number is equal to the number above it
                        return False
                if col>0: #if not at the first column
                    if grid[row][col-1]==grid[row][col]: #check whether the number is equal to the number before it
                        return False
    return True #(otherwise)
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]>=32:
                return True
    return False
                

def copy_grid (grid):
    """return a copy of the grid"""
    outer_grid=[]
    for a in range(len(grid)):
        inner_grid=[] #initialise inner grid 
        for b in range(len(grid[a])):
            inner_grid.append(grid[a][b]) #adds to inner grid 
        outer_grid.append(inner_grid) #adds to outer grid
    
    return outer_grid
            

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    if grid1==grid2:
        return True
    else: return False






    