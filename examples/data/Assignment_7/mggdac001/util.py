def create_grid(grid):
        for i in range (4):
                grid.append([0]*4)
                
        

def print_grid(grid):
        print('+--------------------+')
        number=4
        format_g='{0:<5}'
        for x in range(4):
                for y in range (4):
                        if number%4 ==0:
                                print('|',end='')
                        if grid[x][y]==0:
                                print(format_g.format(' '),end='')
                        else:
                                print(format_g.format(grid[x][y]),end='')
                                
                        number+=1
                        
                print('|',end='')
                print()
        print('+--------------------+')
        
def check_won (grid):
        """return True if a value>=32 is found in the grid; otherwise False"""
        for x in range(4):
                for y in range (4):
                        if grid[x][y]>32:
                                return True
                        return False
                                
def check_lost (grid):
        """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
        for x in range(4):
                for y in range (4):
                        if grid[x][y] !=0 and grid[x][y] != grid[x][y+1]:
                                return True 
                        return False
def copy_grid (grid):
        """return a copy of the grid"""
        
def copy_grid(grid):
        for i in range(len(grid)):
                for i in range(len(grid)):
                        return grid
def grid_equal(grid1, grid2):
        for t in range(4):
                for u in range(4):
                        if grid1==grid2:
                                return True
                        return False
                
        
                     

        
        
   

    
