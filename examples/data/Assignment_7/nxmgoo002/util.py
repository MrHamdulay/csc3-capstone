'''this program manipulate 2-dimensional arrays of size 4x4
Nxumalo Goodman
27 April 2014'''


grid=[]
#create a 4x4 grid
def create_grid(grid):
    grid_list = []
    for i in range(4):
        grid_list.append ([' ']*4)
    #returns a 4x4 grid    
    return grid_list
   
grid = create_grid(grid)
#prints a 4x4 grid in a box with a width of 5
def print_grid(grid):
    print('+'+'-'*20+'+')
    
    for row in range(4):
        print('|',end='')
        
        for colm in range(4):
            if grid[row][colm] == 0:
                            grid[row][colm] = ' '           
            center = (' ' * (5-len(str(grid[row][colm]))))
            print(grid[row][colm],center,sep='',end = '')
            
        print('|',end ='')
        print()
    print('+'+'-'*20+'+')            
    

grid = (create_grid(grid))

#checks if the player has lost
def check_lost(grid):
    for a in range(3):
            for b in range(4):
                if grid[a][b]== 0:
                    
                    return False
     #checks if there are any adjacents equal   
    for a in range(4):
        for b in range(3):
            if grid[a][b]== grid[a][b+1] or grid[a][b]== grid[a][b-1]:
                
                return True
            
            elif grid[a][b]== grid[a+1][b] or grid[a][b] == grid[a-1][b]:
                return True
            else:
                return False    

#checks if the player has won
def check_won(grid):
    blank = 0
    for a in grid:
        for b in a:
            if b > blank:
                blank = b
        if blank >= 32:
            return True
        
        else:
            return False    

#makes a copy of the original grid
def copy_grid(grid):
    another_grid = []
    for j in grid:
        another_grid.append(j)
    #returns the copy of the grid   
    return another_grid

grid1 = grid

#checks if the first grid is equal to the second grid
def grid_equal(grid1,grid2):
    for row in range(4):
        for colm in range(4):
            #iterates through row and colm to check if they are equal 
            if grid2[row][colm] == grid1[row][colm]:
                return True
            else:
                return False