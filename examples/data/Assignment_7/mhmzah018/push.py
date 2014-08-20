"""Assignment 7 - quesiton 3
Zaheer Mahmood
28-04-2014"""

#create function to add values above in grid
def push_up(grid):    
    new_grid=[]         
    temp_grid=[]  
 #adds first item in every list in grid to a temporary variable
    for item in grid:     
        temp_grid.append(item[0])
    t_grid=[]
    
 #adds second item in every list in grid to a temporary variable
    for item in grid:      
        t_grid.append(item[1])
    n_grid=[]
#adds third item in every list in grid to a temporary variable
    for item in grid:       
        n_grid.append(item[2])
    h_grid=[]
 #adds fourth item in every list in grid to a temporary variable   
    for item in grid:      
        h_grid.append(item[3])
    new_grid.append(temp_grid)
#adds all temporary lists into new variable list
    new_grid.append(t_grid)     
    new_grid.append(n_grid)
    new_grid.append(h_grid)
#adds all values in new variable list to the left
    new_grid=push_left(new_grid)    
    count=0
    while count < 4:
#replaces first item in each list in grid with the first list in the new variable grid
        for item in grid:       
            item[0]=new_grid[0][count]
            count+=1
    count1=0
#replaces second item in each list in grid with the second list in the new variable grid
    while count1<4:    
        for item in grid:
            item[1]=new_grid[1][count1]
            count1+=1
    count2=0
#replaces third item in each list in the grid with the third list in the new variable grid
    while count2<4:     
        for item in grid:
            item[2]=new_grid[2][count2]
            count2+=1
    count3=0
#replaces fourth item in each list in grid with the fourth list in the new variable grid
    while count3<4:     
        for item in grid:
            item[3]=new_grid[3][count3]
            count3+=1
            
    return grid
            
#create function adds values in the grid downwards    
def push_down(grid):        
    new_grid=[]             
    temp_grid=[]       
#adds first item in every list in grid to the temporary list
    for item in grid:       
        temp_grid.append(item[0])
    t_grid=[]
#adds second item in every list in grid to the temporary list
    for item in grid:       
        t_grid.append(item[1])
    n_grid=[]
#adds third item in every list in the grid to the temporary list
    for item in grid:     
        n_grid.append(item[2])
    h_grid=[]
#adds fourth item in every list in the grid to the temporary list
    for item in grid:       
        h_grid.append(item[3])
    new_grid.append(temp_grid)
    new_grid.append(t_grid)
#adds temporary variables into new variable grid
    new_grid.append(n_grid)    
    new_grid.append(h_grid)
#adds values in new variable grid to the right
    new_grid=push_right(new_grid)   
    count=0
    while count<4:
#replaces first item in each list in grid with the first list in the new variable grid
        for item in grid:      
            item[0]=new_grid[0][count]
            count+=1
    count1=0
#replaces second item in each list in grid with the second list in the new variable grid
    while count1<4:    
        for item in grid:
            item[1]=new_grid[1][count1]
            count1+=1
    count2=0
#replaces third item in each list in grid with the third list in of the new variable grid
    while count2<4:     
        for item in grid:
            item[2]=new_grid[2][count2]
            count2+=1
    count3=0
#replaces fourth item in each list in grid with the fourth list in the new variable grid
    while count3<4:     
        for item in grid:
            item[3]=new_grid[3][count3]
            count3+=1
                
    return grid  

# create function to move all values left              
def push_left(grid):       
    i=1
#removes all 0 values to the left
    while i<4:              
        for item in grid:
            #to ease calculation
            item.append(0)      
            for i in range(4):
                if item[i]==0:
                    item[i]=item[i+1]
                    item[i+1]=0
            item.remove(item[4])        
        i+=1
    #adds values to the left
    for objct in grid:         
        objct.append(0)
        for i in range(4):
            if objct[i]==objct[i+1]:
                objct[i]*=2
                objct[i+1]=0
        objct.remove(objct[4])
    j=1
    #removes 0 values created when adding values
    while j<4:                  
        for item in grid:
            item.append(0)
            for i in range(4):
                if item[i]==0:
                    item[i]=item[i+1]
                    item[i+1]=0
            item.remove(item[4])
        j+=1
               
    return grid  

# create function to add values to the right
def push_right(grid):       
    count=1
    #removes all 0 values to the right
    while count<4:         
        for item in grid:
            #item inserted to ease calculation
            item.insert(0, 0)   
            for i in range(-4, 0):
                if item[-i]==0:
                    item[-i]=item[-i-1]
                    item[-i-1]=0
            item.remove(item[0])    
        count+=1
    #addition of items to the right
    for objct in grid:             
        objct.insert(0,0)
        for i in range(-4, 0):
            if objct[-i]==objct[-i-1]:
                objct[-i]*=2
                objct[-i-1]=0
        objct.remove(objct[0])
    count1=1
    #removes all 0 values created during the adding of values
    while count1<4:             
        for item in grid:
            item.insert(0, 0)
            for i in range(-4, 0):
                if item[-i]==0:
                    item[-i]=item[-i-1]
                    item[-i-1]=0
            item.remove(item[0])
        count1+=1
    return grid    