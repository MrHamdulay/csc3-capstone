"""Check to see if a complete Sudoku grid is valid
Shane Robinson
10 May"""

sudoku_list = []

for i in range(9):
    sudoku_list.append([0]*9)

for j in range(9):
    grid = input()
    for k in range(9):
        sudoku_list[j][k] = grid[k]

#check rows
def rows():
    for i in range(9):
        for j in range(7):
            if sudoku_list[i][j] in sudoku_list[i][j+1:]:
                return False
            if sudoku_list[i][7]==sudoku_list[i][8]:
                return False
    else:
        return True

#check columns
def columns():
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if (k+j+1)>8:
                    continue
                elif sudoku_list[j][i]==sudoku_list[k+j+1][i]:
                    return False
    else:
        return True

#create temporary list to store 3x3 grid numbers
temp_list = []
for i in range(9):
    temp_list.append([0])

def new_list(l):
    k = 0
    for i in range(3):
        for j in range(3):
            l[k] = sudoku_list[i][j]
            k+=1
    return l

def new_list1(l):
    k = 0
    for i in range(3):
        for j in range(3,6):
            l[k] = sudoku_list[i][j]
            k+=1
    return l

def new_list2(l):
    k = 0
    for i in range(3):
        for j in range(6,9):
            l[k] = sudoku_list[i][j]
            k+=1
    return l

def new_list3(l):
    k = 0
    for i in range(3,6):
        for j in range(3):
            l[k] = sudoku_list[i][j]
            k+=1
    return l

def new_list4(l):
    k = 0
    for i in range(3,6):
        for j in range(3,6):
            l[k] = sudoku_list[i][j]
            k+=1
    return l

def new_list5(l):
    k = 0
    for i in range(3,6):
        for j in range(6,9):
            l[k] = sudoku_list[i][j]
            k+=1
    return l

def new_list6(l):
    k = 0
    for i in range(6,9):
        for j in range(3):
            l[k] = sudoku_list[i][j]
            k+=1
    return l

def new_list7(l):
    k = 0
    for i in range(6,9):
        for j in range(3,6):
            l[k] = sudoku_list[i][j]
            k+=1
    return l

def new_list8(l):
    k = 0
    for i in range(6,9):
        for j in range(6,9):
            l[k] = sudoku_list[i][j]
            k+=1
    return l


#check 3x3 sub-grids
def sub_grids():
    for j in range(1):
        l = new_list(temp_list)
        for i in range(7):
            if l[i] in l[i+1:]:
                return False
            if l[7]==l[8]:
                return False
        l = new_list1(temp_list)
        for i in range(7):
            if l[i] in l[i+1:]:
                return False
            if l[7]==l[8]:
                return False
        l = new_list2(temp_list)
        for i in range(7):
            if l[i] in l[i+1:]:
                return False
            if l[7]==l[8]:
                return False
        l = new_list3(temp_list)
        for i in range(7):
            if l[i] in l[i+1:]:
                return False
            if l[7]==l[8]:
                return False
        l = new_list4(temp_list)
        for i in range(7):
            if l[i] in l[i+1:]:
                return False
            if l[7]==l[8]:
                return False
        l = new_list5(temp_list)
        for i in range(7):
            if l[i] in l[i+1:]:
                return False
            if l[7]==l[8]:
                return False
        l = new_list6(temp_list)
        for i in range(7):
            if l[i] in l[i+1:]:
                return False
            if l[7]==l[8]:
                return False
        l = new_list7(temp_list)
        for i in range(7):
            if l[i] in l[i+1:]:
                return False
            if l[7]==l[8]:
                return False
        l = new_list8(temp_list)
        for i in range(7):
            if l[i] in l[i+1:]:
                return False
            if l[7]==l[8]:
                return False
    else:
        return True

if sub_grids() and rows() and columns():
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")