'''CSC1015F Assign 9 - Q3
Adam Rosendorff - RSNADA001
11 May 2014'''
#for checking for duplicates in a row/col
def duplicate(row):
    '''Checks suduko row/coloumn for duplicates. Returns True if duplicates found'''
    numbers = [i for i in range(1,10)]
    num_found = [False]*9
    for pos in range(9):
        if row[pos] in numbers:
            if not num_found[numbers.index(row[pos])]:
                num_found[numbers.index(row[pos])] = True
            else:
                return True
        else:
            return True
    return False

#for checking if sub grids are valid
def subgrid(grid):
    '''Checks suduko subgrids for duplicates. Returns True if duplicates found'''
    temp_row = []
    for i in range(3): #vertical sub grid number
        for j in range(3): #horizontal sub grid number
            for row in range(3):
                for col in range(3):
                    temp_row.append(grid[row+j*3][col+i*3])
            if duplicate(temp_row):
                return True
    return False

lines = [0]*9
valid = True
#getting nine lines of suduko grid
for i in range(9):
    lines[i] = [int(j) for j in input()]
#checking rows for duplicates
for row in range(9):
    if duplicate(lines[row]):
        valid = False
        break

#checking coloumns for duplicates
for row in range(9):
    temp_row = []
    for col in range(9):
        temp_row.append(lines[col][row])
    if duplicate(temp_row):
        valid = False
        break

#checking subgrids for duplicates
    if subgrid(lines):
        valid = False

if not valid:
    print('Sudoku grid is not valid')
else:
    print('Sudoku grid is valid')
