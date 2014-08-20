
#creating set of merging functions that merge adjacent equal values and eliminate gaps 
#KNNSAD001
#Assignment 7


#function to add values above in grid
def push_up(grid):    
    new_grid=[]         
    temp_grid=[]  
#this adds the first,second,third and fourth numbers in every list to a temporary variable,respectively
    for number in grid:     
        temp_grid.append(number[0])
    temporary_grid=[]
    

    for number in grid:      
        temporary_grid.append(number[1])
    new_grid2=[]

    for number in grid:       
        new_grid2.append(number[2])
    last_grid=[]
   
    for number in grid:      
        last_grid.append(number[3])
    new_grid.append(temp_grid)
#adds all temporary lists into new variable list
    new_grid.append(temporary_grid)     
    new_grid.append(new_grid2)
    new_grid.append(last_grid)
#adds all values in new variable list to the left
    new_grid=push_left(new_grid)    
    addition=0
    while addition < 4:
#replaces first,second,third and fourth number in each list in grid with the first list in the new variable grid,respectively
        for number in grid:       
            number[0]=new_grid[0][addition]
            addition+=1
    addition1=0

    while addition1<4:    
        for number in grid:
            number[1]=new_grid[1][addition1]
            addition1+=1
    addition2=0

    while addition2<4:     
        for number in grid:
            number[2]=new_grid[2][addition2]
            addition2+=1
    addition3=0

    while addition3<4:     
        for number in grid:
            number[3]=new_grid[3][addition3]
            addition3+=1
            
    return grid
            
#function adds values in the grid downwards    
def push_down(grid):        
    new_grid=[]             
    temp_grid=[]       
#adds first,second,third and fourth number in every list in grid to the temporary list,respectively
    for number in grid:       
        temp_grid.append(number[0])
    temporary_grid=[]

    for number in grid:       
        temporary_grid.append(number[1])
    new_grid2=[]

    for number in grid:     
        new_grid2.append(number[2])
    last_grid=[]

    for number in grid:       
        last_grid.append(number[3])
    new_grid.append(temp_grid)
    new_grid.append(temporary_grid)
#adds temporary variables into new variable grid
    new_grid.append(new_grid2)    
    new_grid.append(last_grid)
#adds values in new variable grid to the right
    new_grid=push_right(new_grid)   
    addition=0
    while addition<4:
#replaces first,second,third and fourth number in each list in grid with the first list in the new variable grid,respectively
        for number in grid:      
            number[0]=new_grid[0][addition]
            addition+=1
    addition1=0

    while addition1<4:    
        for number in grid:
            number[1]=new_grid[1][addition1]
            addition1+=1
    addition2=0

    while addition2<4:     
        for number in grid:
            number[2]=new_grid[2][addition2]
            addition2+=1
    addition3=0

    while addition3<4:     
        for number in grid:
            number[3]=new_grid[3][addition3]
            addition3+=1
                
    return grid  

#function to move all values left              
def push_left(grid):       
    i=1
#removes all 0 values to the left
    while i<4:              
        for number in grid:
            
            number.append(0)      
            for i in range(4):
                if number[i]==0:
                    number[i]=number[i+1]
                    number[i+1]=0
            number.remove(number[4])        
        i+=1
    #adds values to the left
    for item in grid:         
        item.append(0)
        for i in range(4):
            if item[i]==item[i+1]:
                item[i]*=2
                item[i+1]=0
        item.remove(item[4])
    j=1
    #removes 0 values from addition
    while j<4:                  
        for number in grid:
            number.append(0)
            for i in range(4):
                if number[i]==0:
                    number[i]=number[i+1]
                    number[i+1]=0
            number.remove(number[4])
        j+=1
               
    return grid  

#function to add values to the right
def push_right(grid):       
    addition=1
    #removes all 0 values to the right
    while addition<4:         
        for number in grid:
           
            number.insert(0, 0)   
            for i in range(-4, 0):
                if number[-i]==0:
                    number[-i]=number[-i-1]
                    number[-i-1]=0
            number.remove(number[0])    
        addition+=1
    #addition of numbers to the right
    for item in grid:             
        item.insert(0,0)
        for i in range(-4, 0):
            if item[-i]==item[-i-1]:
                item[-i]*=2
                item[-i-1]=0
        item.remove(item[0])
    addition1=1
    #removes all 0 values from addition
    while addition1<4:             
        for number in grid:
            number.insert(0, 0)
            for i in range(-4, 0):
                if number[-i]==0:
                    number[-i]=number[-i-1]
                    number[-i-1]=0
            number.remove(number[0])
        addition1+=1
    return grid    