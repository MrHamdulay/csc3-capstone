# Assignment 9 Question 3
# James Behr
# 2014-05-12

def validate_line(line):
    '''Validate a list of numbers against Soduko rules. A list 9 numbers long 
    should contain each number 1 - 9 exactly once'''
    for i in range(1, len(line) + 1):
        if line.count(i) != 1:
            return False
    return True

def validate(grid):
    # Validate row
    for row in grid:
        if not validate_line(row):
            return False
        
    # Validate column
    for x in range(9):
        # Create a column list for each column
        column = [grid[i][x] for i in range(9)]
        if not validate_line(column):
            return False
    
    # Validate 3x3 grids
    for n in range(0, 9, 3):
        for m in range(0, 9, 3):
            minigrid = []
            # Create the 9 3x3 grids from each part of the grid
            # We need them in the form of a list 9 entries long
            for y in range(n, n + 3):
                for x in range(m, m + 3):
                    minigrid.append(grid[y][x])
                    
            # Now use the validate_line function
            if not validate_line(minigrid):
                return False
            
    # It must be valid, therefore
    return True
            
grid = []
for y in range(9):
    line = input()
    # Use a list comprehension to create a 2x2 array
    grid.append([int(c) for c in line])

if validate(grid):
    print('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')
