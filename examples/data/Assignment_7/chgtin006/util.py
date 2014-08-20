"""Program to manipulate 2 dimensional arrays of size 4x4
By Tinashe Choga 
2/5/2014"""

def create_grid(grid): 
    for row in range (4):
        grid.append([0]*4)   
        #appending the zero's to the list

def print_grid(grid):
    print("+"+("-"*20)+"+")
    for col in range (4):
        print("|",end='')
        for row in range(4):
            if grid[col][row]==0:# checking if the output is equal to zero
                print("{:<5}".format(" "),end='') #formatting the text to be right aligned
            else:
                print ("{:<5}".format(grid[col][row]),end='')
        print("|")
    print("+"+("-"*20)+"+")

def check_lost(grid):
    for col in range (4):
        for row in range (4):
            if grid [col][row]==0:
                return False
            if 0 <= row+1 < 4: #checking for equality between adjacent terms
                if grid [col][row]==grid[col][row+1]: #if equal game not over
                    return False
            if 0<= col+1< 4:
                if grid [col][row]==grid[col+1][row]:
                    return False
    return True
            
def check_won(grid):
    for col in range (4):
        for row in range (4):
            if grid[col][row] >=32:   
                return True
    return False
            
def copy_grid (grid):
    copygrid=[]
    for row in range (4):
        copygrid.append([0]*4)
    for row in range(4):
        for col in range (4):
            copygrid[row][col]=grid[row][col]
    return copygrid
    
def grid_equal(grid1,grid2): #checking for grid equality
    if grid1==grid2:
        return True
    return False
        
            