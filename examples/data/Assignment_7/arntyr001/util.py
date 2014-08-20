def create_grid(grid):
    """create a 4x4 grid"""
    grid = []
    length = 4
    
    for i in range(length):
        grid.append([" "] * 4)

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    column = 5
    row = 5
    for i in range(column):
        if i == 0 or i == 5:
            print("+")
        else:
            print("|\n")
    
    for i in range(row):
        if i == 0 or i == 5:
            pass
        else:
            print("--")
            
