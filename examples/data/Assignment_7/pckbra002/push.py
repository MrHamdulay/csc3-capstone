"""Program to use the functions of the util program and shift the values in the 4x4 grid around"""
"""Brandon Pickup"""
"""Assignment 7 Question 3"""
"""27 April 2014"""
import util
def shift(lis):
    """function that takes a single list and shifts all the values as close to the beginning of the list as possible"""
    for i in range(3):
        pos=i+1#variable that allows me to check the value in the list with the value on it's left
        while lis[pos-1] == 0 and pos >0:#continues to shift the value in the list left, while there is a 0 in the position next to it or until the counter is bigger than 0(to avoid an index error)
            lis[pos-1] = lis[pos]#when there is a 0 to the left, the current value is copied over to that position and where it was moved from is set to an empty space - value of 0
            lis[pos]=0
            pos-=1#increments the pos variable by -1 to continue comparing values to the left in the list
    return lis

def add(lis):
    """function that adds adjacent values that are equal in a list, together"""
    for i in range(3):
        pos = i+1#same as the shift function pos variable
        if lis[pos-1] == lis[pos]:#if the value to the left is equal to the current value, the left value is added to the current value in the left value position, and the value in the current position is set to 0
            lis[pos-1] = lis[pos-1]*2
            lis[pos] = 0    
    return lis  

def altered_grid(grid,test_grid):
    """method to alter the grid parameter sent to a function with the edited version of itself"""
    for i in range(4):
        for j in range(4):
            grid[i][j] = test_grid[i][j]  
            
def push_up (grid):
    """merge grid values upwards"""
    test_grid = util.copy_grid (grid)#creates a copy of the grid for us to work on
    for i in range(4):
        lis=[]
        for j in range(4):
            lis.append(test_grid[j][i])#pulls out a list according to the direction of the function name. A column is pulled out of the grid as a list on it's own
        lis=shift(lis)
        lis=add(lis)
        lis= shift(lis)   
        for j in range(4):
            test_grid[j][i] = lis[j]#returns the values in the list to the same positions that they were extracted from in the grid
    altered_grid(grid,test_grid)#alters the grid with the edited version once all the changes have been made  

def push_down (grid):
    """merge grid values downwards"""
    test_grid = util.copy_grid (grid)
    for i in range(4):
        lis=[]
        for j in range(4):
            lis.append(test_grid[j][i])#pulls out a list according to the direction of the function name. A column is pulled out of the grid as a list on it's own
        lis = lis[::-1]#because this function is to shift right, we reverse the string, apply the same shift and add methods, and once that is done, we reverse it back. This works because up and down are reverses of eachother in movement
        lis=shift(lis)
        lis=add(lis)
        lis= shift(lis)   
        lis = lis[::-1]
        for j in range(4):
            test_grid[j][i] = lis[j]#returns the values in the list to the same positions that they were extracted from in the grid
    altered_grid(grid,test_grid)#alters the grid with the edited version once all the changes have been made       

def push_left (grid):
    """merge grid values left"""
    test_grid = util.copy_grid (grid)
    for i in range(4):
        lis = test_grid[i]#pulls out a list according to the direction of the function name. A row is pulled out of the grid as a list on it's own
        lis=shift(lis)
        lis=add(lis)
        lis= shift(lis)   
        for j in range(4):
            test_grid[i][j] = lis[j]#returns the values in the list to the same positions that they were extracted from in the grid
    altered_grid(grid,test_grid)#alters the grid with the edited version once all the changes have been made 
      
def push_right (grid):
    """merge grid values right"""
    test_grid = util.copy_grid (grid)
    for i in range(4):
        lis = test_grid[i]#pulls out a list according to the direction of the function name. A row is pulled out of the grid as a list on it's own
        lis = lis[::-1]#because this function is to shift right, we reverse the string, apply the same shift and add methods, and once that is done, we reverse it back. This works because left and right are reverses of eachother in movement
        lis=shift(lis)
        lis=add(lis)
        lis= shift(lis)
        lis = lis[::-1]
        for j in range(4):
            test_grid[i][j] = lis[j]#returns the values in the list to the same positions that they were extracted from in the grid
    altered_grid(grid,test_grid)#alters the grid with the edited version once all the changes have been made   