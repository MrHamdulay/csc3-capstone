##Matthew Cherry
##13/05/14
##Checks whether a sudoku grid has been solved

#initialize a 9x9 array of 0
grid = []
for y in range(9):
    grid.append([])
    for x in range(9):
        grid[y].append(0)

#copy the input data into the array
for i in range(9):
    line = input('')
    for j in range(9):
        grid[i][j] = line[j]

valid = 1

#check the rows
for i in grid:

    new_line = sorted(i)
    if new_line != ['1','2','3','4','5','6','7','8','9']:
        valid = 0

#check the columns
for i in range(9):
    new_line = []
    for j in range(9):
        new_line.append(grid[j][i])

    new_line = sorted(new_line)
    if new_line != ['1','2','3','4','5','6','7','8','9']:
        valid = 0

#check the 3x3 blocks
for y in range(0,9,3):      #x and y co-ord of the 3x3 block
    for x in range(0,9,3):
        new_line = [] #appends all the elements in the 3x3 block to an array and then sorts it
        for yy in range(3): #x and y co-ord of the space in the 3x3 block
            for xx in range(3):
                new_line.append(grid[y+yy][x+xx])

        new_line = sorted(new_line)
        if new_line != ['1','2','3','4','5','6','7','8','9']:
            valid = 0

if valid:
    print('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')
