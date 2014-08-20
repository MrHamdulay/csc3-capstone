#shane horsley
#utility funtion to be used in supplied program

def create_grid(grid): #create a 4*4 grid
    for i in range(4):
        grid.append([0] * 4)
    
    
def grid_equal(grid1,  grid2): #check whether 2 grids are equal to each other
    if grid1 == grid2:
        return True
    else:
        return False
   

def print_grid (grid): #print grid with a boarder and spacing between items
    print("+--------------------+")
    for row in range(4):
        print("|",end='')
        for col in range(4):       
            if grid[row][col] ==0:
                print(" ",end=(5-len(str(grid[row][col])))*" ")
            else:
                print(grid[row][col],end=(5-len(str(grid[row][col])))*" ")
        print("|")
    print("+--------------------+")

def check_lost (grid): #check whether grid is full and no more sliding options
    space= 't'
    equal_num= 't'
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 0:
                space = 0
    
    for row in range(3):
        for col in range(3):
            if grid[row][col] == grid[row][col+1]:
                equal_num=0                
    
    
    for row in range(3):
        for col in range(3):
            if grid[row][col] == grid[row+1][col]:
                equal_num=0
        
     
    if space== 't' and equal_num== 't':
        return True
     
    else:
        return False
     
                

def check_won (grid): #check whether 32 is in the grid
    for row in range(4):
        for col in range(4):
            if grid[row][col] == 32: 
                return True
            if grid[row][col] >32:
                return True
            else:
                continue
    return False

def copy_grid (grid): #make a copy of a grid
    copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for row in range(4):
        for col in range(4):
            copy[row][col]= grid[row][col] 
    return copy


