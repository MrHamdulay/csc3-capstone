#AMNTAS003  #Tashfia Amin   #2 May 2014
#Question 3: Assignment 7   #Move values in the 2048 game so that they merge if the same value

#Add the values when pushed downwards if the same number of push down if not
def push_down (grid):
    for i in range(3):
        for row in range(2,-1,-1):
            for column in range(3,-1,-1):
                if grid [row+1] [column] == 0:                              #Move all values to the bottom if nothing in column or no same values
                    grid [row+1] [column] = grid [row] [column]
                    grid [row] [column] = 0
    for row in range(2,-1,-1):
        for column in range(3,-1,-1):
                if grid [row+1] [column] == grid [row] [column]:            #Merge and double values if the same downwards
                    grid [row+1] [column] = grid [row+1] [column]*2
                    grid [row] [column] = 0
    for row in range(2,-1,-1):
        for column in range(3,-1,-1):
            if grid [row+1] [column] == 0:
                grid [row+1] [column] = grid [row] [column]
                grid [row] [column] = 0
    return grid

#Add the values when pushed leftwards if values are the same or push to the left if not
def push_left (grid):
    for i in range(3):
        for row in range(4):
            for column in range(1,4):
                if grid [row] [column-1] == 0:                              #Move values leftwards if no values or no same values
                    grid [row] [column-1] = grid [row] [column]
                    grid [row] [column] = 0
    for row in range(4):
        for column in range(1,4):
            if grid [row] [column-1] == grid [row] [column]:                #Merge values and double if the same value leftwards
                grid [row] [column-1] = grid [row] [column-1]*2
                grid [row] [column] = 0
    for row in range(4):
        for column in range(1,4):
            if grid [row] [column-1] == 0:
                grid [row] [column-1] = grid [row] [column]
                grid [row] [column] = 0
    return grid

#Add the values when pushed upwards if the values are the same or push to the right if not
def push_up (grid):
    for i in range(3):
        for row in range(1,4):
            for column in range(4):
                if grid [row-1] [column] == 0:                              #Move all values to the bottom if no same values
                    grid [row-1] [column] = grid [row] [column]
                    grid [row] [column] = 0
    for row in range(1,4):
        for column in range(4):
                if grid [row-1] [column] == grid [row] [column]:            #Merge and double value if the same values upwards
                    grid [row-1] [column] = grid [row-1] [column]*2
                    grid [row] [column] = 0
    for row in range(1,4):
        for column in range(4):
            if grid [row-1] [column] == 0:
                grid [row-1] [column] = grid [row] [column]
                grid [row] [column] = 0
    return grid

#Add the values rightwards if the values are the same or push to the right if not
def push_right (grid):
    for i in range(3):
        for row in range(3,-1,-1):
            for column in range(2,-1,-1):
                if grid [row] [column+1] == 0:                              #Move all values rightwards if no values or no same values
                    grid [row] [column+1] = grid [row] [column]
                    grid [row] [column] = 0
    for row in range(3,-1,-1):
        for column in range(2,-1,-1):
            if grid [row] [column+1] == grid [row] [column]:                #Merge and double values if the same rightwards
                grid [row] [column+1] = grid [row] [column+1]*2
                grid [row] [column] = 0
    for row in range(3,-1,-1):
        for column in range(2,-1,-1):
            if grid [row] [column+1] == 0:
                grid [row] [column+1] = grid [row] [column]
                grid [row] [column] = 0
    return grid