# Sudoku grid check
# Nevarr Pillay - PLLNEV006
# 12 May 2014

grid = [] # Grid to store the numbers of the Sudoku grid       

def Sudoku(string):
    """Function to add all characters of the string to the grid"""
    grid.append([])
    for i in string:
        grid[-1].append(i) # Places all the characters in the last grid  
    
def checkrow(grid):
    """Checks all the rows in a grid for duplicates and returns a boolean variable"""
    check = True
    for i in range(len(grid)): # Checks all the rows
        for j in range(len(grid[i])): # Checks all charcters in given row
            for k in range(len(grid[i])): # Another loop to check all the characters in given row 
                if grid[i][j] == grid[i][k] and j != k: # If a duplicate is found
                    check = False
    return check

def check3x3(grid):
    """Checks all the 3x3 grids in a grid for duplicates and returns a boolean variable"""
    check = True
    for a in range(3): # Divides the grid into 3 rows
        for b in range(3): # Divies the grid into 3 coloums
            for i in range(a*3,a*3 + 3): # Loop for rows that starts at 3 times the a value and ends 3 places later     
                for z in range(a*3,a*3+3): # Another loop for rows that starts at 3 times the a value and ends 3 places later to serve as check
                    for j in range(b*3,b*3 + 3): # Loop for coloums that starts at 3 times the a value and ends 3 places later
                        for k in range(b*3,b*3 + 3): # Another loop for columns that starts at 3 times the a value and ends 3 places later to serve as check
                            if grid[i][j] == grid[z][k] and k != j: # If a duplicate is found
                                check = False
    return check            

def checkcol(grid):
    """Checks all the coloumns in a grid for duplicates and returns a boolean variable"""
    check = True
    for i in range(len(grid[0])): # Checks all the rows
        for j in range(len(grid)): # Checks all charcters in given coloum
            for k in range(len(grid)): # Another loop to check all the characters in given coloum 
                if grid[j][i] == grid[k][i] and j != k: # If a duplicate is found
                    check = False
    return check             
    
def main():
    for i in range(9):
        line = input()
        Sudoku(line)
    if check3x3(grid) == False or checkrow(grid) == False or checkcol(grid) == False: # If any of the checks are false
        print("Sudoku grid is not valid")
    else:
        print("Sudoku grid is valid")
        
if __name__ == "__main__":
    main()  

