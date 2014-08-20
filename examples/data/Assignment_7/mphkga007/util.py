"""program to manipulate a 2d array of size 4x4
kenneth mphele
28/04/2014"""

#create a grid
def create_grid(grid):
    """ creates a 4x4 grid"""
    
    for i in range(4):
        grid.append([0]*4)
  #print the grid
def print_grid(grid):
    """ prints the grid"""
    print("+--------------------+")
    for row in range(4):
        print("|",end="")
        for colunm in range(4):
            if grid[row][colunm]==0:
                grid[row][colunm]= ' '
                print("{:<5}".format(grid[row][colunm]),end="")
                grid[row][colunm]=0
                
            else:
                print("{:<5}".format(grid[row][colunm]),end="")
        print("|")
    print("+--------------------+")


def check_lost(grid):
        # checks if any grid has zero and the rows if are they have the same value
        for row in range(4):
                for colunm in range(4):
                        if colunm<3:
                                if grid[row][colunm]==0 or  grid[row][colunm]==grid[row][colunm+1]:
                                        return False
                        
                        
         #checks for identical colunms                       
        for colunm in range(4):
                for row in range(4):
                        if row<3:
                                if grid[row][colunm]==grid[row+1][colunm]:
                                        return False
        return True

#check won
def check_won(grid):
        for row in range(4):
                for colunm in range(4):
                        if grid[row][colunm]>=32:
                                return True
        return False
#make a copy of grid
def  copy_grid(grid):
        #make a new copy of grid
        grid_copy=[]
        for i in range(4):
                grid_copy.append([0]*4)
        #goes through grid assigning the element if grid to grid_copy
        for row in range(4):
                for colunm in range(4):
                        grid_copy[row][colunm]=grid[row][colunm]
        
        return grid_copy
def grid_equal(grid1,grid2):
        #checks if two grids are equal
        for row in range(4):
                for colunm in range(4):
                        if grid1[row][colunm]!=grid2[row][colunm]:
                                return False
        return True

                
        
         


        
                                

