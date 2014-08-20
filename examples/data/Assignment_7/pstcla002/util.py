"""util module
Claudia Pastellides
01 May 2014"""

def create_grid(grid): #adding one row of the grid at a time
    for block in range(4):
        grid.append([0]*4)
        return grid

def print_grid(grid): #print out grid in 5 width columns within a box
    cross="+"
    dash="-"
    line="|"
    print(cross,dash*20,cross,sep="") #top of box
    for row in range(4):
        print(line,end="",sep="") #left hand side
        for col in range(4):
            if grid[row][col]==0:
                print(" "*5,end="") #blank spaces if item is zero
            else:
                print(grid[row][col],(5-len(str((grid[row][col]))))*" ",sep="",end="") #what remains in width 5
        print(line) #right side of box
    print(cross,dash*20,cross,sep="")
    
def check_lost(grid): #true if no 0 and no equal aadjacent numbers
    for row in range(4):
        for col in range(4):
            if grid[row][col]==0:
                return False
                
            if row!=3:
                if grid[row][col]==grid[row+1][col]:
                    return False
            if col!=3:
                if grid[row][col]==grid[row][col+1]:
                    return False
    return True
    
def check_won(grid):
    #return true if value >=32
    
    for row in range(4):
        for col in range(4): #checks through blocks to find 32
            if grid[row][col]>=32:
                return True
    return False

def copy_grid(grid):
    #return copy of grid
    printgrid=[]
    for row in range(4):
        row_list=[]
        for col in range(4):
            row_list.append(grid[row][col])
        printgrid.append(row_list)
    return printgrid
        
def grid_equal(grid1,grid2):
    #check if 2 grids are equal
    for row in range(4):
        for col in range(4):
            if grid1[row][col]!=grid2[row][col]:
                return False
    return True