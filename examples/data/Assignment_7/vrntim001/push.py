''' push
Tim Mostert
29.30.14'''

def merge_array(array):
    array0 = array[0]
    array1 = array[1]
    array2 = array[2]
    array3 = array[3]
    
    if array0 == array1:
        array0 = array0*2
        array1 = 0
    if array1 == array2:
        array1 = array1*2
        array2 = 0
    if array2 == array3:
        array3 = 0
        array2 = array2*2 
    new = []    
    new.append(array0)
    new.append(array1)
    new.append(array2)
    new.append(array3)
    return new
        
def shift_array(array):
    array0 = array[0]
    array1 = array[1]
    array2 = array[2]
    array3 = array[3]
    
    if array0 == 0:
        if array1 > 0:
            array0 = array1
            array1 = 0
        elif array2 > 0:
            array0 = array2
            array2 = 0
        elif array3 > 0:
            array0 = array3
            array3 = 0
    if array1 == 0:
        if array2 > 0:
            array1 = array2
            array2 = 0
        elif array3 > 0:
            array1 = array3
            array3 = 0
    if array2 == 0:
        if array3 > 0:
            array2 = array3
            array3 = 0
        
    new = []    
    new.append(array0)
    new.append(array1)
    new.append(array2)
    new.append(array3)
    return new    
    
def push_left(grid):
    grid[0] = shift_array(merge_array(shift_array(grid[0])))
    grid[1] = shift_array(merge_array(shift_array(grid[1])))
    grid[2] = shift_array(merge_array(shift_array(grid[2])))
    grid[3] = shift_array(merge_array(shift_array(grid[3])))
    
def push_right(grid):
    grid[0] = grid[0][::-1]
    grid[1] = grid[1][::-1]
    grid[2] = grid[2][::-1]
    grid[3] = grid[3][::-1]    
    grid[0] = shift_array(merge_array(shift_array(grid[0])))
    grid[1] = shift_array(merge_array(shift_array(grid[1])))
    grid[2] = shift_array(merge_array(shift_array(grid[2])))
    grid[3] = shift_array(merge_array(shift_array(grid[3]))) 
    grid[0] = grid[0][::-1]
    grid[1] = grid[1][::-1]
    grid[2] = grid[2][::-1]
    grid[3] = grid[3][::-1]    
    
    
def push_up(grid):
    array0 = []
    array1 = []
    array2 = []
    array3 = []
    array0.append(grid[0][0])
    array0.append(grid[1][0])
    array0.append(grid[2][0])
    array0.append(grid[3][0])
    array1.append(grid[0][1])
    array1.append(grid[1][1])
    array1.append(grid[2][1])
    array1.append(grid[3][1])
    array2.append(grid[0][2])
    array2.append(grid[1][2])
    array2.append(grid[2][2])
    array2.append(grid[3][2])
    array3.append(grid[0][3])
    array3.append(grid[1][3])
    array3.append(grid[2][3])
    array3.append(grid[3][3])
    
    array0 = shift_array(merge_array(shift_array(array0)))
    array1 = shift_array(merge_array(shift_array(array1)))
    array2 = shift_array(merge_array(shift_array(array2)))
    array3 = shift_array(merge_array(shift_array(array3)))
    
    grid[0] = [array0[0],array1[0],array2[0],array3[0]]
    grid[1] = [array0[1],array1[1],array2[1],array3[1]]
    grid[2] = [array0[2],array1[2],array2[2],array3[2]]
    grid[3] = [array0[3],array1[3],array2[3],array3[3]]
    
def push_down(grid):
    array0 = []
    array1 = []
    array2 = []
    array3 = []
    array0.append(grid[3][0])
    array0.append(grid[2][0])
    array0.append(grid[1][0])
    array0.append(grid[0][0])
    array1.append(grid[3][1])
    array1.append(grid[2][1])
    array1.append(grid[1][1])
    array1.append(grid[0][1])
    array2.append(grid[3][2])
    array2.append(grid[2][2])
    array2.append(grid[1][2])
    array2.append(grid[0][2])
    array3.append(grid[3][3])
    array3.append(grid[2][3])
    array3.append(grid[1][3])
    array3.append(grid[0][3])
    
    array0 = shift_array(merge_array(shift_array(array0)))
    array1 = shift_array(merge_array(shift_array(array1)))
    array2 = shift_array(merge_array(shift_array(array2)))
    array3 = shift_array(merge_array(shift_array(array3)))
    
    grid[0] = [array0[3],array1[3],array2[3],array3[3]]
    grid[1] = [array0[2],array1[2],array2[2],array3[2]]
    grid[2] = [array0[1],array1[1],array2[1],array3[1]]
    grid[3] = [array0[0],array1[0],array2[0],array3[0]]    
    
            
   
    
    
  
    
    
   

    
        
        
        
                
            
    
        
        
        
    

    