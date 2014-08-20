def push_left(input_list):
    list1 = []
    for i in input_list:
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
def push_right(input_list):
    list1 = []
    for i in input_list:
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

def push_up (grid):
    #merge grid values upwards
    col1 = []
    for i in range(4):
        col1.append(grid[i][0])
        
    col2 = []
    for i in range(4):
        col2.append(grid[i][1])
    col3 = []
    for i in range(4):
        col3.append(grid[i][2])
    col4 = []
    for i in range(4):
        col4.append(grid[i][3])

    col1 = test.shift_left(col1)
    col2 = test.shift_left(col2)
    col3 = test.shift_left(col3)
    col4 = test.shift_left(col4)

    for i in range(4):
        grid[i][0] = col1[i]
    for i in range(4):
        grid[i][1] = col2[i]
    for i in range(4):
        grid[i][2] = col3[i]
    for i in range(4):
        grid[i][3] = col4[i]
    
def push_down (grid):
    #merge grid values downwards
    col1 = []
    for i in range(4):
        col1.append(grid[i][0])
        
    col2 = []
    for i in range(4):
        col2.append(grid[i][1])
    col3 = []
    for i in range(4):
        col3.append(grid[i][2])
    col4 = []
    for i in range(4):
        col4.append(grid[i][3])

    col1 = test.shift_right(col1)
    col2 = test.shift_right(col2)
    col3 = test.shift_right(col3)
    col4 = test.shift_right(col4)

    for i in range(4):
        grid[i][0] = col1[i]
    for i in range(4):
        grid[i][1] = col2[i]
    for i in range(4):
        grid[i][2] = col3[i]
    for i in range(4):
        grid[i][3] = col4[i]
def push_left (grid):
    #merge grid values left
    for i in range(4):
        grid[i] = test.shift_left(grid[i])
        
def push_right (grid):
    #merge grid values right
    for i in range(4):
        grid[i] = test.shift_right(grid[i])
        
