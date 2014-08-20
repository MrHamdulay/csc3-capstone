"""functions to manipulate 4x4 grid
tafara mtutu
1 may 2014"""

def push_up (grid):
    """merge grid values upwards""" 
    for row in range(4):
        temp_list = []
        list = []        
        for col in range(4):
            if grid[col][row] == 0:
                continue
            else:
                list.append(grid[col][row])                              
        for i in range(4-len(list)):
            list.append(0)            
        for count in range(3):
            if list[count] == list[count+1]:
                list[count] += list[count+1]
                list[count+1] = 0        
        for m in range(4):
            if list[m] != 0:
                temp_list.append(list[m])        
        for j in range(4-len(temp_list)):
            temp_list.append(0)        
        for g in range(4):
            grid[g][row] = temp_list[g]
            
def push_down (grid):
    """merge grid values downwards"""
    for row in range(4):
        temp_list = []
        list = []        
        for col in range(4):
            if grid[col][row] == 0:
                continue
            else:
                list.append(grid[col][row])                              
        for i in range(4-len(list)):
            list.append(0)            
        for count in range(3,0,-1):
            if list[count] == list[count-1]:
                list[count] += list[count-1]
                list[count-1] = 0        
        for m in range(4):
            if list[m] != 0:
                temp_list.append(list[m])        
        for j in range(4-len(temp_list)):
            temp_list.insert(0,0) 
        #print(temp_list)
        for g in range(4):
            grid[g][row] = temp_list[g]    
    
def push_left (grid):
    """merge grid values left"""
    for row in range(4):
        temp_list = []
        list = []        
        for col in range(4):
            if grid[row][col] == 0:
                continue
            else:
                list.append(grid[row][col])
        #print(row, col, list)
        for i in range(4-len(list)):
            list.append(0)            
        for count in range(3):
            if list[count] == list[count+1]:
                list[count] += list[count+1]
                list[count+1] = 0        
        for m in range(4):
            if list[m] != 0:
                temp_list.append(list[m])        
        for j in range(4-len(temp_list)):
            temp_list.append(0) 
        #print(temp_list)
        for g in range(4):
            grid[row][g] = temp_list[g] 
    
def push_right (grid):
    """merge grid values right"""
    for row in range(4):
            temp_list = []
            list = []        
            for col in range(4):
                if grid[row][col] == 0:
                    continue
                else:
                    list.append(grid[row][col])
            #print(row, col, list)
            for i in range(4-len(list)):
                list.append(0)            
            for count in range(3):
                if list[count] == list[count+1]:
                    list[count] += list[count+1]
                    list[count+1] = 0        
            for m in range(4):
                if list[m] != 0:
                    temp_list.append(list[m])        
            for j in range(4-len(temp_list)):
                temp_list.insert(0,0) 
            #print(temp_list)
            for g in range(4):
                grid[row][g] = temp_list[g]    