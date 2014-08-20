# Student Number: PRTNIC017
# Date: 5/13/14

def is_valid(grid):
    # --- VALIDATE ROWS ---
    for row in grid:
        if len(row) != 9:  # Rows must be 9 elements long
            return False
        # check that every number from 1 to 9 occurs once
        for n in range(1, 10):
            if row.count(n) != 1:
                return False

    # --- VALIDATE COLUMNS ---
    # firstly check if there are 9 rows
    if len(grid) != 9:
        return False
    # then check very column
    for c in range(len(grid[0])):
        col = [grid[0][c], grid[1][c], grid[2][c], grid[3][c], grid[4][c], grid[5][c], grid[6][c], grid[7][c],
               grid[8][c]]
        # once again check that every number from 1 to 9 occurs only once
        for n in range(1, 10):
            if col.count(n) != 1:
                return False

    # --- VALIDATE BLOCKS ---
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [grid[i][j], grid[i][j + 1], grid[i][j + 2], grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                     grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]]
            # ...and again check that every number from 1 to 9 occurs only once
            for n in range(1, 10, 1):
                if block.count(n) != 1:
                    return False
    # --- VALID ---
    return True


if __name__ == '__main__':
    # Input
    grid = []
    for l in range(9):
        grid.append([])
        line = list(input(''))
        for el in line:
            grid[-1].append(int(el))

    if is_valid(grid):
        print('Sudoku grid is valid')
    else:
        print('Sudoku grid is not valid')

