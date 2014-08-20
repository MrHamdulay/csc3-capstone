#Complete the code for a 2048 program, using the utility module.
#27 April 2014
#Kiran Desraj


# function to calculate summation of numbers values when moved upwards

def push_up(grid):    
    other_grid = []
    grid1=[]         
    
#adds items in list to temporary lists

    for i in grid:     
        other_grid.append(i[(1-1)])
    first_grid=[]
    

    for i in grid:      
        first_grid.append(i[(2-1)])       #appends to previous list (will be used below again)
    second_grid=[]


    for i in grid:       
        second_grid.append(i[(3-1)])
    third_grid=[]
 
    
    for i in grid:      
        third_grid.append(i[(4-1)])
    grid1.append(other_grid)
    
    
      
#moves created lists to initial list


    grid1.append(first_grid)     
    grid1.append(second_grid)
    grid1.append(third_grid)
    
    
#sums values to left-hand side 


    number = 0
    grid1 = push_left(grid1)
    
    while number < 4:
        for i in grid:       
            i[0]=grid1[0][number]
            number=number+1
    number1=0
    
    
    while number1<4:    
        for i in grid:
            i[1] =grid1[1][number1]
            number1 = number1 + 1
    number2=0

    while number2<4:     
        for i in grid:
            i[2]=grid1[2][number2]
            number2 = number2 + 1
    number3=0

    while number3<4:     
        for i in grid:
            i[3]=grid1[3][number3]
            number3 =number3 + 1
            
    return grid
            
            
#function to calculate the summation of grid numbers in downward direction - combines values

def push_down(grid):        
    for i in range(3):
        for horizontal in range(2,-1,-1):
            for vertical in range(3,-1,-1):
                if grid[horizontal+1][vertical] == 0:
                    grid[horizontal+1][vertical] = grid[horizontal][vertical]
                    grid[horizontal][vertical] = 0
                    
    for horizontal in range(2,-1,-1):
        for vertical in range(3,-1,-1):    
                if grid[horizontal+1][vertical] == grid[horizontal][vertical]:
                    grid[horizontal+1][vertical] = grid[horizontal+1][vertical]*2
                    grid[horizontal][vertical] = 0
                    
    for horizontal in range(2,-1,-1):
        for vertical in range(3,-1,-1):
            if grid[horizontal+1][vertical] == 0:
                grid[horizontal+1][vertical] = grid[horizontal][vertical]
                grid[horizontal][vertical] = 0
                
    return grid  




#summation of values in leftward direction 

def push_left(grid):       
    for i in range(3):
        for horizontal in range(4):
            for vertical in range(1,4):
                if grid[horizontal][vertical-1] == 0:
                    grid[horizontal][vertical-1] = grid[horizontal][vertical]
                    grid[horizontal][vertical] = 0
                    
    for horizontal in range(4):
        for vertical in range(1,4):                    
            if grid[horizontal][vertical-1] == grid[horizontal][vertical]:
                grid[horizontal][vertical-1] = grid[horizontal][vertical-1]*2
                grid[horizontal][vertical] = 0
                
    for horizontal in range(4):
        for vertical in range(1,4):
            if grid[horizontal][vertical-1] == 0:
                grid[horizontal][vertical-1] = grid[horizontal][vertical]
                grid[horizontal][vertical] = 0

    return grid




def push_right(grid):       
    number=1
    
    while number<4:         
        for item in grid:
            item.insert(0, 0)   
            for i in range(-4, 0):
                if item[-i]==0:
                    item[-i]=item[-i-1]
                    item[-i-1]=0
            item.remove(item[0])    
        number = number + 1
    
    for objct in grid:             
        objct.insert(0,0)
        for i in range(-4, 0):
            if objct[-i]==objct[-i-1]:
                objct[-i]*=2
                objct[-i-1]=0
        objct.remove(objct[0])
    number1 = 1
    
    while number1<4:             
        for i in grid:
            i.insert(0, 0)
            for j in range(-4, 0):
                if i[-j]==0:
                    i[-j]=i[-j-1]
                    i[-j-1]=0
            i.remove(i[0])
        number1 =number1 + 1
    return grid    