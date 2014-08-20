import util
def push_left(grid):
    rgrid = [[],[],[],[]]
    for num in range(4):
    
        sgrid = [x for x in grid[num] if x is not 0]
        for i in range(4-len(sgrid)):
            sgrid.append(0)

        for i in range (1,4):
            if sgrid[i] == sgrid [i-1]:
                sgrid[i-1] = sgrid[i]*2
                sgrid[i] = 0
        
        sgrid = [x for x in sgrid if x is not 0]
        for i in range(4-len(sgrid)):
            sgrid.append(0)

        rgrid[num] = sgrid
    for i in range(4):
        grid[i] = rgrid[i]
    return rgrid

def push_right(grid):
    rgrid = [[],[],[],[]]
    returngrid = [[],[],[],[]]
    zero = [[],[],[],[]]
    for num in range(4):
        sgrid = [x for x in grid[num] if x is not 0]
        rgrid[num] = [0]*(4-len(sgrid))
        for i in range(len(sgrid)):
            rgrid[num].append(sgrid[i])
            
        for i in range (2,-1, -1):
            
            if rgrid[num][i] == rgrid[num] [i+1]:
                rgrid[num][i+1] = rgrid[num][i]*2
                rgrid[num][i] = 0
        zero[num] = [x for x in rgrid[num] if x is not 0]
        
        returngrid[num] = [0]*(4-len(zero[num]))
        for i in range(len(zero[num])):
            returngrid[num].append(zero[num][i])
            
                       
                       
    for i in range(4):
        grid[i] = returngrid[i]
    return returngrid
    
    


def push_up(grid):
    returngrid = [[],[],[],[]]
    sgrid = [[],[],[],[]]

    for i in range(4):
        for j in range(4):
            sgrid[i].append(grid[j][i])
    
    
    sgrid = push_left(sgrid)
    for i in range(4):
        for j in range(4):
            returngrid[i].append(sgrid[j][i])
    for i in range(4):
        
        grid[i] = returngrid[i]
    

def push_down(grid):
    
    returngrid = [[],[],[],[]]
    sgrid = [[],[],[],[]]
    temp = [[],[],[],[]]

    for i in range(4):
        for j in range(4):
            sgrid[i].append(grid[j][i])
    
    
    sgrid = push_right(sgrid)
    
    for i in range(4):
        for j in range(4):
            returngrid[i].append(sgrid[j][i])
            
    for i in range(4):
        grid[i] = returngrid[i]
    
        
        
    

        
        
        
 

        

        
        
        
        

    
    




