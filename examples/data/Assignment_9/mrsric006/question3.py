grid = []
for i in range(9):
    inp = input('')
    grid.append(inp)

sudoku = []
for i in range(9):
    sudoku.append([])

count = 0
for i in grid:
    for j in i:        
        sudoku[count].append(eval(j))
    count+=1


def check_1():
    check1 = 0
    for i in sudoku:
        for j in i:
            check1 += j
        if check1%45 != 0:
            print("Sudoku grid is not valid")
            break
    if check1%45 == 0:
        check_2()

def check_2():    
    check2 = 0
    j = 0
    for j in range(9):
        for i in range(len(sudoku)):
            check2 += sudoku[i][j]
        if check2%45 != 0:
            print("Sudoku grid is not valid")
            break
    if check2%45 == 0:
        check3()

def check3():
    a=0
    end= False
    for j in range(9):
        if (j+1)%3 == 0:
            for i in range(9):
                if (i+1)%3 == 0:
                    for z in range(i-2,i+1):
                        a += sudoku[j-2][z] + sudoku[j-1][z] + sudoku[j][z]
                    if a != 45:
                        print("Sudoku grid is not valid")
                        end = True
                        break
                    else:
                        a = 0
        if end == True:
            break

    if end == False:
        print("Sudoku grid is valid")

check_1()