
#Shahrain Coovadia
#CVDSHA992
global grid                           #create a global variable
grid=[]                   #empty list

def create_grid(grid):
    for l in range (4):       #create row          
        list=[]
        for r in range(4):    #create column
            row.append(0)            
            grid.append(row)
            

def print_grid (grid):
    print('+', '-' *20, '+', sep='')          #print box
    for i in range(4):
        for l in range(4):
            if l==0:
                print('|', end='')
            if grid [i][l] == 0:
                print("{0:<5}",format(" "), end="")        #formatting box/grid
            else:
                print("{0:<5}".format(grid[i][l]), end="")
            if l==3:
                print('|' ,end='\n')
    print('+', '-'*20, '+', sep ='')
    
    
def check_lost(grid):
    for i in range (4):           
        
        for num in range(4):
            if grid[i][num] == 0:        #check for no empty space
                return False
        for num in range(3):
            if grid[i][num] == grid[i][num+1]:       #2 similar numbers will return false   
                return False
            
    return True
def check_won (grid):
    for i in grid:
        for a in i: 
            if a>=32:              #returns true if value in grid is more than 32
                return True
            return False
        
def copy_grid(grid):
    copy=[]
    for l in range (4):
            row=[]                    #creates new grid           
            for r in range(4):
                row.append(0)            
                copy.append(row)    

    for i in range (4):
        for l in range(4):                  #returns grid
            copy[i][l]=grid[i][l]
        return copy
    
def grid_equal(grid,grid2):        #cheks if grid is equal
    for i in range(4):                          
        for l in range(4):
            if grid[i][l] != grid2[i][l]:
                return False
            return True
            
    
                
    