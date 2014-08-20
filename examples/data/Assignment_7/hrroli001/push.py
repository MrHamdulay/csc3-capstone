# Question 3 - Assignment 7
# Oliver Harrison
# 30 April 2014



def push_up (grid):
    """merge grid values upwards"""
    #global grid
    # remove zeros
    
    # create new grid
    newgrid = []
    for i in range(4):
        newgrid.append([])
        
    
    for x in range(4):
        row = 0
        for y in range(4):
            if grid[y][x] == 0:
                continue
            else:
                if row !=0 and grid[y][x] == newgrid[row-1][x]:
                    newgrid[row-1][x] += grid[y][x]
                    
                else:
                    newgrid[row].insert(x, grid[y][x])
                    row = row+1
        for zeros in range(row, 4):
            newgrid[zeros].insert(x, 0)
    
    for i in range(4):
        for j in range(4):
            grid[i][j] = newgrid[i][j]
            
  
    

   
    #print(newgrid)
    
    
    

#print(push_up([[0,0,0,0],[0,2,0,0],[0,0,0,0],[0,0,0,0]]))
#print(grid)
#push_up([[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]])
#push_up([[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]]) 
            
            
    
    
    
    
       
# add
"""for row in range(1, 4):              
    for col in range(4):
        if grid[row-1][col] == grid[row][col]:
            grid[row-1][col] += grid[row][col]
            grid[row][col] = 0
            
        else:
            continue

# take out zero's
for row in range(1, 4):                
    for col in range(4):
        if grid[row-1][col] == 0:
            grid[row-1][col] = grid[row][col]
            grid[row][col] = 0
        else:
            continue    
        print(grid)"""


            
                       

                
                
                
                
                


def push_down (grid):
    """merge grid values downwards"""
    
    # add
    
    """for row in range(1, 4):              
        for col in range(4):
            if grid[row-1][col] == grid[row][col]:
                grid[row-1][col] += grid[row][col]
                grid[row][col] = 0
                
            else:
                continue"""
    
    # remove zeros
    
    # create new grid
    newgrid = []
    for i in range(4):
        newgrid.append([])
        
    
    for x in range(4):
        row = 3
        for y in range(3,-1,-1):
            if grid[y][x] == 0:
                continue
            else:
                if row !=3 and grid[y][x] == newgrid[row+1][x]:
                    newgrid[row+1][x] += grid[y][x]
                    
                else:
                    newgrid[row].insert(x, grid[y][x])
                    row = row-1
        for zeros in range(4 - (3-row)):
            newgrid[zeros].append(0)
            
    for i in range(4):
        for j in range(4):
            grid[i][j] = newgrid[i][j]
            
            
    # add numbers            
    """for x in range(4):
        for y in range(3,0,-1):
            if newgrid[y][x] == newgrid[y-1][x]:
                newgrid[y][x] += newgrid[y-1][x]"""


    
    #print(newgrid)
                
#push_down([[0,0,0,0],[0,2,0,0],[0,0,0,0],[0,0,0,0]])
#push_down([[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]])
#push_down([[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]])

def push_left (grid):
    """merge grid values left"""
    
    # eliminate zeros
    newgrid = []
    for y in range(4):
        newgrid.append([])
        for x in range(4):
            if grid[y][x] == 0:
                continue
            else:
                newgrid[y].append(grid[y][x])

        for zeros in range(4 - len(newgrid[y])):
            newgrid[y].append(0)   

    # add
    for y in range(4):
        for x in range(1, 4):
            if newgrid[y][x-1] == newgrid[y][x]:
                newgrid[y][x-1] += newgrid[y][x]
                del newgrid[y][x]                 # delete one of adding numbers
                newgrid[y].append(0)              # add 0 to end of list
                

    for i in range(4):
        for j in range(4):
            grid[i][j] = newgrid[i][j]    

    #print(newgrid)
             
#push_left([[0,0,0,0],[0,2,0,0],[0,0,0,0],[0,0,0,0]])
#push_left([[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]])
#push_left([[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]])
                

def push_right (grid):
    """merge grid values right""" 
    
    # eliminate zeros
    newgrid = []
    for y in range(4):
        newgrid.append([])
        for x in range(3,-1,-1):
            if grid[y][x] == 0:
                continue
            else:
                newgrid[y].insert(0, grid[y][x])

        for zeros in range(4 - len(newgrid[y])):
            newgrid[y].insert(0,0)   

    # add
    for y in range(4):
        for x in range(2,-1,-1):
            if newgrid[y][x+1] == newgrid[y][x]:
                newgrid[y][x+1] += newgrid[y][x]
                del newgrid[y][x]                 # delete one of adding numbers
                newgrid[y].insert(0,0)              # add 0 to start of list
            
    for i in range(4):
        for j in range(4):
            grid[i][j] = newgrid[i][j]
    #print(newgrid)
             
#push_right([[0,0,0,0],[0,2,0,0],[0,0,0,0],[0,0,0,0]])
#push_right([[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]])
#push_right([[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]])
    