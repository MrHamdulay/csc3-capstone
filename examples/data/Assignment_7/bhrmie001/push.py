# Miengha Behardien
#Assignment 7
#28 April 2014

def push_up(grid):
    new_grid=[]
    temp_grid=[]
    for item in grid:
        temp_grid.append(item[0])
    t_grid=[]
    for item in grid:
        t_grid.append(item[1])
    n_grid=[]
    for item in grid:
        n_grid.append(item[2])
    h_grid=[]
    for item in grid:
        h_grid.append(item[3])
    new_grid.append(temp_grid)
    new_grid.append(t_grid)
    new_grid.append(n_grid)
    new_grid.append(h_grid)
    new_grid=push_left(new_grid)
    count=0
    while count<4:
        for item in grid:
            item[0]=new_grid[0][count]
            count+=1
    count1=0
    while count1<4:
        for item in grid:
            item[1]=new_grid[1][count1]
            count1+=1
    count2=0
    while count2<4:
        for item in grid:
            item[2]=new_grid[2][count2]
            count2+=1
    count3=0
    while count3<4:
        for item in grid:
            item[3]=new_grid[3][count3]
            count3+=1
            
    return grid
            
          
def push_down(grid):
    new_grid=[]
    temp_grid=[]
    for item in grid:
        temp_grid.append(item[0])
    t_grid=[]
    for item in grid:
        t_grid.append(item[1])
    n_grid=[]
    for item in grid:
        n_grid.append(item[2])
    h_grid=[]
    for item in grid:
        h_grid.append(item[3])
    new_grid.append(temp_grid)
    new_grid.append(t_grid)
    new_grid.append(n_grid)
    new_grid.append(h_grid)
    new_grid=push_right(new_grid)
    count=0
    while count<4:
        for item in grid:
            item[0]=new_grid[0][count]
            count+=1
    count1=0
    while count1<4:
        for item in grid:
            item[1]=new_grid[1][count1]
            count1+=1
    count2=0
    while count2<4:
        for item in grid:
            item[2]=new_grid[2][count2]
            count2+=1
    count3=0
    while count3<4:
        for item in grid:
            item[3]=new_grid[3][count3]
            count3+=1
                
    return grid    
                
def push_left(grid):
    i=1
    while i<4:
        for item in grid:
            item.append(0)
            for i in range(4):
                if item[i]==0:
                    item[i]=item[i+1]
                    item[i+1]=0
            item.remove(item[4])
        i+=1
    for objct in grid:
        objct.append(0)
        for i in range(4):
            if objct[i]==objct[i+1]:
                objct[i]*=2
                objct[i+1]=0
        objct.remove(objct[4])
    j=1
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

def push_right(grid):
    count=1
    while count<4:
        for item in grid:
            item.insert(0, 0)
            for i in range(-4, 0):
                if item[-i]==0:
                    item[-i]=item[-i-1]
                    item[-i-1]=0
            item.remove(item[0])
        count+=1
    for objct in grid:
        objct.insert(0,0)
        for i in range(-4, 0):
            if objct[-i]==objct[-i-1]:
                objct[-i]*=2
                objct[-i-1]=0
        objct.remove(objct[0])
    count1=1
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