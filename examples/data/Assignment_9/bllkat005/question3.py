""" Study Arrays
    Kate Bell
    BLLKAT005 """

def test(grid):
    valid = True
    
    #check all numbers from 1 to 9 appear in each row
    for i in range(1,9):
        for row in range(9):
            if not i in grid[row]: valid = False
        
    #invert grid such that columns become rows...   
    test_columns = []    
    for j in range (9):
        test_columns.append ([0] * 9)
     
    for row in range(9):
        for column in range(9):
            test_columns[row][column]=grid[column][row]
            
    # ...then test that all numbers from 1 to 9 appear in each row i.e. grid's column    
    for i in range(1,9):
            for row in range(9):
                if not i in test_columns[row]: valid = False   
    
    # create new 2d array with sub-grids as 'rows'
    test_subs = []
    for k in range (9):
                test_subs.append ([0] * 9)  
        
    for i in range (9):
            for column in range(9):
                test_subs[i][column]=grid[column//3+(i%3)*3][column%3+(i//3)*3]
    
    #check all numbers from 1 to 9 appear in each 'row' i.e. sub-grid
    for i in range(1,9):
        for row in range(9):
            if not i in test_subs[row]: valid = False
    
    return valid


#create 2d array
grid = []
height = 9
width = 9
for i in range (height):
    grid.append ([0] * width)

#Input into array
for i in range(height):
    numbers = input()
    for j in range(width):
        grid[i][j]=eval(numbers[j])
    
# invoke function to test if grid is valid sudoku solution     
if test(grid)== True:
    print("Sudoku grid is valid")
else: print("Sudoku grid is not valid")