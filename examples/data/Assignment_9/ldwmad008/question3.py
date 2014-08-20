def invalid():
    print('Soduku grid is not valid')

def valid():
    print('Soduku grid is valid')

def grid():
    grid = []
    for i in range(9):
        rows = input('')
        grid.append(rows)
    row_check(grid)
    
def row_check(grid):
    check = True
    for i in range(len(grid)):
        row_c = []
        row = grid[i]
        for i in range(len(row)):
            row_c.append(row[i])
        row_c.sort()
        for i in range(len(row_c)):
            row_c[i] = eval(row_c[i])
        for i in range(8):
            if row_c[i] == row_c[i + 1]:
                check = False
        if check:
            continue
        else:
            return invalid()
    return grid_check(check)
        
def grid_check(grid):
    check = True
    grid_n = 0
    grid_i = 3
    i = 0
    while i != 3:
        grid_l = []
        row_c = []
        row1 = grid[grid_n]
        row2 = grid[grid_n + 1]
        row3 = grid[grid_n +2]
        for i in range(3):
            row_c.append(row1[grid_n:grid_i])
            row_c.append(row2[grid_n:grid_i])
            row_c.append(row3[grid_n:grid_i])
            ''.join(row_c)
            for i in range(9):
                grid_l.append(row_c[i])
                for i in range(8):
                    if row_c[i] == row_c[i + 1]:
                            check = False
                    if check:
                        continue
                    else:
                        return invalid()
        i += 1
        grid_n += 3
        grid_i += 3
    return valid()

grid()