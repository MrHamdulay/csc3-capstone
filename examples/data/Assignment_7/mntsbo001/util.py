"""Program to manipulate 2D array
Sbonelo Mntungwa
2 May 2014"""

def create_grid(grid): # Creating a grid
    for i in range(4):
        grid.append(['0']*4)#making a 4X4 grid
        


def print_grid(grid): #printing the grid
    pattrn = ("+"+"-"*20+"+") #assigning the pattern
    print(pattrn)
    for i in grid:
        print("|",end = '')
        for j in i:
            if j == 0:
                j = ' '
            print("{0:<5}".format(j), end = '') #extending the column width
        print("|", end = '\n')
    print(pattrn)
                
                                
def check_lost(grid): #Determining whether person has lost
    for j in range(4):
        for k in range(4):
            if grid[j][k] == 0:# to see if there is a 0 value in array
                return False
    for j in range(4): #Checking the adjacent values in the same row
        for k in range(3):
            if grid[j][k] == grid [j][k+1] or grid[j][k] == grid[j][k-1]: 
                return False
            else:
                return True
    for j in range(3):
        for k in range(4): #Checking the adjacent values in the same column
            if grid[j][k] == grid[j+1][k] or grid[j][k] == grid[j-1][k]:
                return False
            else:
                return True
                      
def check_won(grid): #to see if the person has won
    a = []
    for i in grid:
        max_val = max(j for j in i)
        a.append(max_val)# Determining the maximum value in each row
    a.sort()
    if max(k for k in a)>=32: #Determining the maximum of the maximum values if it is greater than 32
        return True
    else:
        return False
    
def copy_grid(grid): #copying grid to another grid 
    import copy
    new_grid = []
    new_grid = copy.deepcopy(grid)
    return new_grid
    

def grid_equal (grid1, grid2): # finding out if grids are the same
    if grid1 == grid2:
        return True
    else:
        return False



            



            