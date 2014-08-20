"""creating heart of 2048
James Cushway
27-04-2014"""
#creating a grid
def create_grid(grid):
    
    for i in range(4):
        grid.append([0,0,0,0])
    return grid
#printing a grid
def print_grid(grid):
    print('+--------------------+')
    for row in range(4):
        print('|',end='')
        for col in range(4):
            if grid[row][col]!=0:
                print("{0:<5}".format(grid[row][col]),sep='',end='')
            else:
                print("{0:<5}".format(' '),sep='',end='')
        print('|')
    print('+--------------------+')
#checking if you lost the game
def check_lost(grid):
    count=0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==0:
                count+=1
            if grid[i][j]==grid[i][j-1]:
                count+=1
    if count>0:
        return False
    else:
        return True
    
 #checking if you have won the game          
def check_won(grid):
    count=0
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                count+=1
    if count>0:
        return True
    else:
        return False
    
#copying the grid
def copy_grid(grid):
    new_grid=[[]for i in range(4)]
    for y in range (4):
        for x in range (4):
            new_grid[y].append(grid[y][x])
    return new_grid

#checking if two grids are equal
def grid_equal(grid1,grid2):
    count=0
    for i in range (4):
        for j in range (4):
            if grid1[i][j]==grid2[i][j]:
                count+=1
    if count==16:
        return True
    else:
        return False
           
            
    
            
            
            
        
 
                
            
    
       