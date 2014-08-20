#Ali Goldstein
#program to check if a complete Sudoku grid is valid or not.
#16 May 2014

#creating a function to check if the sudoku grid is valid or not
#if valid,returns a boolean of True, if not valid, returns False
def is_valid(grid):
    if len(grid)==9:
        for row in range(9):
            for col in range(9):
                if (grid[row][col]!=grid[row+1][col]) and (grid[row][col]!=grid[row][col+1]):
                    return True
                else:
                    return False
    else:
        return False

#creating an empty list
grid=[]
#adding each line to the grid
for i in range(9):
    num=input("")
    grid.append(num)
        
#calling the function
#printing whether or not the sudoku is valid
if is_valid(grid) == True:
    print("Sudoku grid is valid")
if is_valid(grid) == False:
    print("Sudoku grid is not valid")
        