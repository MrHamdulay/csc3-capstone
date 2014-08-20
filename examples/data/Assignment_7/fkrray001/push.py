# Author : Rayaan Fakier FKRRAY001
# Date : 30 - 04 - 2014
# push.py

import util

def push_left(grid):
    
    for row in range(4):
        # Creates a temporary list of row values
        row_vals = []
        for value in range(4):
            row_vals.append(grid[row][value])
        # Moves numbers to end
        for nums in range(4):
            if row_vals[nums] == 0:
                row_vals.remove(0)
                row_vals.append(0)
        # Adds adjacent nums that are equal
        for num in range(3):
            if row_vals[num] == row_vals[num+1]:
                val_add = row_vals[num+1]
                row_vals.remove(row_vals[num+1])
                row_vals.append(0)
                row_vals[num] += val_add
        # Replaces grid values with new (added) values
        for replacement in range(4):
            grid[row][replacement] = row_vals[replacement]
    return grid

def push_right(grid):
    
    for row in range(4):
        # Creates a temporary list of row values
        row_vals = []
        for value in range(3,-1,-1):
            row_vals.append(grid[row][value])
        # Moves numbers to end
        for nums in range(4):
            if row_vals[nums] == 0:
                row_vals.remove(0)
                row_vals.append(0)           
        # Adds adjacent nums that are equal
        for num in range(3):
            if row_vals[num] == row_vals[num+1]:
                val_add = row_vals[num+1]
                row_vals.remove(row_vals[num+1])
                row_vals.append(0)
                row_vals[num] += val_add
        # Replaces grid values with new (added) values
        rep_place = 0
        for replacement in range(3,-1,-1):
            grid[row][rep_place] = row_vals[replacement]
            rep_place += 1
    return grid

def push_up(grid):
    # Creates a temporary list of column values
    for column in range(4):
        column_vals = []
        for val in range(4):
            column_vals.append(grid[val][column])
        # Moves numbers to end
        for nums in range(4):
            if column_vals[nums] == 0:
                column_vals.remove(0)
                column_vals.append(0)                  
        # Adds nums below that are equal    
        for num in range(3):
            if column_vals[num] == column_vals[num+1]:
                val_add = column_vals.pop(num+1)
                column_vals[num] += val_add
                column_vals.append(0)
        # Replaces grid values with new (added) values
        for k in range (4):
            grid[k][column] = column_vals[k]
    return grid

def push_down(grid):
    # Creates a temporary list of column values
    for column in range(4):
        column_vals = []
        for val in range(3,-1,-1):
            column_vals.append(grid[val][column])
       # Moves numbers to end
        for nums in range(4):
            if column_vals[nums] == 0:
                column_vals.remove(0)
                column_vals.append(0)                  
        # Adds nums above that are equal    
        for num in range(3):
            if column_vals[num] == column_vals[num+1]:
                val_add = column_vals.pop(num+1)
                column_vals[num] += val_add
                column_vals.append(0)
        # Replaces grid values with new (added) values
        rep_place = 0
        for k in range (3,-1,-1):
            grid[rep_place][column] = column_vals[k]
            rep_place += 1
    return grid