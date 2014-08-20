"""check if won sudoku
Anna Borysova
2014-05-12"""

def check_rows(grid):
    """check if rows have only one occurence of value"""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            #check only part of row that has not been checked
            if grid[row][col:].count(grid[row][col]) != 1:
                return False
    return True

def transpose(grid):
    """swap rows and columns"""
    transpose = []
    for i in range(len(grid)):
        row=[]
        for j in range(len(grid[i])):
            row.append(grid[j][i])
        transpose.append(row)
    return transpose

def check_columns(grid):
    """check if columns have only one occurence of value"""
    grid = transpose(grid)
    return check_rows(grid)

def make_subgrids(grid):
    """make lists of values in subgrids"""
    subgrids = []
    for j in range(3):
        subgrid=[]
        for i in range(3):
            # slice third of row, append to grid
            for num in grid[i][j*3:j*3+3]:
                subgrid.append(num)
        subgrids.append(subgrid)
    return subgrids
        
def check_won(grid):
    """check sudoku grid's columns, rows and subgrids"""
    if check_rows(grid) and check_columns(grid) and check_rows(make_subgrids(grid)):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
        
# get input
inputstr = []
for i in range(9):
    inputstr.append(input())

# make 2d grid of ints    
grid = []    
for i in range(len(inputstr)):
    row = []
    for j in inputstr[i]:
        row.append(int(j))
    grid.append(row)

check_won(grid)