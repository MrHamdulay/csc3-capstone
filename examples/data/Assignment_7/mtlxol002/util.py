"""CSC1015F Assignment 7 Question 2 
Xola Matlanyane MTLXOL002
2 May 2014"""

def create_grid(grid): #create a 4x4 grid
    for i in range(4):
        grid.append(4*[0])
          
          
def print_grid(grid):  #pprint out a 4x4 grid with 5-width columns within a box
    print("+--------------------+")
    for i in range(4):
        print('|', end='')
        for x in grid[i]:
            if x != 0:
                print(str(x)+(5-len(str(x)))*' ', end='')
            else:
                print(5*' ', end='')
        print('|')
    print("+--------------------+")
    
    
def check_lost(grid): #return Tre if there are no 0 values and no adjacent values that are equal; otherwise False
    #if there are no 0s
    zero = 'default'
    same = 'default'
    right = 'no'
    down = 'no'
    
    for i in range(4):
        for x in grid[i]:
            if x == 0:
                break
            else: zero = 'no'
        
    #check if no adjacent values are equal
    #check right
    for i in range (4):
        for x in range (3):
            if grid[i][x] == grid[i][x+1]:
                right = 'yes'
                break
         
            
    #check down
    for i in range (3):
            for x in range (4):
                if grid[i][x] == grid[i+1][x]:
                    down = 'yes'
                    break
               
    if right == 'no' and down == 'no':
        same = 'no'
            
        
    if zero == 'no' and same == 'no':
        return True
    else: return False
    

def check_won(grid): #return True if a value>=32 is found in the grid; otherwiose False
    for i in range(4):
        for x in grid[i]:
            if x >= 32:
                return True
    return False


def copy_grid(grid): #return a copy of the grid
    gridcopy = []
    gridcopy = [x[:] for x in grid]
        
    return gridcopy


def grid_equal(grid1, grid2):#check if 2 grids are equal - return boolean value
    if grid1 == grid2:
        return True
    else: return False
    