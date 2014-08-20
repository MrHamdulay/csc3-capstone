#30 April 2014
#Many untility functions for question 2 and 3
#LYLJON002

def create_grid(grid):          #create grid
    for j in range (4):
            grid.append ([0] * 4)    

def print_grid(grid):               #print grid
    print("+" + "-"*20 + "+")     #top line
    for j in range(4):      
        print("|",end='')
        for i in grid[j]:                   #print inner grid
            if i==0:
                print(" "*5,end='')   
            else:
                print(i," "*(5-len(str(i))),sep='',end='') 
        print("|")
    print("+" + "-"*20 + "+")       #bottom line
    
def check_lost (grid):  #check if game is lost
    
    for i in range(4):
        for j in grid[i]:
            if j == 0:
                return False
            
    for i in range(3):
        for j in range(4):
            if grid[i][j]==grid[i+1][j]:
                return False


    for i in range(4):
        for j in range(3):
            if grid[i][j]==grid[i][j+1]:
                return False


    return True



def check_won (grid):               #check if game is won
    for i in range(4):
        for j in grid[i]:
            if j >= 32:             #if more than 32 then win
                return True
            
    return False        #otherwise no win
            



def copy_grid (grid):           #copies a grid
    newgrid=[]
    create_grid(newgrid)
    for i in range(4):
        for j in range(4):
            newgrid[i][j] = grid[i][j]
    return newgrid                          #return new grid

def grid_equal (grid1, grid2):      #check if grids are equal
    if grid1 == grid2:
        return True
     
    return False