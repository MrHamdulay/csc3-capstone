#Module with grid functions
#Denzel Ncube
#28 April 2014

import copy

def create_grid(grid):
    #create a 4x4 grid
    for i in range (4):
        grid.append ([0] * 4)    


def print_grid (grid):
    #printing out a 4x4 grid in 5-width columns within a box
    for i in range(0,6):
        for j in range(0,6):
            if i ==0 and j ==0 :
                print('+',end= '')
            elif i == 0 and j == 5:
                print('+')
            elif i == 5 and j == 0:
                print('+', end = '')
            elif i ==5 and j ==5:
                print('+')
            elif i ==0 or i == 5:
                print('-'*5,end = '')
            elif j ==0:
                print('|',end = '')
            elif j == 5:
                print('|')
            else:
                #Making the column width 5
                if grid[i-1][j-1] == 0:
                    print("{0:<5}".format(''), end = '')
                else:
                    print("{0:<5}".format(str(grid[i-1][j-1])), end = '')   
            
    
def check_lost (grid):
    #returning True if there are no 0 values and no adjacent values that are equal; otherwise False
    answer = ''
    for i in range(4):
        if grid[0][i] == 0:
            answer += 'False'
        if grid[0][0] == grid[0][1]:
            answer += 'False'
        if grid[0][1] == grid[0][2]:
            answer += 'False'
        if grid[0][2] == grid[0][3]:
            answer += 'False'         
        if grid[0][0] == grid[1][0]:
            answer += 'False'
        if grid[1][0] == grid[2][0]:
            answer += 'False'
        if grid[2][0] == grid[3][0]:
            answer += 'False'         
                
    for i in range(4):
        if grid[1][i] == 0:
            answer += 'False'
        if grid[1][0] == grid[1][1]:
            answer += 'False'
        if grid[1][1] == grid[1][2]:
            answer += 'False'
        if grid[1][2] == grid[1][3]:
            answer += 'False'         
        if grid[0][1] == grid[1][1]:
            answer += 'False'
        if grid[1][1] == grid[2][1]:
            answer += 'False'
        if grid[2][1] == grid[3][1]:
            answer += 'False'             
    
    for i in range(4):
        if grid[2][i] == 0:
            answer += 'False'
        if grid[2][0] == grid[2][1]:
            answer += 'False'
        if grid[2][1] == grid[2][2]:
            answer += 'False'
        if grid[2][2] == grid[2][3]:
            answer += 'False'         
        if grid[0][2] == grid[1][2]:
            answer += 'False'
        if grid[1][2] == grid[2][2]:
            answer += 'False'
        if grid[2][2] == grid[3][2]:
            answer += 'False'           
    
    for i in range(4):
        if grid[3][i] == 0:
            answer += 'False'
        if grid[3][0] == grid[3][1]:
            answer += 'False'
        if grid[3][1] == grid[3][2]:
            answer += 'False'
        if grid[3][2] == grid[3][3]:
            answer += 'False'         
        if grid[0][3] == grid[1][3]:
            answer += 'False'
        if grid[1][3] == grid[2][3]:
            answer += 'False'
        if grid[2][3] == grid[3][3]:
            answer += 'False'             
    
    if 'False' in answer:
        return False
    else:
        return True        
            
                
              
def check_won (grid):
    #returning True if a value>=32 is found in the grid; otherwise False
    answer = ''
    for i in range(4):
                for j in range(4):
                    if grid[i][j] >= 32 :
                        answer += 'True'
                        break
                    else:
                        answer += 'False' 
    if 'True' in answer:
        return True
    else:
        return False    

def copy_grid (grid):
    #returning a copy of the grid
    newgrid = copy.deepcopy(grid)
    return newgrid
            



def grid_equal (grid1, grid2):
    #checking if 2 grids are equal gr
    boolean = ""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                boolean += 'False'
            else:   
                boolean += ''
    if 'False' in boolean:
        return False
    else:
        return True
    