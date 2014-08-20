"""Akhil Singh
SNGAKH004
30 April 2014"""
import util

def push_up(grid):
    #Defined function to merge grid values up
    #Take the grid values from each column and temporarily store each value
    for x in range(4):
        column = []
        for y in range(4):
            column.append(grid[y][x])
        #Take out all zeroes prior to the significant numbers. Variable delete_number is an accumulator which allows for the deletion of successive zeroes.
            delete_number = 0
        for number in range(3):
            if column[number-delete_number] == 0:
                del column[number-delete_number]
                column.append(0)
                delete_number += 1
        #Going from top to bottom in the original grid, add equal numbers that are together and store the sum in the upper of the two blocks.
        for number in range(3):
            if column[number] == column[number+1]:
                column[number] = column[number]+column[number+1]
                del column[number+1]
                column.append(0)
        #Copy each new column onto the original grid.
        for y in range(4):
            grid[y][x] = column[y]
            
def push_down(grid):
    #Defined function to merge grid values down
    #Follows the same code as function "push_up(grid)" but uses the list reverse function such that zeroes are deleted and blocks added from bottom to top.
    for x in range(4):
        column = []
        for y in range(4):
            column.append(grid[y][x])
            delete_number = 0
        column.reverse()
        for number in range(3):
            if column[number-delete_number] == 0:
                del column[number-delete_number]
                column.append(0)
                delete_number += 1
        for number in range(3):
            if column[number] == column[number+1]:
                column[number] = column[number]+column[number+1]
                del column[number+1]
                column.append(0)
        column.reverse()
        for y in range(4):
            grid[y][x] = column[y]

def push_left(grid):
    #Defined function to merge grid values to theleft
    for y in range(4):
        row = []
        for x in range(4):
            row.append(grid[y][x])
            delete_number = 0
        for number in range(3):
            if row[number-delete_number] == 0:
                del row[number-delete_number]
                row.append(0)
                delete_number += 1
        for number in range(3):
            if row[number] == row[number+1]:
                row[number] = row[number]+row[number+1]
                del row[number+1]
                row.append(0)
        for x in range(4):
            grid[y][x] = row[x]
            
def push_right(grid):
    #defined function to merge grid values to the right
    for y in range(4):
        row = []
        for x in range(4):
            row.append(grid[y][x])
            delete_number = 0
        row.reverse()
        for number in range(3):
            if row[number-delete_number] == 0:
                del row[number-delete_number]
                row.append(0)
                delete_number += 1
        for number in range(3):
            if row[number] == row[number+1]:
                row[number] = row[number]+row[number+1]
                del row[number+1]
                row.append(0)
        row.reverse()
        for x in range(4):
            grid[y][x] = row[x]            
            
