import shifts #Use the shifts module to administrate the shifts in the game

def push_up (grid):
    #merge grid values upwards"""
    column_one = [] #Creating the first column using a list
    for i in range(4):
        column_one.append(grid[i][0])
        
    column_two= []
    for i in range(4):
        column_two.append(grid[i][1])
    column_three = []
    for i in range(4):
        column_three.append(grid[i][2])
    column_four = []
    for i in range(4):
        column_four.append(grid[i][3]) #Creating the four column as it is a four by four grid

    column_one = shifts.shiftone(column_one)
    column_two = shifts.shiftone(column_two)
    column_three = shifts.shiftone(column_three)
    column_four= shifts.shiftone(column_four)

    for i in range(4):
        grid[i][0] = column_one[i]
    for i in range(4):
        grid[i][1] = column_two[i]
    for i in range(4):
        grid[i][2] = column_three[i]
    for i in range(4):
        grid[i][3] = column_four[i]
    
def push_down (grid):
    #merge grid values downwards
    column_one = []
    for i in range(4):
        column_one.append(grid[i][0])
        
    column_two = []
    for i in range(4):
        column_two.append(grid[i][1])
    column_three = []
    for i in range(4):
        column_three.append(grid[i][2])
    column_four = []
    for i in range(4):
        column_four.append(grid[i][3])

    column_one = shifts.shifttwo(column_one)
    column_two = shifts.shifttwo(column_two)
    column_three= shifts.shifttwo(column_three)
    column_four = shifts.shifttwo(column_four)

    for i in range(4):
        grid[i][0] = column_one[i]
    for i in range(4):
        grid[i][1] = column_two[i]
    for i in range(4):
        grid[i][2] = column_three[i]
    for i in range(4):
        grid[i][3] = column_four[i]

def push_left (grid):
    #merge grid values left
    for i in range(4):
        grid[i] = shifts.shiftone(grid[i])
        

def push_right (grid):
    #merge grid values right
    for i in range(4):
        grid[i] = shifts.shifttwo(grid[i])
        
