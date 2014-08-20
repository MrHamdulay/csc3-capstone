#This is push.py, moving and combining blocks
#Hendrik Joosten
#2 may 2014 

# this is by far the hardest piece of code ive ever written
# i tried 3 different mehods, the failed methods have been added at the bottom
# this one works but NOT as efficiently as i would have liked it to

#NOTE: i should be possible to only have ONE written method here and the manipulate
# the grid pre input to this method so that it has the correct output
# like what i did with push up and push down
# except with connecting push up with all other methods



def push_up (grid):
    """merge grid values upwards"""  
    # go through grid column by column
    for z in range(4):
        # working with one column at a time
        col = [0,0,0,0]
        # unique values used to move the original values
        unique = []
        
        # take all the values in one column and puts them in a list
        for a in range(4):
            col[a] = grid[a][z]
        # BUILD A BUFFER INTO THE LIST TO MAKE CHECKING EQUELNESS EASIER
        col.append(0)
        col.append(0)
        col.append(0)
        # checks equalness
        for b in  range(3):
            if col[b] == col[b+1]:
                col[b] = 2*(int(col[b]))
                col[b+1] = 0
                
            elif col[b] == col[b+2] and col[b+1] == 0:
                col[b] = 2*(int(col[b]))
                col[b+2] = 0                      
                
            elif col[b] == col[b+3] and col[b+2] == 0 and col[b+1] == 0:
                col[b] = 2*(int(col[b]))
                col[b+3] = 0                 
        #take nonzero items out of the list
        for c in range(4):
            if col[c] != 0:
                unique.append(int(col[c]))
                col[c] = 0     
        # replace nonzero items from left to right in list
        for d in range(len(unique)):
            col[d] = unique[d]
            #return the manipulated values to the column in the grid
        for e in range(4):
            grid[e][z] = col[e]
    return grid
        

def push_down (grid):
    """merge grid values downwards"""
    #turn grid upside down
    #run it through push up
    #turn grid back the right way again
    grid = grid[::-1]
    push_up(grid)
    grid = grid[::-1]
    return grid
    

def push_left (grid):
    """merge grid values left"""
    
    # this method uses the same logic as push up
    for z in range(4):
        row = [0,0,0,0]
        unique = []
        row = grid[z]
        row.append(0)
        row.append(0)
        row.append(0)
        
        for a in range(3):
            if row[a] == row[a+1]:
                row[a] = 2*(int(row[a]))
                row[a+1] = 0
            elif row[a] == row[a+2] and row[a+1] == 0:
                row[a] = 2*(int(row[a]))
                row[a+2] = 0                      
            elif row[a] == row[a+3] and row[a+2] == 0 and row[a+1] == 0:
                row[a] = 2*(int(row[a]))
                row[a+3] = 0 
                    
        for b in range(4):
            if row[b] != 0:
                unique.append(int(row[b]))
                row[b] = 0
                
        for c in range(len(unique)):
            row[c] = unique[c] 
            
        grid[z] = row[:4]
    return grid

        
def push_right (grid):
    """merge grid values right"""
    #reverse the lists inside the grid
    # run it through push left
    # retrun the inner list to thei original positons
    for a in range(4):
        grid[a] = (grid[a])[::-1]
    push_left(grid)
    for a in range(4):
        grid[a] = (grid[a])[::-1]
    return grid



          
"""MY FIRST ATTEMPT"""                
#if a == 1:
#if grid[a-1][b] == 0:
#if grid[a][b] == 0:
#if grid[a+1][b] == 0:
#grid[a-1][b] = grid[a+2][b]
#grid[a+2][b] = 0
#grid[a-1][b] = grid[a+1][b]
#grid[a+1][b] = 0
#grid[a-1][b] = grid[a][b]
#grid[a][b] = 0
#if a == 2:
#if grid[a-1][b] == 0:
#if grid[a][b] == 0:
#grid[a-1][b] = grid[a+1][b]
#grid[a+1][b] = 0
#grid[a-1][b] = grid[a][b]  
#grid[a][b] = 0
#if a == 3:
#if grid[a-1][b] == 0:
#grid[a-1][b] = grid[a][b]
#grid[a][b] = 0
                        
                        
"""MY SECOND ATTEMPT"""                      
#for a in range(1,4):
#if grid[a][b] == grid[a-1][b]:
#grid[a-1][b] = 2*(int(grid[a-1][b]))
#grid[a][b] = 0
#for c in range(4):
#column = []  
#if grid[c][b] != 0:
#column.append(grid[c][b])
#grid[c][b] = 0
#for d in range(len(column)):
#grid[d][b] = column[d]

         

  
