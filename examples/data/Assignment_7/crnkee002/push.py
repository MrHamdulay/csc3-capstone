"""A7Q3 - Move the grid
01/05/2014
CRNKEE002"""  

def push_up (grid):
    """merge grid values upwards"""
    newgrid = []
   #get the "minigrid" 
    for x in range(4):
        temp = []       
        for y in range(4):
            temp.append(grid[y][x]) 
       #remove zeroes     
        for i in range(4)[::-1]:
            if temp[i] == 0:
                del(temp[i])   
       #add the values 
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1]:
                temp[i] = temp[i]*2
                temp[i+1] = 0    
       #remove zeroes     
        for i in range(len(temp)-1)[::-1]:
            if i >= 0:
                if temp[i] == 0:
                    del(temp[i])          
       #add zeroes as fillers 
        for i in range(4-(len(temp))):
            temp.append(0)  
            
        newgrid.append(temp)      
    for x in range(4):
        for y in range(4):
            grid[x][y] = newgrid[y][x]

def push_down (grid):
    """merge grid values downwards"""
    """merge grid values right"""
    newgrid = []
   #get the "minigrid" 
    for x in range(4):
        temp = []       
        for y in range(4):
            temp.append(grid[y][x]) 
       #remove zeroes     
        for i in range(4)[::-1]:
            if i >= 0:
                if temp[i] == 0:
                    del(temp[i])   
       #add the values 
        for i in range(len(temp)-1)[::-1]:
            if temp[i] == temp[i+1]:
                temp[i+1] = temp[i]*2
                temp[i] = 0
            else:
                pass
       #remove zeroes     
        for i in range(len(temp)-1)[::-1]:
            if i >= 0:
                if temp[i] == 0:
                    del(temp[i])          
       #add zeroes as fillers 
        while len(temp) != 4:
            temp.insert(0,0)
            
        newgrid.append(temp)      
    for x in range(4):
        for y in range(4):
            grid[x][y] = newgrid[y][x]
    
                                
def push_left (grid):
    """merge grid values left"""
    newgrid = []
   #get the "minigrid" 
    for x in range(4):
        temp = []       
        for y in range(4):
            temp.append(grid[x][y]) 
       #remove zeroes     
        for i in range(4)[::-1]:
            if temp[i] == 0:
                del(temp[i])   
       #add the values 
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1]:
                temp[i] = temp[i]*2
                temp[i+1] = 0    
       #remove zeroes     
        for i in range(len(temp)-1)[::-1]:
            if i >= 0:
                if temp[i] == 0:
                    del(temp[i])          
       #add zeroes as fillers 
        for i in range(4-(len(temp))):
            temp.append(0)  
            
        newgrid.append(temp)      
    for x in range(4):
        for y in range(4):
            grid[x][y] = newgrid[x][y]
        

def push_right (grid):
    """merge grid values right"""
    newgrid = []
   #get the "minigrid" 
    for x in range(4):
        temp = []       
        for y in range(4):
            temp.append(grid[x][y]) 
       #remove zeroes     
        for i in range(4)[::-1]:
            if i >= 0:
                if temp[i] == 0:
                    del(temp[i])   
       #add the values 
        for i in range(len(temp)-1)[::-1]:
            if temp[i] == temp[i+1]:
                temp[i+1] = temp[i]*2
                temp[i] = 0
            else:
                pass
       #remove zeroes     
        for i in range(len(temp)-1)[::-1]:
            if i >= 0:
                if temp[i] == 0:
                    del(temp[i])          
       #add zeroes as fillers 
        while len(temp) != 4:
            temp.insert(0,0)
            
        newgrid.append(temp)      
    for x in range(4):
        for y in range(4):
            grid[x][y] = newgrid[x][y]   
                                