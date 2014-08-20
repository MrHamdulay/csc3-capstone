#Assignment 7, Question 3
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Created: 01/05/2014; Modified: 02/05/2014

#This is the list of functions which are used for movement in the 2048.py game.


#Creating function push_up() to move up
#.#Pre-condition: Sum up 2 numbers if they are equal. If number is not equal do nothing.
#.#Post-condition: Move up.
#i represents row
#j represents column
def push_up(grid):
    for j in range(len(grid[0])):
        #Merging values if possible,but only once!
        i = 0
        x = i + 1 #x counts the steps.
        while True: #The loop ends when i > len(grid)
            try:
                if i < len(grid[0]):
                    #Checking if next number is not equal the current number
                    if grid[x][j] and grid[i][j] and grid[i][j] != grid[x][j]:
                        raise IndexError
                    #Checking if next number equals current number
                    elif grid[i][j] and grid[i][j] == grid[x][j]:
                        grid[i][j] *= 2
                        grid[x][j] = 0
                        raise IndexError
                    x += 1 #Update x
                else:
                    break #break out of loop
            except IndexError:#On indexerror, reset. Means enf of grid reach
                i += 1
                x = i + 1
        #Move the values up if value above is 0 and previous value is set to zero if movement is made.
        i = 0 #initiate i
        read = False
        stop = False
        while True:
            try:
                if not grid[i][j] and grid[i + 1][j]:
                    grid[i][j] = grid[i + 1][j]
                    grid[i + 1][j] = 0
                    stop = False
                elif stop and read:
                    break #break out of loop
                i += 1
            except IndexError:#On indexerror, reset. Means enf of grid reach
                stop = read
                read = True
                i = 0
    



#Creating function push_down() to move down. (Basically does push_up function in reverse)
#.#Pre-condition: Sum up 2 numbers if they are equal. If number is not equal do nothing.
#.#Post-condition: Move down.
#i represents row
#j represents column
def push_down(grid):
    for j in range(len(grid[0])):
        #Merge values if equal, but only once.
        i = -1 #Starting from the last row. I should be -1 since it should not work backwards.
        x = i - 1 #x counts the number of steps.
        while True:
            try:
                if i < len(grid) and i != -(len(grid)): #As long as I does not go out of grid, to avoid an infinite loop.
                    #Checking if above number(not zero) is not equal to the current number
                    if grid[x][j] and grid[i][j] and grid[i][j] != grid[x][j]:
                        raise IndexError
                    #Checking if above row number is equal to  the current number
                    elif grid[i][j] and grid[i][j] == grid[x][j]:
                        grid[i][j] *= 2 
                        grid[x][j] = 0
                        raise IndexError
                    x -= 1
                else:
                    break #Break out of loop
            except IndexError:#On indexerror, reset. Means enf of grid reach
                i -= 1
                x = i - 1
        #Move the values down if value above is 0 and previous value is set to zero if movement is made.
        i = -1
        read = False
        stop = False
        while True:
            try:
                if not grid[i][j] and grid[i - 1][j]:
                    grid[i][j] = grid[i - 1][j]
                    grid[i - 1][j] = 0
                    stop = False
                elif stop and read:
                    break #Break out of loop
                i -= 1
            except IndexError:
                stop = read
                read = True
                i = -1
    return(grid)



#push_right is created by a swapping process of i->j, j->i or j->[i - 1] from the push_down function.
#push_right works for the columns.
#i repesents column
#j represents row
def push_right(grid):
    for j in range(len(grid[0])):
        #Merge values if equal, but only once.
        i = -1 #Starts from last column
        x = i - 1
        while True:
            try:
                if i < len(grid) and i != -(len(grid)):
                    #Checking if previous number(not zero) is not equal to the current number
                    if grid[j][x] and grid[j][i] and grid[j][i] != grid[j][x]:
                        raise IndexError
                    #Checking if previous number(not zero) is equal to the current number
                    elif grid[j][i] and grid[j][i] == grid[j][x]:
                        grid[j][i] *= 2
                        grid[j][x] = 0
                        raise IndexError
                    x -= 1
                else:
                    break
            except IndexError: #On indexerror, reset. Means enf of grid reach
                i -= 1
                x = i - 1
        #Move the values right if previous value is 0 then previous value is set to zero if movement is made.
        i = -1
        read = False
        stop = False
        while True:
            try:
                if not grid[j][i] and grid[j][i - 1]:
                    grid[j][i] = grid[j][i - 1]
                    grid[j][i - 1] = 0
                    stop = False
                elif stop and read:
                    break #Break out of loop
                i -= 1
            except IndexError:#On indexerror, reset. Means enf of grid reach
                stop = read
                read = True
                i = -1
    
    return(grid)

#push_left is created by a swapping process of i->j, j->i or j->[i + 1] from the push_up function.
#push_left works for the columns.
#i repesents column
#j represents row
def push_left(grid):
    for j in range(len(grid[0])):
        #Merge values if equal, but only once.
        i = 0 #Start from first column
        x = i + 1
        while True:
            try:
                if i < len(grid):
                    #Checking if next number(not zero) is not equal to the current number
                    if grid[j][x] and grid[j][i] and grid[j][i] != grid[j][x]:
                        raise IndexError
                    #Checking if next number(not zero) is equal to the current number
                    elif grid[j][i] and grid[j][i] == grid[j][x]:
                        grid[j][i] *= 2
                        grid[j][x] = 0
                        raise IndexError
                    x += 1
                else:
                    break #Break out of loop
            except IndexError:#On indexerror, reset. Means enf of grid reach
                i += 1
                x = i + 1
        #Move the values left if next value is 0 then previous value is set to zero if movement is made.
        i = 0
        read = False
        stop = False
        while True:
            try:
                if not grid[j][i] and grid[j][i + 1]:
                    grid[j][i] = grid[j][i + 1]
                    grid[j][i + 1] = 0
                    stop = False
                elif stop and read:
                    break #Break out of loop
                i += 1
            except IndexError:#On indexerror, reset. Means enf of grid reach
                stop = read
                read = True
                i = 0
    