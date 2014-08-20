'''Wade Cresswell'''
def create_grid(grid):
    for i in range (4):
        grid.append([0]*4)
    return grid
def print_grid(grid):
    print('+--------------------+')
    for row in range (4):
        print('|',end='')
        for coloumn in range (4):
            if grid[row][coloumn] == 0:
                print('     ',end='') #prints spaces if item is a 0
            else:
                print(grid[row][coloumn],' '*(5-len(str(grid[row][coloumn]))),sep='',end='') #prints each item in the grid with appropriate spacing
        print('|') #prints boarder of box
    print('+--------------------+')
def check_won (grid): #checks if grid has won
    flag = False
    for row in range (4):
            for coloumn in range (4):
                if grid[row][coloumn] >= 32: # if any block is >= 32 the function returns true
                    flag = True
                    return flag
    return flag
def check_lost (grid): #CHECKS IF LOST
    flag = True
    for row in range (4): #CHECKS IF THERE ARE ANY ZEROS
                for coloumn in range (4):
                    if grid[row][coloumn] == 0:
                        flag = False
                        return flag
    for row in range (4): #CHECKS IF ANY ELEMENTS ARE EQUAL TO THE ONE DIRECTLY TO THE RIGHT OF IT
                for coloumn in range (3):
                    if grid[row][coloumn]==grid[row][coloumn+1]:
                        flag = False
                        return flag
    for row in range (3): #CHECKS IF ANY ELEMENTS ARE EQUAL TO THE ONE DIRECTLY TO THE BELOW IT
                for coloumn in range (4):
                    if grid[row][coloumn]==grid[row+1][coloumn]:
                        flag = False
                        return flag              
    return flag
def copy_grid(grid):
    trg = [[0]*4,[0]*4,[0]*4,[0]*4]
    for row in range (4):
                for coloumn in range (4):
                    trg[row][coloumn]=grid[row][coloumn]
    return trg #creates copy of grid
def grid_equal(grid1,grid2):
    if grid1 == grid2:
        return True #returs true if grids are equal
    else:
        return False



    
          
