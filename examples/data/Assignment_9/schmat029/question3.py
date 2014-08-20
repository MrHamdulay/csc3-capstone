#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     checks whether a sudoko solution is valid
#
# Author:      Matthias
#
# Created:     12-05-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

sudoku = []
for i in range(9):
    sudoku.append(input("\n"))

def check(array):
    want = ["1","2","3","4","5","6","7","8","9"]
    have = []
    for num in array:
        if num not in want:
            # not an integer between 1 and 9
            return False
        elif num in have:
            #duplicate
            return False
        else:
            have.append(num)
    # nothing wrong
    return True

def check_row(grid):
    # checks if each row contains the integers 1-9 only once
    for row in range(9):
        numbers = []
        for column in range(9):
            numbers.append(grid[row][column])
        if not check(numbers):
            # check returned False
            return False
    # every row passed the check
    return True

def check_column(grid):
    # checks if each column contains the integers 1-9 only once
    for column in range(9):
        numbers = []
        for row in range(9):
            numbers.append(grid[row][column])
        if not check(numbers):
            # check returned False
            return False
    # every row passed the check
    return True

def check_squares(grid):
    # divides grid into 9 3x3 blocks and checks each one individually
    # iterates from left to right and from top to bottom
    min_row = 0
    min_column = 0
    numbers = []
    for max_row in range(3,10,3):
        # indicates the upper limit for row (3,6,9)
        for max_column in range(3,10,3):
            # indicates the upper limit for column (3,6,9)
            for row in range(min_row,max_row):
                # always loops three times
                for column in range(min_column,max_column):
                    # also loops three times
                    numbers.append(grid[row][column])
            if not check(numbers):
                # check returned False
                return False
            # reset numbers - new 3x3 block
            numbers = []
            # increase lower column limit
            min_column = column + 1
        # increase lower row limit
        min_row = row + 1
        # reset column limit - new 3x9 chunk
        min_column = 0
    # every square passed the test
    return True

if check_row(sudoku) and check_column(sudoku) and check_squares(sudoku):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")

