import copy
def create_grid(grid):
    for i in range(4):
            grid.append ([0] * 4)
    return(grid)

def print_grid(grid):
    print("+--------------------+")
    for row in range(4):
        for col in range(4):
            a=grid[row][col]
            output='{0:<5}'
            if col==0:
                output='|{0:<5}'
            if a ==0:
                grid[row][col]=' '
            print(output.format(grid[row][col]),end='')
            if a ==0:
                grid[row][col]=0

        print('|')        
    print("+--------------------+")

#print_grid([[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]])
        
def check_lost(grid):
    lost=True
    for row in range(4):
        if 0 in grid[row]:
            lost=False
            break
        for col in range(4):
            a=grid[row][col]
            for i in range(4):
                b=grid[row][i]
                c=grid[i][col]
                if a==b and col!=i:
                    if col==i+1 or col==i-1:
                        lost=False
                        break
                if a==c and row!=i:
                    if row==i+1 or row==i-1:
                        lost=False
                        break
            if lost==False:
                break
    return(lost)

def check_won(grid):
    won=False
    for row in range(4):
        for col in range(4):
            if grid[row][col]>=32:
                won=True
                break
        if won==True:
            break
    return(won)


def copy_grid(grid):
    gridcopy=copy.deepcopy(grid)
    return(gridcopy)


def grid_equal(grid1,grid2):
    if grid1==grid2:
        return(True)
    else:
        return(False)
    


        
#print(copy_grid("[[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]]"))
#print_grid([[2,4,2,5],[4,6,9,8],[3,16,8,128],[2,6,9,3]])
#print(check_lost([[2,4,2,5],[4,6,9,8],[3,16,8,128],[2,6,9,3]]))
#print(check_won([[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]]))
