"""Question 3 of Assignment 9: Checks whether an input sudoku grid is valid
SWNREI001
2014/05/11"""

def isValid(elements):
    """Checks for validity by checking for repeats in supplied list"""
    found = []
    # store found values in elements
    for elem in elements:
        if elem in found:
            return False
        else:
            found.append(elem)
    return True

def checkRows(grid):
    """Checks that each row in grid is valid; True if so, False if not"""
    for row in grid: # goes through 9x9 grid row by row
        if not isValid(row):
            return False
    return True

def checkColumns(grid):
    """Checks that each column in grid is valid; True if so, False if not"""
    columns = [[[] for i in range(len(grid[0]))]for i in range(len(grid))] # transpose grid into a list of columns (9x9)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            columns[j][i] = grid[i][j]
    # check each column for validity
    for col in columns:
        if not isValid(col):
            return False
    return True

def checkGrids(grid):
    """Checks each 3x3 grid in the supplied 9x9 grid"""
    grids = []
    for i in [0, 3, 6]:
        grids.append(grid[i][0:3] + grid[i+1][0:3] + grid[i+2][0:3])
        grids.append(grid[i][3:6] + grid[i+1][3:6] + grid[i+2][3:6])
        grids.append(grid[i][6:9] + grid[i+1][6:9] + grid[i+2][6:9])
    for g in grids: # check each generated grid for validity
        if not isValid(g):
            return False
    return True
    
def main():
    """Main function of question3.py"""
    grid = [] # store 9x9 grid of values
    for i in range(9):
        temp = []
        # collect values from a single line into a list
        for char in input():
            temp.append(eval(char))
        # add list to grid
        grid.append(temp)
    if checkRows(grid) and checkColumns(grid) and checkGrids(grid):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
    
if __name__ == "__main__":
    main()