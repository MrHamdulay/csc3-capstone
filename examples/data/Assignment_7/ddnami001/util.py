#Amitha Doodnath
#DDNAMI001
#30/04/2014
#Programme of utility functions  to manipulate 2D arrays for question2.py and the game 2048

def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
        

def print_grid(grid):
    print("+", ("-"*20), "+",sep="")
    
    f="{0:<5}"
    for row in range(4):
        print("|",sep="",end="")
        for column in range (4):
            if grid[row][column]==0:
                print(f.format(" "),sep="",end="")
            else:
                print(f.format(grid[row][column]),sep="",end="")
        print("|")
    
    print("+", ("-"*20), "+",sep="")




def above(grid):
    for row in range(1,4):
        for column in range(4):
            if grid[row-1][column]== grid[row][column]:
                return True
    return False

def below(grid):
    for row in range(0,3):
        for column in range(4):
            if grid[row+1][column]== grid[row][column]:
                return True
    return False

def left(grid):
    for row in range(4):
        for column in range(1,4):
            if grid[row][column-1]== grid[row][column]:
                return True
    return False

def right(grid):
    for row in range(4):
        for column in range(0,3):
            if grid[row][column+1]== grid[row][column]:
                return True
    return False

'''def horizontalAL(grid):
    for row in range(1,4):
        for column in range(1,4):
            if grid[row-1][column-1]== grid[row][column]:
                return True
    return False
        
def horizontalBL(grid):
    for row in range(0,3):
        for column in range(1,4):
            if grid[row+1][column-1]== grid[row][column]:
                return True
    return False

def horizontalAR(grid):
    for row in range(1,4):
        for column in range(0,3):
            if grid[row-1][column+1]== grid[row][column]:
                return True
    return False

def horizontalBR(grid):
    for row in range(0,3):
        for column in range(0,3):
            if grid[row+1][column+1]== grid[row][column]:
                return True
    return False'''

    

def check_lost(grid):
    a=left(grid)
    b=right(grid)
    c=above(grid)
    d=below(grid)
    '''e=horizontalAL(grid)
    f=horizontalBL(grid)
    g=horizontalAR(grid)
    h=horizontalBR(grid)'''
    
    flag=True
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                flag=False
                break
            
    if (a==True or b==True or c==True or d==True) or (flag==False):
        return False
    
    else:
        return True
    
    
def check_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                return True
    return False


def copy_grid(grid):
    a= []
    create_grid(a)
    for i in range(4):
        for j in range(4):
            a[i][j]=grid[i][j]
    
    return a



def grid_equal(grid1,grid2):
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True
    
    