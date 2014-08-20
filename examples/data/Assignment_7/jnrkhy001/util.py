#Khyati Jinerdeb
#02 May 2014
#Assignment 7
#module of utility functions to manipulate 2-dimensional arrays of size 4X4

#to create a 4x4 grid
def create_grid(grid):
    for i in range(4):
        grid.append ([0]*4)
    return grid
    

#to print  the grid
def print_grid(grid):
    print("+--------------------+")
    
    for i in range(4):
        print("|", end="")
        for j in range(4):
            if str(grid[i][j])=="0":
                print(" "*5,end="")   #if it's not a number, ithas to be a space, hence spacex5
            else:
                print("{0:<5}".format(str(grid[i][j])), end="")   #to format the numbers
            
        print("|")
    print("+--------------------+")
    
#to check if there  are no 0 values and no adjacent values that are equal
def check_lost(grid):
    for i in range(4):
        for j in range(4):
            if str(grid[i][j])==0:
                return False
            elif j+1<4 and str(grid[i][j])==str(grid[i][j+1]):
                return False
            elif i+1<4 and str(grid[i][j])==str(grid[i+1][j]):
                return False
            
    return True

#to return true if a value is less or equal to 32 or else return false
def check_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                return True
    return False

#returns a copy of the grid
def copy_grid(grid):
    grid1=[]
    for i in range(4):
        a=[]
        for j in range(4):
            a.append(grid[i][j])
        grid1.append(a)
    return grid1
    
#to check if 2 grids are equal and return boolean values
def grid_equal(grid1,grid2):
    for i in range(4):
        for j in range(4):
            if str(grid1[i][j])!=str(grid2[i][j]):
                return False
    return True

               
    
    

            
            
                     
            
        
        
            
            
            
            
    
            
            
            
        
        


        