#create empty grid
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        #rows
        grid.append([])
        for j in range(4):
            #values
            grid[i].append(0)
    return grid
    
#print grid in frame
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    space = 5
    #first line
    print('+', '-'*20, '+', sep='')
    for i in grid:
        #for each of the 4 rows
        print('|', end ='')
        for j in i:
            if j == 0:
                print(' '*space, sep='', end ='')
            else:  
                #format and print values
                space -= len(str(j))
                print(j, ' '*space, sep='', end='')
                space = 5
        print('|', end ='')
        print()
    #last line
    print('+', '-'*20, '+', sep='')

#check if no more possible moves
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    zero = True
    for i in grid:
        for j in i:
            #f any blank spaces
            if j == 0:
                #have not lost yet
                zero = False
                break
            else: continue
    if zero == 1:
        array = grid
        b = [0,0,0,0]
        c = 0
        #create frame to not get range errors
        array.insert(0,b)
        array.insert(5,b)
        for row in array:
            row.insert(0,c)
            row.insert(5,c)            
        for y in range(len(array)):
            for x in range(len(array)):
                #for all values
                if array[y][x] != 0:
                    #look for matching values next to the value
                    if (array[y][x] == array[y][x-1])or (array[y][x] == array[y+1][x]):
                        zero = False
                        break
                    else:
                        continue
    return zero
                        
#check if any values over 32
def check_won(grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won = False
    for i in grid:
        for j in i:
            if j >= 32:
                won = True
            else:
                continue
    return won        

#create copy
def copy_grid (grid):
    """return a copy of the grid"""
    copy = []
    for i in range(4):
        copy.append([])
        for j in range(4):
            #for each row, insert numbers
            copy[i].append(grid[i][j])
            
    return copy

#check if grids are equal
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    equal = True
    for x in range(4):
        for y in range(4):
            if grid1[x][y] == grid2[x][y]:
                continue
            else:
                equal = False
                break
    return equal
                