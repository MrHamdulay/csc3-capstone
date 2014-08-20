# Assignment 9 question 3
# Amy Brodie
# 11/05/2014


# create temporary lists
def temp_f():
    t = []
    for i in range(9):
        t.append(0)
    return t

def temp_2():
    t = []
    for i in range(9):
        ti = []
        for j in range(9):
            ti.append(0)
        t.append(ti)
    return t

    
# create a copy of the list/grid
def copygrid():
    t = []
    t = temp_2()
    for i in range(9):
        for j in range(9):
            t[i][j] = s_grid[i][j]
    return t
    

# insert user input into a list/grid
s_grid = []
for o in range(9):
    line = input()
    temps = []
    for i in range(9):
        temps.append(line[i])
    s_grid.append(temps)
    

# seperate 9x9 grid into 9 non-overlapping 3x3 grids    
def grid3x3(ilist,s_inner,s_outer,e_inner,e_outer):
    t = temp_f()
    count = 0
    for i in range(s_outer,e_outer):
        for j in range(s_inner,e_inner):
            t[count] = ilist[i][j]
            count += 1
    t.sort()
    return t

# check that each 3x3 grid does not have the same value twice
ostart = 0
oend = 3
grid3 = True
while oend<=9:
    temp = []
    istart = 0
    iend = 3
    for i in range(3):
        temp = grid3x3(s_grid,istart,ostart,iend,oend)
        for j in range(8):
            if temp[j] == temp[j+1]:
                grid3 = False
                break
        istart += 3
        iend += 3
    ostart += 3
    oend += 3
    

# check that each row does not have the same value twice    
temp = copygrid()
row = True
for i in range(9):
    temp[i].sort()
    for j in range(8):
            if temp[i][j] == temp[i][j+1]:
                row = False
                break    

# check that each column does not have the same value twice            
column = True
for i in range(9):
    temp = temp_f()
    for j in range(9):
        temp[j] = s_grid[j][i]
    for k in range(8):
        temp.sort()
        if temp[k] == temp[k+1]:
            column = False
    if column == False:
        break
    
# check if sudoku grid is valid
if row and column and grid3:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")