"""functions to be used in 2048
clare walker
27 apri 2014"""
import util
grid=[]
def push_up (grid):
    """merge grid values upwards"""
    
    newgrid=[]
    for row in range(4):    #new empty array
        newgrid.append([0]*4)
        
    for col in range(4):    #new array with values in column
        values=[]
        for row in range(4):    #eliminate 0s
            if grid[row][col] != 0:
                values.append(grid[row][col])
        merged=[]       
        if len(values)==4: #merge adjacent values sequentially
            if values[3]==values[2]:
                merged.append(values[3]*2)
                if values[1]==values[0]:
                    merged.append(values[1]*2)
                else:
                    merged.append(values[1])
                    merged.append(values[0])
            else:
                merged.append(values[3])
                if values[2]==values[1]:
                    merged.append(values[2]*2)
                    merged.append(values[0])
                else:
                    merged.append(values[2])
                    if values[1]==values[0]:
                        merged.append(values[0]*2)
                    else:
                        merged.append(values[1])
                        merged.append(values[0])
        elif len(values)==3:
            if values[2]==values[1]:
                merged.append(values[2]*2)
                merged.append(values[0])
            else:
                merged.append(values[2])
                if values[1]==values[0]:
                    merged.append(values[1]*2)
                    
                else:
                    merged.append(values[1])
                    merged.append(values[0])
        elif len(values)==2:
            if values[1]==values[0]:
                merged.append(values[1]*2)
            else:
                merged.append(values[1])
                merged.append(values[0])
        elif len(values)==1:
            merged.append(values[0])
        
        merged.reverse()             #reverse merged as new values had been added at end
        for i in range(len(merged)):
            newgrid[i][col] = merged[i] #add merged values to corresponding point in new grid
    for row in range(4): #copy newgrid values to grid
        for col in range(4):
            grid[row][col] = newgrid[row][col]
    return grid
    
 # other functions used same methods as push up, comments are used where it differs
 
def push_down (grid):
    """merge grid values downwards"""        
    newgrid=[]  
    for row in range(4):
        newgrid.append([0]*4)
        
    for col in range(4):
        values=[]
        for row in range(4):
            if grid[row][col] != 0:
                values.append(grid[row][col])
       
        merged=[]       
        if len(values)==4:
            if values[0]==values[1]:
                merged.append(values[0]*2)
                if values[2]==values[3]:
                    merged.append(values[2]*2)
                else:
                    merged.append(values[2])
                    merged.append(values[3])
            else:
                merged.append(values[0])
                if values[1]==values[2]:
                    merged.append(values[1]*2)
                    merged.append(values[3])
                else:
                    merged.append(values[1])
                    if values[2]==values[3]:
                        merged.append(values[2]*2)
                    else:
                        merged.append(values[2])
                        merged.append(values[3])
        elif len(values)==3:
            if values[0]==values[1]:
                merged.append(values[0]*2)
                merged.append(values[2])
            else:
                merged.append(values[0])
                if values[1]==values[2]:
                    merged.append(values[2]*2)
                    
                else:
                    merged.append(values[1])
                    merged.append(values[2])
        elif len(values)==2:
            if values[1]==values[0]:
                merged.append(values[1]*2)
            else:
                merged.append(values[0])
                merged.append(values[1])
        elif len(values)==1:
            merged.append(values[0])
                    
# add merged to new grid from bottom to top row
        j=3
        i=len(merged)-1
        while i >= 0:
            newgrid[j][col]=merged[i]
            j-=1
            i-=1
    for row in range(4):
        for col in range(4):
            grid[row][col] = newgrid[row][col]
    return grid

def push_left (grid):
    """merge grid values leftwards"""
    newgrid=[]
    for row in range(4):
        newgrid.append([0]*4)
        
    for row in range(4):
        values=[]
        v=grid[row]     # values, unedited, are simply all values in row
        for i in v:
            if i!= 0:
                values.append(i)
        merged=[]       
        if len(values)==4:
            if values[3]==values[2]:
                merged.append(values[3]*2)
                if values[1]==values[0]:
                    merged.append(values[1]*2)
                else:
                    merged.append(values[1])
                    merged.append(values[0])
            else:
                merged.append(values[3])
                if values[2]==values[1]:
                    merged.append(values[2]*2)
                    merged.append(values[0])
                else:
                    merged.append(values[2])
                    if values[1]==values[0]:
                        merged.append(values[0]*2)
                    else:
                        merged.append(values[1])
                        merged.append(values[0])
        elif len(values)==3:
            if values[2]==values[1]:
                merged.append(values[2]*2)
                merged.append(values[0])
            else:
                merged.append(values[2])
                if values[1]==values[0]:
                    merged.append(values[1]*2)
                    
                else:
                    merged.append(values[1])
                    merged.append(values[0])
        elif len(values)==2:
            if values[1]==values[0]:
                merged.append(values[1]*2)
            else:
                merged.append(values[1])
                merged.append(values[0])
        elif len(values)==1:
            merged.append(values[0])
        merged.reverse()             
                
      
        for i in range(len(merged)):
            newgrid[row][i] = merged[i]
    for row in range(4):
        for col in range(4):
            grid[row][col] = newgrid[row][col]
    return grid

def push_right (grid):
    """merge grid values right"""        
    newgrid=[]
    for row in range(4):
        newgrid.append([0]*4)
        
    for row in range(4):
        values=[]
        v=grid[row]
        for i in v:
            if i!= 0:
                values.append(i)

        merged=[]       
        if len(values)==4:
            if values[0]==values[1]:
                merged.append(values[0]*2)
                if values[2]==values[3]:
                    merged.append(values[2]*2)
                else:
                    merged.append(values[2])
                    merged.append(values[3])
            else:
                merged.append(values[0])
                if values[1]==values[2]:
                    merged.append(values[1]*2)
                    merged.append(values[3])
                else:
                    merged.append(values[1])
                    if values[2]==values[3]:
                        merged.append(values[2]*2)
                    else:
                        merged.append(values[2])
                        merged.append(values[3])
        elif len(values)==3:
            if values[0]==values[1]:
                merged.append(values[0]*2)
                merged.append(values[2])
            else:
                merged.append(values[0])
                if values[1]==values[2]:
                    merged.append(values[2]*2)
                    
                else:
                    merged.append(values[1])
                    merged.append(values[2])
        elif len(values)==2:
            if values[1]==values[0]:
                merged.append(values[1]*2)
            else:
                merged.append(values[0])
                merged.append(values[1])
        elif len(values)==1:
            merged.append(values[0])
                    
        
       
       
        j=3
        i=len(merged)-1
        while i >= 0:
            newgrid[row][j]=merged[i]
            j-=1
            i-=1
     
    for row in range(4):
        for col in range(4):
            grid[row][col] = newgrid[row][col]
    return grid