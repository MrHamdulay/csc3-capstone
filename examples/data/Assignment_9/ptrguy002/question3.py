#check row
def check(grid):
    for i in range(9):
        vals = set()
        for ch in grid[i]:
            if ch in vals:
                return False
            vals.add(ch)

    for i in range(9):
        vals = set()
        for j in range(9):
            if grid[j][i] in vals:
                return False
            vals.add(grid[j][i])

    for i in range(3):
        for j in range(3):
            vals = set()
            for ii in range(i*3, i*3+3):
                for jj in range(j*3, j*3+3):
                    if grid[ii][jj] in vals:
                        return False
                    vals.add(grid[ii][jj])

    return True

#input
print("Sudoku grid is", "valid" if check(list(map(lambda x: input(), range(9)))) else "not valid")
