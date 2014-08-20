""" Create utility functions
Kumaran Reddy
2 May 2014 """


grid=[]
def create_grid(grid):
    O_s=[0,0,0,0]
    for i in range (4):
        grid.append(O_s) #To create four rows of the array "O_s"
    return grid

def print_grid (grid):
    print('+--------------------+') #To print first line 
    for i in range(4):
        print('|', end='') #To print lefthand side border
        for k in range(4):
            if grid[i][k]==0: #When there is a 0,it must be replaced by 5 spaces
                print(' '*5,end='')
            else:
                print(grid[i][k],(5-len(str((grid[i][k]))))*' ',sep='',end='') #Converting the value to a string to use the "len" function so can print value and subtract spaces accordingly
        print('|')
    print('+--------------------+') #To print last line
    
def check_lost(grid):
    for i in range(4):
        for k in range(4):
            if grid[i][k]==0: #To check if there are any spaces left so then the user hasn't lost yet
                return False
            
            if k!=3:
                if grid[i][k]==grid[i][k+1]: #To check whether the values are within the box(range)-horizontally
                    return False
            if i!=3:
                if grid[i][k]==grid[i+1][k]: #To check whether the values are in the box(range)-vertically
                    return False
         
                
    return True    
                            

def check_won(grid):
    for i in range(4):
        for k in range(4):
            if grid[i][k]>=32: #The user has won if a position is greater than or equal to 32
                return True
    return False

def copy_grid(grid):
    c_grid=[]
    for i in range(4):
        grid_1=[]
        for k in range(4):
            grid_1.append(grid[i][k]) #Inserting values at each position for each row
        c_grid.append(grid_1) #Then adding this "row" to the whole grid and starting with a new "row" each time the "i" loop iterates.
    return c_grid
            
def grid_equal(grid1, grid2):
    for i in range(4):
        for k in range(4):
            if grid1[i][k]!=grid2[i][k]: #To check if both the grids are equal
                return False
    return True