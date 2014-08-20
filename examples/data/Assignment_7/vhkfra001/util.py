# Assignment 7
# Question 2: Foundation for '2048' game 
# Frans van Hoek
# 30 April 2014

def create_grid(grid):
    for i in range(4):
        grid.append(4*[0])
          
          
def print_grid(grid):
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
    
    
def check_lost(grid):
    # if there are no zero's
    zero = 'default'
    same = 'default'
    right = 'no'
    down = 'no'
    
    for i in range(4):
        for x in grid[i]:
            if x == 0:
                break
            else: zero = 'no'
        
    # now check if no adjacent values are equal
    # check right
    for i in range (4):
        for x in range (3):
            if grid[i][x] == grid[i][x+1]:
                right = 'yes'
                break
         
            
    # check down
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
    

def check_won(grid):
    for i in range(4):
        for x in grid[i]:
            if x >= 32:
                return True
    return False


def copy_grid(grid):
    gridcopy = []
    gridcopy = [x[:] for x in grid]
        
    return gridcopy


def grid_equal(grid1, grid2):
    if grid1 == grid2:
        return True
    else: return False
    