"""assignment #7 question 2
Gyu Park
02 May 2014"""


def create_grid(grid):
    height = 4
    for i in range (height):
        grid.append ([0] * 4)
        
def print_grid(grid):
    for row in range(6):
            if row == 0 or  row == 5 :
                print("+--------------------+")
            else:
                row = row-1
                for col in range(22):
                    if col == 0:
                        print("|",end='')
                    elif col == 21:
                        print("|")
                    elif col == 1 or col == 6 or col == 11 or col == 16:
                        if col == 1 :
                            col = 0
                        elif col == 6:
                            col = 1
                        elif col == 11:
                            col = 2
                        elif col == 16:
                            col = 3
                        spacing = 5 - len(str(grid[row][col]))
                        if (grid[row][col]) == 0:
                            grid[row][col] = " "
                            print(grid[row][col]," "*spacing,sep = '',end='')
                        else:
                            print(grid[row][col]," "*spacing,sep = '',end='')
                    else:
                        print("",end='')

                    
def check_lost(grid):
    newgrid = []
    for row in range(4):
        for col in range(4):
            newgrid.append(grid[row][col])
    X = True
    for i in range(len(newgrid)):
        if newgrid[i] == 0:
            return False
        elif newgrid[i-1] == newgrid[i]:
            return False
        else:
            X = True
    return X
                            
                            
        
    

def check_won(grid):
    for row in range(4):
        for col in range(4):
            if grid[row][col] < 32:
                X = False
            else:
                return True
    return X


def copy_grid(grid):
    newgrid = []
    for i in grid:
        newgrid.append(i)
    newgrid2 = newgrid
    return(newgrid2)



def grid_equal(grid1, grid2):
    X = False
    for row in range(4):
        for col in range(4):
            while grid1[row][col] == grid2[row][col]:
                X = True
                return X
            return False
                
                
