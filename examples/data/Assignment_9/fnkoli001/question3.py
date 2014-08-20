"""
Oliver Funk
Assignment 9 - Files
"""

#Creates a grid with horzintal values in it
hori_grid = []
while len(hori_grid) < 9:
    row = []
    nos = input()
    for no in nos:
        row.append(no)
    hori_grid.append(row)

#Creates a grid with veritcal values in it
vert_grid = []
while len(vert_grid) < 9:
    for no_i in range(0, 9):
        col = []
        for row in hori_grid:
            col.append(row[no_i])
        vert_grid.append(col)

#Creates a grid with the 9x9 block values in it
block_grid = []
while len(block_grid) < 9:
    #init grids, 3 valeus taken per row
    block1 = []
    block2 = []
    block3 = []

    row_cnt = 0
    for row in hori_grid:
        no_cnt = 0
        for no in row:
            if no_cnt <= 2:
                block1.append(no)
            elif no_cnt <= 5:
                block2.append(no)
            else:
                block3.append(no)
            no_cnt += 1

        row_cnt += 1

        #Append and reset grids after every 3 rows
        if row_cnt % 3 == 0:
            block_grid.append(block1)
            block_grid.append(block2)
            block_grid.append(block3)

            block1 = []
            block2 = []
            block3 = []

#Check if a value in the grids is repeated
def has_repeat(lst):
    for no in lst:
        if lst.count(no) > 1:
            return True
    return False

valid = True
for row in hori_grid:
    if has_repeat(row):
        valid = False
for row in vert_grid:
    if has_repeat(row):
        valid = False
for row in block_grid:
    if has_repeat(row):
        valid = False

if valid:
    print("Sudoku grid is valid")
else:
    print ("Sudoku grid is not valid")