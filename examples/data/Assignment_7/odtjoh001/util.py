"""Program to manipulate 2-D arrays of size 4 * 4
John Odetokun ODTJOH001
27 April 2014"""

def create_grid(grid):
    for i in range(4):
        grid.append([0] *4)
        
def print_grid (grid):
    print("+" , 20*"-", "+",sep = "")
    for j in range(4):
        print("|",end = "")
        for k in range(4):
            if(grid[j][k] == 0):
                print("{0:<5}".format(' ') , end = "")
            else:
                print("{0:<5}".format(grid[j][k]) , end = "")
        print("|")
    print("+" , 20*"-", "+",sep = "")

def check_lost(grid):
    flag1 = True
    for b in range(4):
        for a in range(4):
            if grid[b][a] == 0:
                flag1 = False
    flag2 = False          
    count = 0
    for i in range(4):
        for k in range(3):
            if grid[i][k] == grid[i][k+1] and grid[i][k] != 0 and grid[i][k+1]!= 0:
                count += 1
    for l in range(4):
        for j in range(3):
            if grid[j][l] == grid[j+1][l] and grid[j][l] != 0 and grid[j+1][l]!= 0:
                count += 1
    if count == 0:
        flag2 = True
    if flag1 == True and flag2 == True:
        return True
    else:
        return False
    
    
def check_won(grid):
    flag = False
    for i in range(4):
        for j in range(4):
            if(grid[i][j] >= 32):
                flag = True
    return flag

def copy_grid(grid):
    ngrid = []
    for i in range (4):
        nngrid = []
        for k in range(4):
            nngrid.append(grid[i][k])
        ngrid.append(nngrid)
    
    return ngrid

def grid_equal(grid1, grid2):
    return grid1 == grid2


    
            

            
                
    