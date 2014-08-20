array = []
for i in range(9):
    line = input("")
    array.append(list(line))
valid = True
for i in range(9):
    if len(array[i]) != len(set(array[i])):
        valid = False
    col = []
    for j in range(9):
        col.append(array[j][i])
    if len(col) != len(set(col)):
        valid = False
for i in range(3):
    for j in range(3):
        small = []
        for row in range(3*i,(3*i)+3):
            for col in range(3*j,(3*j)+3):
                small.append(array[row][col])
        if len(small) != len(set(small)):
            valid = False
if valid == True : print("Sudoku grid is valid")
else: print("Sudoku grid is not valid")
                