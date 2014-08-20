'''Util functions 
Siphesihle Zwane 
29 April 2014'''

import copy 
def create_grid(grid):
    grid=[]
    for i in range (4):
        grid.append ([" "]*4)
    return grid

def print_grid (grid):        
        print("+","-"*20,"+",sep="")
        form= "{:<4}"   #getting aignment 
        for row in range(4):           
            print("|", end="") 
            for col in range(4): 
                    if grid[row][col]==0:  #to get rid of all the 0
                        print(form.format(" "),end=" ")
                    else:    
                        print (form.format(str(grid[row][col])),end=" ") #end works works with 4 column format=5
            print("|")      
        print("+","-"*20,"+", sep="")    


def check_lost (grid):
    for row in range(4):
        if 0 in grid[row]: # checks 0 in each column
            return False
        for col in range(4):
                if  row> 0 and grid[row-1][col]==grid[row][col]:      #checks a row below/above       
                    return False
                #does not check the 0 value row and col
                elif col>0 and grid[row][col-1]==grid[row][col] :    #same with col
                    return False
    else:
        return True
                

def copy_grid(grid):

    copy_grid=copy.deepcopy(grid)
    return copy_grid


def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False

def check_won (grid):
    Value=False
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                Value=True
    return Value
            