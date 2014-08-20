"""Mishka Latib
programme for 2048
02 May 2014"""

import util

def push_up(grid):
    #Defined function to merge grid values up
    for x in range(4):
        column = []
        for y in range(4):
            column.append(grid[y][x])
            delete_number = 0
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
        for y in range(4):
            grid[y][x] = column[y]
            
def push_down(grid):
    #Defined function to merge grid values down
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
            
