#Muzammil Jable
#Assignment 7
#28 April 2014

def push_up(grid):      #adds values in the grid up
    new_grid=[]         #new variable for storage
    temp_grid=[]        #temporary variables
    for item in grid:      #adds first item in every list within the grid to a temporary variabe
        temp_grid.append(item[0])
    t_grid=[]
    for item in grid:       #adds second item in every list within the grid to a temporary variabe
        t_grid.append(item[1])
    n_grid=[]
    for item in grid:       #adds third item in every list within the grid to a temporary variabe
        n_grid.append(item[2])
    h_grid=[]
    for item in grid:       #adds fourth item in every list within the grid to a temporary variabe
        h_grid.append(item[3])
    new_grid.append(temp_grid)
    new_grid.append(t_grid)     #adds all temp lists into new variable list
    new_grid.append(n_grid)
    new_grid.append(h_grid)
    new_grid=push_left(new_grid)    #adds all values in new varuable list to the left
    count=0
    while count<4:
        for item in grid:       #replaces first item in each list within the grid with the first list within of the new variable grid
            item[0]=new_grid[0][count]
            count+=1
    count1=0
    while count1<4:     #replaces second item in each list within the grid with the second list within of the new variable grid
        for item in grid:
            item[1]=new_grid[1][count1]
            count1+=1
    count2=0
    while count2<4:     #replaces third item in each list within the grid with the third list within of the new variable grid
        for item in grid:
            item[2]=new_grid[2][count2]
            count2+=1
    count3=0
    while count3<4:     #replaces fourth item in each list within the grid with the fourth list within of the new variable grid
        for item in grid:
            item[3]=new_grid[3][count3]
            count3+=1
            
    return grid
            
          
def push_down(grid):        #adds values in the grid down
    new_grid=[]             #new variable grid
    temp_grid=[]            #temporary list
    for item in grid:       #adds first item in every list within the grid to the temp list
        temp_grid.append(item[0])
    t_grid=[]
    for item in grid:       #adds second item in every list within the grid to the temp list
        t_grid.append(item[1])
    n_grid=[]
    for item in grid:       #adds third item in every list within the grid to the temp list
        n_grid.append(item[2])
    h_grid=[]
    for item in grid:       #adds fourth item in every list within the grid to the temp list
        h_grid.append(item[3])
    new_grid.append(temp_grid)
    new_grid.append(t_grid)
    new_grid.append(n_grid)     #adds temp variables into new variable grid
    new_grid.append(h_grid)
    new_grid=push_right(new_grid)   #adds values in new variable grid right
    count=0
    while count<4:
        for item in grid:       #replaces firsth item in each list within the grid with the first list within of the new variable grid
            item[0]=new_grid[0][count]
            count+=1
    count1=0
    while count1<4:     #replaces second item in each list within the grid with the second list within of the new variable grid
        for item in grid:
            item[1]=new_grid[1][count1]
            count1+=1
    count2=0
    while count2<4:     #replaces third item in each list within the grid with the third list within of the new variable grid
        for item in grid:
            item[2]=new_grid[2][count2]
            count2+=1
    count3=0
    while count3<4:     #replaces fourth item in each list within the grid with the fourth list within of the new variable grid
        for item in grid:
            item[3]=new_grid[3][count3]
            count3+=1
                
    return grid    
                
def push_left(grid):        #moves all values left
    i=1
    while i<4:              #eliminates all 0 values to the left
        for item in grid:
            item.append(0)      #added for calculation purposes
            for i in range(4):
                if item[i]==0:
                    item[i]=item[i+1]
                    item[i+1]=0
            item.remove(item[4])        #removes item appended for calculation
        i+=1
    for objct in grid:          #adds values to the left
        objct.append(0)
        for i in range(4):
            if objct[i]==objct[i+1]:
                objct[i]*=2
                objct[i+1]=0
        objct.remove(objct[4])
    j=1
    while j<4:                  #eliminates 0 values created when adding values
        for item in grid:
            item.append(0)
            for i in range(4):
                if item[i]==0:
                    item[i]=item[i+1]
                    item[i+1]=0
            item.remove(item[4])
        j+=1
               
    return grid        

def push_right(grid):       #adds values to the right
    count=1
    while count<4:          #removes all 0 values to the right
        for item in grid:
            item.insert(0, 0)   #item inserted for clculation purposes
            for i in range(-4, 0):
                if item[-i]==0:
                    item[-i]=item[-i-1]
                    item[-i-1]=0
            item.remove(item[0])    #inserted item removed again
        count+=1
    for objct in grid:              #adds items to the right
        objct.insert(0,0)
        for i in range(-4, 0):
            if objct[-i]==objct[-i-1]:
                objct[-i]*=2
                objct[-i-1]=0
        objct.remove(objct[0])
    count1=1
    while count1<4:             #removes all 0 values created during the adding of values
        for item in grid:
            item.insert(0, 0)
            for i in range(-4, 0):
                if item[-i]==0:
                    item[-i]=item[-i-1]
                    item[-i-1]=0
            item.remove(item[0])
        count1+=1
    return grid    