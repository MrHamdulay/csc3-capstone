""" A module that contains a set of merging functions that merge adjacent 
equal values and eliminate gaps.
Author: Dominic Manthoko
1 March 2014
"""


from copy import deepcopy

def len_1(array):
    """ function that shifts the single non-zero value of the array to the left
    and adds 3 zeros to the end
    """
    
    al_list = deepcopy(array)
    al_list2 = []
    
    al_list2.append(array[0])
    for l in range(3):
        al_list2.append(0)    
        
    return al_list2

# the functions len_2, len_3 and len_4 perform a similar task to len_1 but they
# hanlde array with more that one non_zero value

def len_2(array):
   
    al_list = deepcopy(array)
    al_list2 = []
    
    
    if al_list[0] == al_list[1]:
        al_list2.append(al_list[0] + al_list[1])
        
        for l in range(3):
            al_list2.append(0)
            
    
    else:
        al_list2.append(al_list[0])
        al_list2.append(al_list[1])
        al_list2.append(0)
        al_list2.append(0)
        
    return al_list2 
    
def len_3(array):
    
    al_list = deepcopy(array)
    al_list2 = []
    
    if al_list[0] == al_list[1]:
        al_list2.append(al_list[0] + al_list[1])
        al_list2.append(al_list[2])
        for i in range(2):
            al_list2.append(0)
        
        
    else:
        al_list2.append(al_list[0])
        
        if al_list[1] == al_list[2]:
            al_list2.append(al_list[1] + al_list[2])
            
            for l in range(2):
                al_list2.append(0)
                
                
        else:
            al_list2.append(al_list[1])
            al_list2.append(al_list[2])
            al_list2.append(0)
    
    return al_list2
        
def len_4(array):
    
    al_list = deepcopy(array)
    al_list2 = []
    
    if al_list[0] == al_list[1]:
        al_list2.append(al_list[0] + al_list[1])
        
        if al_list[2] == al_list[3]:
            al_list2.append(al_list[2] + al_list[3])
            for l in range(2):
                al_list2.append(0)
                
            item = al_list2
            
        else:
            al_list2.append(al_list[2])
            al_list2.append(al_list[3])
            al_list2.append(0)
            
            item = al_list2
            
    else:
        al_list2.append(al_list[0])
        
        new_list = len_3(al_list[1:])
        
        for i in range(3):
            al_list2.append(new_list[i])
       
    return al_list2

def sym(grid):
    """ a function that switches the values in a grid"""
    grid_copy = deepcopy(grid)
    for y in range(4):
        for x in range(4):
            grid[x][y]=grid_copy[y][x]
            
def rev_grid(grid):
    """ a function that reverses the values in an array or reverses the values
    of the items in a 2-d array
    """
    for y in range(len(grid)):
        grid[y].reverse()
        

def push_up (grid):
    """merge grid values upwards"""
    
    sym(grid)
    #print('after sym\n',grid)
    push_left(grid)
    #print('push left of sym\n',grid)
    sym(grid)
    #print('go back to initial pos\n',grid)    
    
def push_down (grid):
    """merge grid values downwards"""
    sym(grid)
    push_right(grid)
    sym(grid)

def push_left (grid):
    """merge grid values left"""
    
    counter=0
        
    # each list(item) in the grid(2-d array) will be altered
    for item in grid:
        
        # create an empty list where the non-zero values in the line will be stored
        al_list = []
        
        # create an empty list where the new values will be stores
        al_list2 = []
        
        # add the non_zero values in list1 to al_list
        for val in item:
            if val > 0:
                al_list.append(val)
                
        #print(al_list)
        
        if len(al_list) == 1:
            
            al_list2 = len_1(al_list)
            
            item = al_list2
            grid[counter]=item
        
            
        # checks if the length of the list is 2
        elif len(al_list) == 2:
            
            al_list2 = len_2(al_list)
                
            item = al_list2
            grid[counter]=item
        
        # checks if the length of the altered list is 3
        elif len(al_list) == 3:
            
            al_list2 = len_3(al_list)
            
            item = al_list2
            grid[counter]=item

        elif len(al_list) == 4:
            
            al_list2 = len_4(al_list)
            
            item = al_list2
            grid[counter]=item
        counter+=1
    return grid   
    

def push_right (grid):
    """merge grid values right"""     
    for i in range(4):
        grid[i].reverse()
    #print(grid[0])
    push_left(grid)
    #print(grid[0])
    for i in range(4):
        grid[i].reverse() 
    #print(grid[0])
