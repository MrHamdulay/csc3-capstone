'''question3.py
check whether a sudoku grid is valid
douglas newton NWTDOU001
12 may 2014'''

# returns False if the number has been seen by the checker or if the number lies
# outside range 1-9. otherwise records it in the checker and returns True
def check(number,checker):
    if not 1<=number<=9: return False
    if number in checker: return False
    checker[number] = True
    return True    

# checks the ith row of a grid. True if valid, False if not
def check_row(grid,i):
    checker = {}
    for number in grid[i]:
        if not check(number,checker):
            return False
    return True

# checks the ith column of a grid
def check_col(grid,i):
    checker = {}
    for y in range(len(grid)):
        if not check(grid[y][i],checker):
            return False
    return True

# checks 3x3 region at x,y -- where 0,0 is top left region of grid
def check_region(grid,x,y):
    checker = {}
    # top, bottom, left, right coords of region (for looping ranges)
    t = y*3
    b = t+2
    l = x*3
    r = l+2
    for y in range(t,b+1):
        for x in range(l,r+1):
            if not check(grid[y][x],checker):
                return False
    return True

# combine all checks above into single function
def check_grid(grid):
    
    # check all the rows
    for y in range(len(grid)):
        if not check_row(grid,y):
            #print('row fail at',y)
            return False
        
    # check all the columns
    for x in range(len(grid)):
        if not check_col(grid,x):
            #print('col fail at',y)
            return False
        
    # check all the regions
    for y in range(0,3):
        for x in range(0,3):
            if not check_region(grid,x,y):
                #print('reg fail at',x,y)
                return False
    
    # if all the checks passed, the grid is valid
    return True

# get the grid row by row from input

grid = []

for i in range(9):
    line = input()
    row = []
    for c in line:
        row.append(eval(c))
    grid.append(row)

if check_grid(grid):
    print('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')