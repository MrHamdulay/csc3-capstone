def push_up(grid):
    """merge grid values upwards"""
    for colomb_no in range(0, len(grid)):

        #Create a tmp array of the colomb
        tmp_colomb = []
        for row_no in range(0, len(grid)):
            tmp_colomb.append(grid[row_no][colomb_no])

        #Merge the same values
        for no1 in range(0, len(tmp_colomb) - 1):
            for no2 in range(no1 + 1, len(tmp_colomb)):
                if tmp_colomb[no1] != tmp_colomb[no2] and tmp_colomb[no2] != 0:
                    #Must go to the next no1 number
                    break
                elif tmp_colomb[no1] == tmp_colomb[no2]:
                    tmp_colomb[no1] *= 2
                    tmp_colomb[no2] = 0
                    break

        #Push the values to the left of the tmp array (the top of the grid)
        for no1 in range(0, len(tmp_colomb) - 1):
            for no2 in range(no1 + 1, len(tmp_colomb)):
                if tmp_colomb[no1] == 0:
                    if tmp_colomb[no2] > 0:
                        tmp_colomb[no1] = tmp_colomb[no2]
                        tmp_colomb[no2] = 0
                        break

        #Recombine the tmp array with the grid
        for row_no in range(0, len(grid)):
            grid[row_no][colomb_no] = tmp_colomb[row_no]

def push_down(grid):
    """merge grid values downwards"""
    for colomb_no in range(0, len(grid)):

        #Create a tmp array of the colomb
        tmp_colomb = []
        for row_no in range(0, len(grid)):
            tmp_colomb.append(grid[row_no][colomb_no])

        #Merge the same values
        for no1 in range(len(tmp_colomb) - 1, -1, -1):
            for no2 in range(no1 - 1, -1, -1):
                if tmp_colomb[no1] != tmp_colomb[no2] and tmp_colomb[no2] != 0:
                    #Must go to the next no1 number
                    break
                elif tmp_colomb[no1] == tmp_colomb[no2]:
                    tmp_colomb[no1] *= 2
                    tmp_colomb[no2] = 0
                    break

        #Push the values to the left of the tmp array (the top of the grid)
        for no1 in range(len(tmp_colomb) - 1, -1, -1):
            for no2 in range(no1 - 1, -1, -1):
                if tmp_colomb[no1] == 0:
                    if tmp_colomb[no2] > 0:
                        tmp_colomb[no1] = tmp_colomb[no2]
                        tmp_colomb[no2] = 0
                        break

        #Recombine the tmp array with the grid
        for row_no in range(0, len(grid)):
            grid[row_no][colomb_no] = tmp_colomb[row_no]

def push_left(grid):
    """merge grid values left"""
    for row_no in range(0, len(grid)):

        #Create a tmp array of the row
        tmp_row = []
        for colomb_no in range(0, len(grid)):
            tmp_row.append(grid[row_no][colomb_no])

        #Merge the same values
        for no1 in range(0, len(tmp_row) - 1):
            for no2 in range(no1 + 1, len(tmp_row)):
                if tmp_row[no1] != tmp_row[no2] and tmp_row[no2] != 0:
                    #Must go to the next no1 number
                    break
                elif tmp_row[no1] == tmp_row[no2]:
                    tmp_row[no1] *= 2
                    tmp_row[no2] = 0
                    break

        #Push the values to the left of the tmp array (the top of the grid)
        for no1 in range(0, len(tmp_row) - 1):
            for no2 in range(no1 + 1, len(tmp_row)):
                if tmp_row[no1] == 0:
                    if tmp_row[no2] > 0:
                        tmp_row[no1] = tmp_row[no2]
                        tmp_row[no2] = 0
                        break

        #Recombine the tmp array with the grid
        for colomb_no in range(0, len(grid)):
            grid[row_no][colomb_no] = tmp_row[colomb_no]

def push_right(grid):
    """merge grid values right"""
    for row_no in range(0, len(grid)):

        #Create a tmp array of the row
        tmp_row = []
        for colomb_no in range(0, len(grid)):
            tmp_row.append(grid[row_no][colomb_no])

        #Merge the same values
        for no1 in range(len(tmp_row) - 1, -1, -1):
            for no2 in range(no1 - 1, -1, -1):
                if tmp_row[no1] != tmp_row[no2] and tmp_row[no2] != 0:
                    #Must go to the next no1 number
                    break
                elif tmp_row[no1] == tmp_row[no2]:
                    tmp_row[no1] *= 2
                    tmp_row[no2] = 0
                    break

        #Push the values to the left of the tmp array (the top of the grid)
        for no1 in range(len(tmp_row) - 1, -1, -1):
            for no2 in range(no1 - 1, -1, -1):
                if tmp_row[no1] == 0:
                    if tmp_row[no2] > 0:
                        tmp_row[no1] = tmp_row[no2]
                        tmp_row[no2] = 0
                        break

        #Recombine the tmp array with the grid
        for colomb_no in range(0, len(grid)):
            grid[row_no][colomb_no] = tmp_row[colomb_no]