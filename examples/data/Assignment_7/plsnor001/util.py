''' manipulates 2-dimensional arrays of size 4x4
Pilusa NOKO
April 2014'''

def create_grid(x):
     """create a 4x4 grid"""
     for i in range(4):
          x.append([0,0,0,0])
     return x
    
                        
def print_grid (grid):
     """print out a 4x4 grid in 5-width columns within a box"""
     print('+'+'-'*19+'-'+'+')#top of box
    
     for row in range(len(grid)):
          print('|',end='')
          for column in range(len(grid)):
               if grid[row][column]!=0:
                    print("{0:<5}".format(grid[row][column]),end='')
                
               else:
                    print("{0:<5}".format(' '),end='')
          print('|')
    
     print('+'+'-'*19+'-'+'+')#bottom of box
    
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    found=0 

    #counts the zeros found
    for row in range(len(grid)):
        for column in range(len(grid)):     
            if grid[row][column]==0:
                found+=1
                break
            
        #row comparison
        for column in range(len(grid)-1):
            if grid[row][column]==grid[row][column+1]:
                found+=1
            
           
    #column comparion       
    for row in range(len(grid)-1):
        for column in range(len(grid)):
            if grid[row][column]==grid[row+1][column]:
                found+=1
            
    if found==0:
        return True  
    else: return False

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    count=0
    for row in range(len(grid)):
        for column in range(len(grid)):
            if grid[row][column]>=32:
                count+=1
    if count>0:
        return True
    else:
        return False
        

def copy_grid (grid):
    """return a copy of the grid"""
    import copy
    grid2=copy.deepcopy(grid)
    return grid2

def grid_equal (grid1, grid2):
     """check if 2 grids are equal - return boolean value"""
     if grid1==grid2:
          return True
     else:
          return False
            
#grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#create_grid(grid)