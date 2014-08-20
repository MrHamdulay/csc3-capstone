"""checks whether an inputted Sudoku grid is valid or not
Jonathan Nathan
10 may 2014"""

grid = []

# appends input to 2D grid list
for i in range (9):
    grid.append(([input('')]))

                      
def valid(grid):
    """validity checks for Sudoku square"""
    # checks no 2 cells in the same row have the same value, by checking each row's numbers with a list of numbers in that same row
    row_test_list = []
    for line in grid:
        for i in range (9):
            if int(line[0][i]) in row_test_list:
                return False
            else:
                row_test_list.append(int(line[0][i])) 
        row_test_list = []
            
    # checks no 2 cells in the same column have the same value, by checking each column's numbers with a list of numbers in that same column
    column_test_list = []
    for i in range (9):
        for j in range (9):
            if int(grid[j][0][i]) in column_test_list:
                return False
            else:
                column_test_list.append(int(grid[j][0][i]))
        column_test_list = []
        
    # checks no 2 cells in the same 3x3 sub-grid have the same value    
    subgrid_test_list = []
    for g in [0,3,6]:
        for h in [0,3,6]:
            for i in range (3):
                for j in range(3):
                    if int(grid[i + g][0][j + h]) in subgrid_test_list:
                        return False
                    else:
                        subgrid_test_list.append(int(grid[i + g][0][j + h]))
            subgrid_test_list = []
           
           
           
if valid(grid) is False:
    print("Sudoku grid is not valid")
else: print("Sudoku grid is valid")