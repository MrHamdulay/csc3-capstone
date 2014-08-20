"""Program for merging numbers left right up and down
Kennedy Muranda
2 May 2014"""

#Util try 2
def push_up (grid):
    """merge grid values upwards"""
    for x in range(4):#Looping through each column
        line=[]
        for y in range(4):#Going through every value in column (Top to bottom) and add to new array
            line.append(grid[y][x])
            
        push(line)#Push the line
        
        for z in range(4):#Change value of grid in column x to the corresponding value in shifted array(line)
            grid[z][x]=line[z]

#merge grid values downwards
def push_down (grid):
    
    for x in range(4):#Looping through each column
        line =[]
        for y in range (3,-1,-1):#Going through every value in column (Bottom to top) and add to new array
            line.append(grid[y][x])
        push(line)#Push the line
        for z in range(3,-1,-1):#Change value of grid in column x to the corresponding value in shifted array(line)
            grid[z][x]=line[3-z]
        

#merge grid values left
def push_left (grid):
    
    for x in range(4):#Looping through each row 
        line=[]
        for y in range(4):#Going through each value in row (Left to right) and add to new array
            line.append(grid[x][y])
        push(line)#push the line
        for z in range(4):#Change value of grid in row x to the corresponding value in shifted array(line)
            grid[x][z]=line[z]

#merge grid values right
def push_right (grid):
    
    for x in range(4):#Looping through eah row
        line =[]
        for y in range (3,-1,-1):#Going through each value in row (right to left) and add to new array
            line.append(grid[x][y])
        push(line) #Push the line
        for z in range(3,-1,-1):#Change value of grid in row x to the corresponding value in shifted array(line)
            grid[x][z]=line[3-z]

#Function to merge a 1D array to the left
def push (line): 
    
    
    for x in range (3):#Do shifting 3 times in case element on far right
        for i in range(3):#Goes through 1st 3 elements , if one is 0 then shift one space
            if line[i]==0:
                line[i]=line[i+1]
                line[i+1]=0
     
    #Go through array look for matching elements next to each other if so add together and make right element equal 0           
    for i in range (3): 
        if line[i]==line[i+1]:
            line[i]=line[i]*2
            line[i+1]=0
    
    
    #Shift all elements left again incase some combined leaving spaces
    for x in range (3):
        for i in range(3):
            if line[i]==0:
                line[i]=line[i+1]
                line[i+1]=0    
        
    
            
        