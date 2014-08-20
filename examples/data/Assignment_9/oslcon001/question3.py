# checks if a complete Sudoku grid is valid or not
# Conor O'Sullivan
# 10/05/2014



"""Write a program to .

A Sudoku grid is a 9x9 grid of integers, with each cell containing an integer value from 1-9. The input to your program is a set of nine lines, each containing 9 single digit integers with no intervening spaces. Your program must store these integers internally in a 2-dimensional array.

In a correct Sudoku solution, the following conditions hold:

no 2 cells in the same row have the same value
no 2 cells in the same column have the same value
no 2 cells in the same 3x3 sub-grid have the same value - this is tested for the 9 non-overlapping sub-grids that a 9x9 grid can be divided into


Sample I/O:

359716482
867345912
413928675
398574126
546281739
172639548
984163257
621857394
735492861
Sudoku grid is not valid
Sample I/O:

259716483
867345912
413928675
398574126
546281739
172639548
984163257
621857394
735492861
Sudoku grid is valid"""
# Main function - creates and populates 2d array
def main():
              grid = []
              for row in range(9):
                            grid.append([0]*9)

              for row in range(9):
                            
                            ingrid = input("")
                            for col in range(9):
                                          grid[row][col] = ingrid[col]
              
              if check_row(grid) == True and check_col(grid) == True and check_3x3(grid) == True:
                            print("Sudoku grid is valid")
              else:
                            print("Sudoku grid is not valid")

def check_row(grid):
              for row in range(9):        
                            for x in range(9):
                                          if grid[row].count(str(x+1)) == 0:
                                                        return False
                                          
              return True
              
def check_col(grid):
              col_grid = []
              for row in range(9):  
                            col_grid = []
                            for col in range(9):
                                          col_grid.append(grid[col][row])
                            for x in range(9):
                                          if col_grid.count(str(x+1)) == 0:
                                                        return False
              
              return True 
#Checks the 3x3 grids
def check_3x3(grid):
              for col in range(0,9,3):
                            for row in range(0,9,3):
                                          grid_3x3 = []
                                          for col_temp in range(3):
                                                        for row_temp in range(3):
                                                                      grid_3x3.append(grid[col+col_temp][row+row_temp])
                                          for x in range(9):
                                                        if grid_3x3.count(str(x+1))>1:
                                                                      return False
                            
              
              return True
main()