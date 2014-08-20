'''Module push for 2048 game
Othniel KONAN
KNNOTH001
2014/04/27
'''
import util

#TRANSFORM A DOUBLE ARRAY(X->Y)
def symetric_x_y(grid):
    '''transform the array to its symetric such as [x][y]->[y][x] (e.g [[1,2],[3,4]]->[[1,3],[2,4]])'''
    gri = util.copy_grid(grid)                  #make copy of the grid
    for y in range(4):
        for x in range(4):
            grid[y][x] = gri[x][y]              #rotate grid

#REVERSE EACH LINE OF AN ARRAY
def revers(grid):
    '''reverse an array or every line of a double array'''
    for y in range(len(grid)):
        grid[y].reverse()

#MOVE THE NON-ZERO OF THE LIST TO THE LEFT
def organizer(lt):
    '''Organize the grid in such way that the zero are moved to the end e.g [2,0,9,0]->[2,9,0,0]'''
    l=[]                                      
    for i in lt:
        if i!=0:
            l.append(i)               #append the non zero value to a list
    for j in range(len(lt)-len(l)):
        l.append(0)                   #append 0 to the rest of that list
    for i in range(len(l)):           
        lt[i]=l[i]                    #modify the input list


#PUSH UP
def push_up (grid):
    """merge grid values upwards"""
    symetric_x_y(grid)                          #flip the grid in order to manipulate push_up as if it was push_left(In fact i strated with push_left so I wanted to make my life easier)
    push_left (grid)                            
    symetric_x_y(grid)                          #flip the grid to its original position
 
#PUSH DOWN        
def push_down (grid):
    """merge grid values downwards"""
    symetric_x_y(grid)                          #flip the grid in order to manipulate push_down as if it was push_up
    push_right (grid)
    symetric_x_y(grid)                          #flip the grid to its original position
                

#PUSH LEFT                    
def push_right (grid):
    """merge grid values right"""
    revers(grid)                                #reverse the grid (change the situation to the one in push_left)
    push_left(grid)                              
    revers(grid)                                #return to the normal

#PUSH LEFT
def push_left (grid):
    """merge grid values left"""
    for y in range(4):
        organizer(grid[y])                      #organise that line of the grid
        for x in range(3):
            if grid[y][x] == grid[y][x+1]:      #add those which are equal
                grid[y][x] *= 2                 #double the one at the left position
                grid[y][x+1] = 0                #make the other equal to zero
        organizer(grid[y])                      #organise that line of the grid


            
