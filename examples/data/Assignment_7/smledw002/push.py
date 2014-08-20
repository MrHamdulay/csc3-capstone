#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 2014-05-01
#Function       : Merges values in a grid that are adjacent
#Title          : Push


def array_merger(extracted_list, orientation):
    """finds two adjacent values in an extracted list and adds them together towards the left"""
    if orientation.lower() == "reversed":
        #reverses the list if its shifted right or down
        extracted_list.reverse()

    #remove zero values
    while 0 in extracted_list:
        extracted_list.remove(0)

    temporary_list = []

    while len(extracted_list) != 0:
        if len(extracted_list) != 1:
            #removes two adjacent values from a list and adds there sum to a temporary list
            if extracted_list[0] == extracted_list[1]:
                temporary_list.append(extracted_list[0] * 2)
                extracted_list.remove(extracted_list[0])
                extracted_list.remove(extracted_list[0])
            else:
                #moves a value that has no equal adjacent values to a temporary list
                temporary_list.append(extracted_list[0])
                extracted_list.remove(extracted_list[0])

        else:
            temporary_list.append(extracted_list[0])
            extracted_list.remove(extracted_list[0])

    #adds the zero values that were removed
    while len(temporary_list) != 4:
            temporary_list.append(0)

    if orientation.lower() == "reversed":
        temporary_list.reverse()
    return temporary_list


def push_left(grid):
    """shifts the grid left and adds equal adjacent values in the grid"""

    row_number = 0

    for row in grid:
        #adds adjacent values
        row = array_merger(row, "forward")
        #replaces the old row in a grid with the shifted one
        grid[row_number] = row
        #keeps track of the row number
        row_number += 1


def push_right(grid):
    """shifts the grid right and adds equal adjacent values in the grid"""
    row_number = 0
    for row in grid:
        row = array_merger(row, "reversed")
        #replaces the old row with the altered one
        grid[row_number] = row
        row_number += 1


def push_down(grid):
    """shifts the grid down and adds equal adjacent values in the grid"""
    for x in range(4):
        temporary_list = []
        for y in range(4):
            #adds all values in column to a list
            temporary_list.append(grid[y][x])

        temporary_list = array_merger(temporary_list, "reversed")

        #replaces old values in the column with the altered ones
        for z in range(4):
            grid[z][x] = temporary_list[z]


def push_up(grid):
    """shifts the grid up and adds equal adjacent values in the grid"""
    for x in range(4):
        temporary_list = []

        for y in range(4):
            #adds all values in column to a list
            temporary_list.append(grid[y][x])
        temporary_list = array_merger(temporary_list, "forward")
        for z in range(4):
            grid[z][x] = temporary_list[z]
