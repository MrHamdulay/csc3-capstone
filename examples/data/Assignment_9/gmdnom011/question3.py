# Program to check a Sudoku grid
# Nomsa Gamedze
# 11 May 2014

def get_grid():
    lines = []
    for x in range(9):
        lines.append([])
    for i in range(9):
        lines[i] = list(input(""))
    return lines
    
def check_lines(lines):
    answer = True
    for i in lines:
        for c in range(9):
            c_s = str(c)
            if i.count(c_s) > 1:
                answer = False
    return answer

def get_vertical(lines):
    answer = True
    vert = []
    for x in range(9):
        vert.append([])
    for i in range(9):
        for c in range(9):
            vert[i].append(lines[i][c])
    return vert

def get_subgrid(grid):
    subgrids = []
    for i in range(9):
        subgrids.append([])
    for x in range(9):
        for i in (0, 3, 6):
            for c in (i, i+1, i+2):
                subgrids[x].append(grid[i][c])
                subgrids[x].append(grid[i+1][c])
                subgrids[x].append(grid[i+2][c])
    return subgrids

            
def main():
    grid = get_grid()
    if check_lines(grid):
        vert_lines = get_vertical(grid)
        if check_lines(vert_lines):
            subgrids = get_subgrid(grid)
            if check_lines(subgrids):
                print("Sudoku grid is valid")
            else:
                print("Sudoku grid is not valid")
        else:
            print("Sudoku grid is not valid")        
    else:
        print("Sudoku grid is not valid")
    
main()