'''program to check if a sudoku grid is valid
Othniel KONAN
KNNOTH001
10 May 2014'''

#FUNCTION TO CHECK IF THERE ARE MORE ONE SAME ELEMENT IN A LIST
def no_double(lt):
    for e in lt:                            #go through all the str 
        nbr = lt.count(e)                   #count the number of time than the element appear in the str
        if nbr > 1: return False            #return false if it's more than one
    else : return True                      #else return true
        

#PROMPT THE USER AND PUT THE VALUES IN A 2D ARRAY
grid = []
for i in range(9):                          #ask the user 9 times
    line = input()                          
    line = ' '.join(str(line)).split(' ')   #put space between each character and split them 
    grid.append(line)                       #append the list of number to grid

#CHECK HORIZONTAL LINES
for i in range(len(grid)):
    horizontal = no_double(grid[i])         #check if each horizontal line are correct
    if horizontal == False: break           #return the value of horizontal (true if it's correct else false)
else:
    horizontal = True

#CHECK VERTICAL LINES
for i in range(len(grid)):
    ver=[]
    for j in range(len(grid)):              
        ver.append(grid[j][i])              #put each column in ver
    vertical = no_double(ver)               #check if the vertical line is correct
    if vertical == False: break             #return the value of vertical (true if it's correct else false)
else:
    vertical = True

#PUT 3x3 GRID IN A LIST AND CHECK IF T'S CORRECT
def block(y,x):
    '''create a 3x3 grid given a starting point being the top left of the 3x3 grid'''
    bl = []
    for j in range(3):
        for i in range(3):
            bl.append(grid[y+i][x+j])   #append all the value of the 3x3 grid in a list
    return no_double(bl)                #check if the 3x3 grid (sub-grid) is correct and return it's value

#CHECK ALL THE 9 BLOCK
ext=0
for y in range(3):                      
    for x in range(3):
        sub_grid = block(y*3,x*3)       #set 9 principle starting points for the function block and check all 9 sub-grids
        if sub_grid == False: 
            ext=1
            break
    if ext==1: break


#CHECK THE ENTIRE GRID
if horizontal == False or vertical == False or sub_grid == False:   #check if the entire grid is correct
    print('Sudoku grid is not valid')
else:
    print('Sudoku grid is valid')
        