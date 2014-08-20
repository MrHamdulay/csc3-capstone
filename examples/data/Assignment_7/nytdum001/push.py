"""Module for use in 2048 number game
Dumisani J Nyathi
02-05-2014"""

# merge grid values upwards
def push_up (grid):
   
    column1 = []
    for i in range(4):
        column1.append(grid[i][0])  
    column2 = []
    for i in range(4):
        column2.append(grid[i][1])
    column3 = []
    for i in range(4):
        column3.append(grid[i][2])
    column4 = []
    for i in range(4):
        column4.append(grid[i][3])

    column1 = shift_left(column1)
    column2 = shift_left(column2)
    column3 = shift_left(column3)
    column4 = shift_left(column4)

    for i in range(4):
        grid[i][0] = column1[i]
    for i in range(4):
        grid[i][1] = column2[i]
    for i in range(4):
        grid[i][2] = column3[i]
    for i in range(4):
        grid[i][3] = column4[i]

    
# merge grid values downwards
def push_down (grid):
   
    column1 = []
    for i in range(4):
        column1.append(grid[i][0])
    column2 = []
    for i in range(4):
        column2.append(grid[i][1])
    column3 = []
    for i in range(4):
        column3.append(grid[i][2])
    column4 = []
    for i in range(4):
        column4.append(grid[i][3])

    column1 = shift_right(column1)
    column2 = shift_right(column2)
    column3 = shift_right(column3)
    column4 = shift_right(column4)

    for i in range(4):
        grid[i][0] = column1[i]
    for i in range(4):
        grid[i][1] = column2[i]
    for i in range(4):
        grid[i][2] = column3[i]
    for i in range(4):
        grid[i][3] = column4[i]



#merge grid values left
def push_left (grid):
    for i in range(4):
        grid[i] = shift_left(grid[i])#will call another function which will shift the values leftward
        


# merge grid values right
def push_right (grid):
    for i in range(4):
        grid[i] = shift_right(grid[i])#will call another function which will shift the values rightward


#shifts the values to the left,just shift
def shift_left(grid):
    list1 = []
    for i in grid:
        if i!=0:
            list1.append(i)
    shifted_list = []
    i = 0
    while i < len(list1):
        if i+1<len(list1) and list1[i] == list1[i+1]:
            shifted_list.append(list1[i]*2)
            i += 2
        else:
            shifted_list.append(list1[i])
            i += 1
    for i in range(4-len(shifted_list)):
        shifted_list.append(0)
    return shifted_list


#shifts the values to the right,just shifts
def shift_right(grid):
    list1 = []
    for i in grid:
        if i!=0:
            list1.append(i)
    shifted_list = []
    i = len(list1)-1
    while i >=0:
        if i-1>=0 and list1[i] == list1[i-1]:
            if len(shifted_list) ==0:
                shifted_list.append(list1[i]*2)
            else:
                shifted_list.insert(0,list1[i]*2)
            i -= 2
        else:
            shifted_list.insert(0,list1[i])
            i -= 1
    for i in range(4-len(shifted_list)):
        if len(shifted_list) == 0:
            shifted_list.append(0)
        else:
            shifted_list.insert(0,0)
        
    return shifted_list