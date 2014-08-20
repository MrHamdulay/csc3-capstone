'''program that merges adjacent equal values and eliminate gaps 
sankara mallane
27 april 2014'''

# function to push elements
def push (line): 
    
    for a in range (3):# for loop through the elements in the list
        for i in range(3):#loops through the first 3 elements in the list
            if line[i]==0: # if the element is zero 
                line[i]=line[i+1] # shift one unit to the right
                line[i+1]=0
     
    for i in range (3):  #for loops through the first 3 elements in the list
        if line[i]==line[i+1]:# checks if elements there are matching elements
            line[i]=line[i]*2 # multiply the element if they match by 2
            line[i+1]=0 # the right element then equals to 0
    
    for a in range (3): # for loop through the elements in the list
        for i in range(3):# loops through the first 3 elements in the list
            if line[i]==0: # shift the elements to the left
                line[i]=line[i+1] # to leave spaces
                line[i+1]=0   

#merge values upwards
def push_up (grid):
    
    for a in range(4):# Loops through the column in the list
        line=[] # empty list
        for b in range(4):# for loop to go through elements in column
            line.append(grid[b][a]) # add elements to the array
            
        push(line)# function that pushes the line
        
        for c in range(4):#for loop to replace the value in the grid   
            grid[c][a]=line[c]#to the matching value in the array that has been shifted

#merge grid values downwards
def push_down (grid):
    
    for a in range(4):#Loops through the column in the list
        
        line =[] # empty list
        
        for b in range (3,-1,-1):# for loop that is the reverse of push_up
            line.append(grid[b][a]) # add elements to array
            
        push(line)# function that pushes the line
        
        for c in range(3,-1,-1):#for loop to replace the value in the grid
            grid[c][a]=line[3-c]#to the matching value in the array that has been shifted

#merge grid values left
def push_left (grid):
    
    for a in range(4):#Loops through each row in the list
        
        line=[] # empty list
        
        for b in range(4):# for loop to go through elements in row 
            line.append(grid[a][b]) # add elements to array
            
        push(line)# function that pushes the line
        
        for c in range(4):#for loop to replace the value in the grid 
            grid[a][c]=line[c] #to the matching value in the array that has been shifted

#merge grid values right
def push_right (grid):
    
    for a in range(4):#Loops through each row in the list
        
        line =[] # empty list
        
        for b in range (3,-1,-1):# for loop that is the reverse of push_left
            line.append(grid[a][b])# add elements to array
            
        push(line) #function that pushes the line
        
        for c in range(3,-1,-1):#for loop to replace the value in the grid 
            grid[a][c]=line[3-c]#to the matching value in the array that has been shifted

 
        
    
            
        