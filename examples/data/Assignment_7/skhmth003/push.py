#Function that pushes blocks up,down,left or right
#Gordon Skhosana
#2/05/2014
height=4
grid = [[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]]
def push_up (grid):
    """merge grid values upwards"""
    tmp_grid=[]
    for row in range(height):
        for col in range(height):
            print(row)
            print(col)
            if grid[row][col]!=" ":
                tmp_grid.append(grid[row][col])
    print(tmp_grid)
    util.print_grid(grid)
push_up (grid)