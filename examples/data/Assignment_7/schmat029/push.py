#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     creates push functions for 2048
#
# Author:      Matthias
#
# Created:     27-04-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def pushing(list1, list2):
    """ the actual function that does the pushing
    and is independent of the direction """
    for i in range(len(list1)-1): # don't have to check the last value in list1
        if list1[i] == list1[i+1]:
            # double the value of list1[i] and delete the following value
            list1[i] = 2 * list1[i]
            list1[i+1] = 0
    for term in list1:
        # loop through list1 again and add all non-zero values that are left
        if term != 0:
            list2.append(term)
    return list1, list2

def push_up(grid):
    for column in range(4):
        list1 = [] # for storing values after eliminating zeros
        list2 = [] # for storing values after combining terms
        for row in range(4):
            if grid[row][column] != 0:
                # append all non-zero values to list1
                list1.append(grid[row][column])
            # delete the values in the current column
            grid[row][column] = 0
        # use pushing function to update list1 and list2
        list1, list2 = pushing(list1, list2)
        for i in range(len(list2)):
            # loop through list2 and add the values to the current column in grid
            grid[i][column] = list2[i]
    return grid

def push_down(grid):
    for column in range(4):
        list1 = [] # for storing values after eliminating zeros
        list2 = [] # for storing values after combining terms
        for row in range(3,-1,-1): # loop backwards through the column
            if grid[row][column] != 0:
                # append all non-zero values to list1
                list1.append(grid[row][column])
            # delete the values in the current column
            grid[row][column] = 0
        #use pushing function to update list1, list2
        list1, list2 = pushing(list1, list2)
        for i in range(len(list2)):
            # loop through list2 and add the values to the current column in grid
            grid[3-i][column] = list2[i]
    return grid

def push_left(grid):
    for row in range(4):
        list1 = [] # for storing values after eliminating zeros
        list2 = [] # for storing values after combining terms
        for column in range(4):
            if grid[row][column] != 0:
                # append all non-zero values to list1
                list1.append(grid[row][column])
            # delete the values in the current row
            grid[row][column] = 0
        # use pushing function to update list1 and list2
        list1, list2 = pushing(list1, list2)
        for i in range(len(list2)):
            # loop through list2 and add the values to the current row in grid
            grid[row][i] = list2[i]
    return grid

def push_right(grid):
    for row in range(4):
        list1 = [] # for storing values after eliminating zeros
        list2 = [] # for storing values after combining terms
        for column in range(3,-1,-1): # loop backwards through the row
            if grid[row][column] != 0:
                # append all non-zero values to list1
                list1.append(grid[row][column])
            # delete the values in the current row
            grid[row][column] = 0
        # use pushing function to update list1 and list2
        list1, list2 = pushing(list1, list2)
        for i in range(len(list2)):
            # loop through list2 and add the values to the current row in grid
            grid[row][3-i] = list2[i]
    return grid