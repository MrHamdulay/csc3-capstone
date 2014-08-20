"""Keegan Naidoo
NDXKEE009
27 April 2014"""

grid=[]
height=4

def create_grid (grid):         #Creates 4x4 grid

    for i in range(height):
        grid.append([0]*height)

    #print ("END")
    
def print_grid (grid):     #Prints grid in box
    
    print("+"+"-"*20+"+")
    
    for row in range (height):
        
        for col in range (height):
            
            if grid[row][col]==0:
                
                grid[row][col]=" "
                
            if col ==0:
                
                print("|"+"{0:5}".format(str(grid[row][col])),end="")
            
            elif col==3:
                
                print ("{0:5}".format(str(grid[row][col]))+"|",end="")   
                
            else:
                
                print ("{0:5}".format(str(grid[row][col])),end="")
                
        print()
    print("+"+"-"*20+"+")   
    
def check_lost(grid):         #Checks if they are spaces free or two adjacent equal values if there aren't then you lose
    
    boo=False
    
    for row in range (3):
        
        for col in range (3):
            
            x=grid[row][col]  
            
            if grid[row][col]== " ":
                grid[row][col]=0
            if grid[row][col]==0 or grid[row][col]==grid[row][col+1]:
                return False
           
            
    for row in range (3):
                   
        for col in range (3):
                       
            x=grid[row][col]  
                       
            if grid[row][col]== " ":
                grid[row][col]=0
            if grid[row][col]==0 or grid[row][col]==grid[row+1][col]:
                return False               
        #return boo    
    return True
            
def check_won(grid):
    
    boo=False
    
    for row in range (height):
        
        for col in range (height):

            if grid[row][col]!=" " :
                
                if grid[row][col]>=32:

                    boo=True        

    return boo

def copy_grid(grid):     #Makes a copy of the grid
    
    c_grid=[]
    
    for i in range(height):
            c_grid.append([0]*height)    
    
    for row in range (height):
                   
        for col in range (height):  
                
            c_grid[row][col]=grid[row][col]
                
    return c_grid

def grid_equal (grid1, grid2):     #Checks if two grids given are equal
    
    if grid1==grid2:
       
        return True
    else:
        return False
   
            


#create_grid(grid)

#print_grid(grid)