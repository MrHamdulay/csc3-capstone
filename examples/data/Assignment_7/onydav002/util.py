def create_grid (grid):
    for row in range (4):
        tempgrid = []
        for col in range (4):
            tempgrid.append(0)
        grid.append(tempgrid)

def print_grid (grid):
    print("+--------------------+")
    for row in range (4):
        print ("|",end = "")
        for col in range (4):
            if grid [row][col] == 0:
                print ("{:<5}".format(" "),end="")
                
            else:
                print ("{:<5}".format(grid[row][col]),end="")
        print("|")
        
    print("+--------------------+")
    print ()
    
    
def check_lost (grid):
    for row in range (4):
        for col in range (4):
            if grid [row][col] == 0:
                return False
            elif col >= 0:
                if grid [row][col] == grid [row][col-1]:
                    return False
            elif col <= 3:
                if grid [row][col] == grid [row][col+1]:
                    return False
                
            elif row >= 0:
                if grid [row][col] == grid [row-1][col]:
                    return False
            elif row <=3:
                if grid [row][col] == grid [row+1][col]:
                    return False
                
    else:
        return True
                


                
                
                
def check_won (grid):
    for row in range (4):
        for col in range(4):
            if grid[row][col] >= 32:
                return True
            else:
                return False
            
            
def copy_grid (grid):
    gridnew = []
    for row in range (4):
        temp = []
        for col in range (4):
            temp.append(temp)
    for row in range (4):
            for col in range (4):
                gridnew[row][col] = grid [row][col]
    return gridnew


def grid_equal (grid1,grid2):
    for row in range(4):
        for col in range (4):
            if grid1[row][col] != grid2[row][col]:
                return False
            elif grid1[row][col] == grid2[row][col]:
                continue
    return True