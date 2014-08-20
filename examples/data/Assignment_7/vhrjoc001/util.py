#vhrjoc001
#functions used to make the 2048 game
#assignment 7 q2

#Importing copy for the copy_grid function
import copy 

#making grid
def create_grid(grid): 
    """Creates a 4x4 grid"""
    for i in range (4): 
        grid.append ([0] * 4)         

#printing the aesthetics of the grid 
def print_grid (grid): 
    """Prints out a box around a 4x4 grid"""
    print('+--------------------+') 
    for i in grid: 
        print('|',end='') 
        for j in i: 
            j=str(j) 
            if j=='0': 
                print(' '.ljust(5),end='')
            else: 
                print(j.ljust(5),end='') 
        print('|')         
          
    print('+--------------------+') 
  
def check_lost (grid): 
    """Checks if the player has lost the game by having no adjacent tiles equal or having no 0 tiles. 
    It returns True if the player has lost and returns False if the player hasn't"""
    for i in range(len(grid)-1):  #Checks Rows
        for j in range(len(grid[i])-1): #Checks columns
            #It checks if there are any zeros 
            if grid[i][j]==0:  
                return False
            #Checking if the value to the right is equal to the value 
            elif grid[i][j]==grid[i][j+1]: 
                return False
            #check if the value above equals value 
            elif grid[i][j]==grid[i+1][j]: 
                return False
    return True

def check_won (grid): 
    """Checks if the player has won the game by getting 32 or more. 
    It returns True if the player has won and returns False if the player hasn't"""
    for i in range(len(grid)): 
            for j in range(len(grid[i])): 
                if grid[i][j]>=32: 
                    return True
    return False
 #make the grid base 
def copy_grid (grid): 
    """Returns a copy of the grid"""
    CopyOfGrid=copy.deepcopy(grid) 
    return CopyOfGrid 
  
#update grid base
def grid_equal (grid1, grid2): 
    """Checks if two given grids are equal. Returns True if they are. Returns False if they are not"""
    for i in range(len(grid1)): 
            for j in range(len(grid1[i])): 
                if grid1[i][j]==grid2[i][j]: 
                    continue
                else: 
                    return False
    return True