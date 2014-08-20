# Question 3 Assignment 7 2048 game
# Michael Sanne
# 2014/05/01

#Moves all the empty spaces to the end to allow for merger
def zero_to_end (list0):
    count = 0            
    for i in range (4):
        
        if (0) in list0:
            list0.remove(0)
            count += 1
    for j in range (count):
            list0.append(0)
    return list0

#Moves all the empty spaces to the beginning of the list to allow merger
def zero_to_beginning (list0):
    count = 0
    new_list = []
    for i in range (4):
        if (0) in list0:
            list0.remove(0)
            count += 1
    for j in range (count):
        new_list.append(0)
    for k in range (len(list0)):
        new_list.append (list0[k])
    return new_list    

#merges up and left
def merge (list0):
    for i in range (len(list0) - 1):
        if list0[i] == list0[i+1] and list0[i]!=0:
            list0[i] = 2*(list0[i])
            list0[i+1] = 0
            zero_to_end(list0)
    return list0
#Merges down and right from other side
                    
def merge_reverse (list0):
    list0.reverse()
    list0 = merge(list0)
    list0.reverse()
    return list0    
#Button for up
def push_up (grid):    
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    
    for j in range (len(grid)):
        for i in range (len(grid[j])):
            if i == 0:
                list1.append(grid[j][i])
            if i == 1:
                list2.append(grid[j][i])
            if i == 2:
                list3.append(grid[j][i])
            if i == 3:
                list4.append(grid[j][i])
    
    list1 = zero_to_end(list1)
    list2 = zero_to_end(list2)
    list3 = zero_to_end(list3)
    list4 = zero_to_end(list4)
    
    list1 = merge(list1)
    list2 = merge(list2)
    list3 = merge(list3)
    list4 = merge(list4)
    
    x1 = [list1[0], list2[0], list3[0], list4[0]]
    x2 = [list1[1], list2[1], list3[1], list4[1]]
    x3 = [list1[2], list2[2], list3[2], list4[2]]
    x4 = [list1[3], list2[3], list3[3], list4[3]]
    grid[0] = x1
    grid[1] = x2
    grid[2] = x3
    grid[3] = x4
#Button for down
def push_down(grid):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
        
    for j in range (len(grid)):
        for i in range (len(grid[j])):
            if i == 0:
                list1.append(grid[j][i])
            if i == 1:
                list2.append(grid[j][i])
            if i == 2:
                list3.append(grid[j][i])
            if i == 3:
                list4.append(grid[j][i])    
    
    list1 = zero_to_beginning(list1)
    list2 = zero_to_beginning(list2)
    list3 = zero_to_beginning(list3)
    list4 = zero_to_beginning(list4)
    
    list1 = merge_reverse (list1)
    list2 = merge_reverse (list2)
    list3 = merge_reverse (list3)
    list4 = merge_reverse (list4)
    
    x1 = [list1[0], list2[0], list3[0], list4[0]]
    x2 = [list1[1], list2[1], list3[1], list4[1]]
    x3 = [list1[2], list2[2], list3[2], list4[2]]
    x4 = [list1[3], list2[3], list3[3], list4[3]]
    
    grid[0] = x1
    grid[1] = x2
    grid[2] = x3
    grid[3] = x4    
    
#Button for left
def push_left (grid):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
        
    for j in range (len(grid)):
        for i in range (len(grid[j])):
            if j == 0:
                list1.append(grid[j][i])
            if j == 1:
                list2.append(grid[j][i])
            if j == 2:
                list3.append(grid[j][i])
            if j == 3:
                list4.append(grid[j][i])
        
    list1 = zero_to_end(list1)
    list2 = zero_to_end(list2)
    list3 = zero_to_end(list3)
    list4 = zero_to_end(list4)
        
    list1 = merge(list1)
    list2 = merge(list2)
    list3 = merge(list3)
    list4 = merge(list4)
        
    x1 = list1
    x2 = list2
    x3 = list3
    x4 = list4
    
    grid[0] = x1
    grid[1] = x2
    grid[2] = x3
    grid[3] = x4

#Button for right
def push_right (grid):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
            
    for j in range (len(grid)):
        for i in range (len(grid[j])):
            if j == 0:
                list1.append(grid[j][i])
            if j == 1:
                list2.append(grid[j][i])
            if j == 2:
                list3.append(grid[j][i])
            if j == 3:
                list4.append(grid[j][i])    
        
    list1 = zero_to_beginning(list1)
    list2 = zero_to_beginning(list2)
    list3 = zero_to_beginning(list3)
    list4 = zero_to_beginning(list4)
        
    list1 = merge_reverse (list1)
    list2 = merge_reverse (list2)
    list3 = merge_reverse (list3)
    list4 = merge_reverse (list4)
        
    x1 = list1
    x2 = list2
    x3 = list3
    x4 = list4
    
    grid[0] = x1
    grid[1] = x2
    grid[2] = x3
    grid[3] = x4        