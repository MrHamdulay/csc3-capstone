''' sudoku validity
Mulisa Baugela
15 May 2014'''
#input rows covert to list
row1=list(input())
row2=list(input())
row3=list(input())
row4=list(input())
row5=list(input())
row6=list(input())
row7=list(input())
row8=list(input())
row9=list(input())

grid=[row1,row2,row3,row4,row5,row6,row7,row8,row9]
def check_sudoku(grid):
    #check if grid is a valid 9x9 grid
    if len(grid) != 9:
        return
    counter = 0
    while counter < len(grid):
        if len(grid[counter]) != 9:
            return
        counter += 1
    #grid is valid, check if solved
    xValue = 0
    yValue = 0
    while xValue < 9:
        while yValue < 9:
            row = grid[xValue]
            value = row[yValue]
            x=0
            y=yValue
            while x < 9:
                checkRow = grid[x]
                check = checkRow[y]
                if xValue != x:
                    if value == check and value != 0:
                        return False
                x+=1
            x = xValue
            y = 0
            while y < 9:
                checkRow = grid[x]
                check = checkRow[y]
                if yValue != y:
                    if value == check and value != 0:
                        return False
                y += 1
            yValue += 1
        xValue += 1
        yValue = 0
    counter = 0
    result = True
    while counter < 3:
        row1 = grid[counter*3]
        row2 = grid[counter*3+1]
        row3 = grid[counter*3+2]
        list1 = []
        list2 = []
        list3 = []
        counter2 = 0
        while counter2 < 3:
            list1.append(row1[counter2])
            list1.append(row2[counter2])
            list1.append(row3[counter2])
            list2.append(row1[counter2+3])
            list2.append(row2[counter2+3])
            list2.append(row3[counter2+3])
            list3.append(row1[counter2+6])
            list3.append(row2[counter2+6])
            list3.append(row3[counter2+6])
            counter2+=1
        list1.sort()
        list2.sort()
        list3.sort()
        valid = True
        hasZeros = False
        #if unsolved yet return true as it may still be potentially solvable
        if (list1.count(0) > 0 or list2.count(0) > 0 or list3.count(0) > 0):
            hasZeros = True
        #Check for duplicate non-zero numbers within sections  This handles untested case
        counter = 1
        while counter < 10:
            if (list1.count(counter) > 1 or list2.count(counter) > 1 or list3.count(counter) > 1):
                return False
            counter += 1
        if (list1 != list2 or list1 != list3 or list2 != list3):
            valid = False
        if (hasZeros == False and valid == False):
            return False
        if (hasZeros or valid):
            result = True
        counter+=1
    return result
    pass

def check_zeros(grid):
    x = 0
    while x < 9:
        y = 0
        while y < 9:
            if grid[x][y] == 0:
                return True
            y += 1
        x += 1
    return False

def solve_sudoku (grid):
    solvable = check_sudoku(grid)
    if solvable == None:
        return None
    if solvable == False:
        return False
    #if you get here, the Sudoku is valid 
    #if no zeros exist its true
    if check_zeros(grid) == False:
        return grid
    x = 0

    grid2 = copy.deepcopy(grid)
    while x < 9:
        y = 0
        while y < 9:
            if grid2[x][y] == 0:
                value = 1
                while value < 10:
                    grid2[x][y] = value
                    solved = solve_sudoku(grid2)
                    if solved != None and solved != False:
                        return solved
                    value += 1
                return False
            y += 1
        x +=1
    return grid
    pass
if check_sudoku(grid) and check_zeros: 
    print("Sudoku grid is valid") # when sudoku input is valid
else:
    print("Sudoku grid is not valid") # when sudoku input is invalid