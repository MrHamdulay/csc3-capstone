""" A program to check if a complete Sudoku grid is valid or not.
Author: Afika Nyati
Date: 10th May 2014"""


def main():
    
    grid = sudoku_grid()    # Assigns a sudoku grid created by the sudoku_grid function to a variable.

    print(check_complete(grid))     # Prints the result of whether the Sudoku grid is valid or not, which is returned by a fuction called check_complete.




def sudoku_grid():      # A function that creates a 2D Array representing a Sudoku grid.
    
    grid = []       # Initializes the Sudkou grid variable.   
    
    
    for line in range(9):   # A definite loop that continues as long as it gets line input and adds each line to the Sudoku grid variable.
        
        list_line = []
        
        line = input()      # Asks the user for the first line of the Sudoku grid.
        
        for i in range(len(line)):      # A definite loop that splits the string of numbers into individual strings to store in the line list.
                    
                    list_line.append(line[i:i+1])       # Appends the current number to the line list.        
            
        grid.append(line)       # Appends the current line list to the Sudooku grid. 

    
    return grid     # Returns the Sudoku grid.
            



def check_complete(grid):       # A function that checks whether a Sudoku grid is valid or not.
    
    # Check rows:
    for y in range(9):   # A definite loop that checks the all the rows (horizontal) to check if any numbers are the same.
        
        numbers1 = []   # Initializes a list that will add each number the loop processes.
        
        for x in range(9):      # Loops nine times.
            
            if grid[y][x] in numbers1:  # If the current number is in the number list:
                
                return "Sudoku grid is not valid"
            else:   # If the current number is not in the number list:
                numbers1.append(grid[y][x])     # Add the number to the number list.
                
    # Notice that the x's represent the columns and the y's represent the rows. The x loop is nested in the y loop, therefore the columns of each row are checked.
                
    # Check columns:
    
    for x in range(9):      # A definite loop that checks the all the rows (horizontal) to check if any numbers are the same.
        
        numbers2 = []       # Initializes a list that will add each number the loop processes.
        for y in range(9):      # Loops nine times.
                
            if grid[y][x] in numbers2:      # If the current number is in the number list:
                
                return "Sudoku grid is not valid"
            else:       # If the current number is not in the number list:
                numbers2.append(grid[y][x])     # Add the number to the number list.
   
    # Notice that the x's represent the columns and the y's represent the rows. The y loop is nested in the x loop, therefore the rows of each column are checked.                
    
    # Check Blocks:
    
    for down in range (0,9,3):      # A definite loop that checks the all the rows (horizontal) of 3x3 blocks to check if any numbers are the same.
        
        for right in range(0,9,3):      # A definite loop that checks the all the columns (vertical) of 3x3 blocks to check if any numbers are the same.
            
            numbers = []    # Initializes a list that will add each number the loop processes.
            
            # This x and y matrix represents a 3x3 grid within the Sudoku grid.
            
            for y in range(3):       # A definite loop that checks the three vertical numbers in one block to check if any numbers are the same.
                    
                for x in range(3):      # A definite loop that checks the three horizontal numbers in one block to check if any numbers are the same.
                    
                
                        
                    if grid[down + y][right + x] in numbers:    # If the current number is in the number list:
                            
                        return "Sudoku grid is not valid"  
                    else:       # If the current number is not in the number list:
                        numbers.append(grid[down + y][right + x])       # Add the number to the number list.
                        
            
            numbers = []       # Reinitializes the numbers variables to zero.
        
        
    else: return "Sudoku grid is valid"

        
main()