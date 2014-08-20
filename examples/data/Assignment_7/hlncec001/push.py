#HLNCEC001
#Assignment7
#push.py

def pushItems(l):
    numberOfpush = l.count(0)
    #get the number of zeros and then move values according to numberOfpush
    if numberOfpush != 4:
        for loop in range(numberOfpush):
            for i in range(len(l)-1):
                if l[i] == 0:
                    l[i] = l[i+1]
                    l[i+1] -= l[i+1]
                    i = 0
    return l

def addItems(l):
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            l[i] *= 2
            l[i+1] = 0
    return l

def push_up (grid):
    """merge grid values upwards"""
    tmpList = []
    for column in range(4):
            for row in range(4):
                tmpList.append(grid[row][column])
            pushItems(tmpList)
            addItems(tmpList)
            pushItems(tmpList)
            for k in range(4):
                grid[k][column] = tmpList[k]
            tmpList = []          
            
def push_down (grid):
    """merge grid values downwards"""
    tmpList = []
    for column in range(4):
        for row in range(3,-1,-1):
            tmpList.append(grid[row][column])
                    
        pushItems(tmpList)
        addItems(tmpList)
        pushItems(tmpList)
        i = 0
        for k in range(3,-1,-1):
            grid[k][column] = tmpList[i]
            i += 1
        tmpList = []              
    
       

def push_right (grid):
    """merge grid values left"""
    tmpList = []
    for row in range(4):
        for column in range(3,-1,-1):
            tmpList.append(grid[row][column])
        
        pushItems(tmpList)
        addItems(tmpList)
        pushItems(tmpList)
        i = 0
        for k in range(3,-1,-1):
            grid[row][k] = tmpList[i]
            i += 1
        tmpList = []
    
    

def push_left (grid):
    """merge grid values right"""
    tmpList = []
    for row in range(4):
        for column in range(4):
            tmpList.append(grid[row][column])
        
        pushItems(tmpList)
        addItems(tmpList)
        pushItems(tmpList)
        for k in range(4):
            grid[row][k] = tmpList[k]
        tmpList = []