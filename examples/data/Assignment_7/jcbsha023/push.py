#Program for merging numbers left right up and down
#Anthony Jacob
#02 May 2014

def push_up (grid): #merge grid values upwards
    for x in range(4):
        line=[]
        for y in range(4):#Going through every value in column (Top to bottom) and add to new array
            line.append(grid[y][x])
            
        push(line)#Push the line
        
        for z in range(4):#Change value of grid in column x to the corresponding value in shifted array(line)
            grid[z][x]=line[z]

def push_down (grid): #merge grid values downwards
    for x in range(4):
        line =[]
        for y in range (3,-1,-1):#Going through every value in column (Bottom to top) and add to new array
            line.append(grid[y][x])
        push(line)#Push the line
        for z in range(3,-1,-1):#Change value of grid in column x to the corresponding value in shifted array(line)
            grid[z][x]=line[3-z]
        
def push_left (grid):  #merge grid values to the left
    for x in range(4):
        line=[]
        for y in range(4):#Going through each value in row (Left to right) and add to new array
            line.append(grid[x][y])
        push(line)
        for z in range(4):
            grid[x][z]=line[z]

def push_right (grid): #merge grid values right
    for x in range(4):
        line =[]
        for y in range (3,-1,-1):#Going through each value in row (right to left) and add to new array
            line.append(grid[x][y])
        push(line) #Push the line
        for z in range(3,-1,-1):
            grid[x][z]=line[3-z]

def push (line): #merging 1D array to the left    
    for x in range (3):
        for i in range(3):
            if line[i]==0:
                line[i]=line[i+1]
                line[i+1]=0
    for i in range (3): #Go through array look for matching elements next to each other if so add together and make right element equal 0
        if line[i]==line[i+1]:
            line[i]=line[i]*2
            line[i+1]=0
    
    for x in range (3):#Shift all elements left again incase some combined leaving spaces
        for i in range(3):
            if line[i]==0:
                line[i]=line[i+1]
                line[i+1]=0    
        
    
            
        