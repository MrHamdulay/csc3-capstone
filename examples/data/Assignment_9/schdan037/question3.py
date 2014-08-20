"""Daniel Schwartz
SCHDAN037
question 3
may 2014"""


def main():
    """main"""
    lines = []
    for i in range(9):
        lines.append(input())

    grid = []
    for line in lines:
        temp = []
        for number in line:
            temp.append(int(number))
        grid.append(temp)

    valid = True
    #row checks
    for row in grid:
        used = ""
        unique = True
        for item in row:
            if str(item) in used:
                unique = False
            else:
                used += str(item)
        if not unique:
            valid = False

    #column check
    for col in range(9):
        used = ""
        unique = True
        for row in range(9):
            if str(grid[row][col]) in used:
                unique = False
            else:
                used += str(grid[row][col])
        if not unique:
            valid = False

    #sub-grid check
    sub_grids = []
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            row_1 = [grid[i][j], grid[i][j+1], grid[i][j+2]]
            row_2 = [grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2]]
            row_3 = [grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
            sub_grids.append([row_1, row_2, row_3])

    for sub_grid in sub_grids:
        used = ""
        unique = True
        for row in sub_grid:
            for item in row:
                if str(item) in used:
                    unique = False
                else:
                    used += str(item)
        if not unique:
            valid = False

    # valid check
    if valid:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")


if __name__ == "__main__":
    main()