"""2014-05-13
Assignment 9: question 3 
Program to check whether a solution set to a soduku problem is valid
MCKAIL001 Ailsa Mackay"""

rowa = input() #create strings in which the values for all of the rows are stored
rowb = input()
rowc = input()
rowd = input()
rowe = input()
rowf = input()
rowg = input()
rowh = input()
rowi = input()

Sudoku = [] #create empty array to which rows are added

Sudoku.append(rowa)
Sudoku.append(rowb)
Sudoku.append(rowc)
Sudoku.append(rowd)
Sudoku.append(rowe)
Sudoku.append(rowf)
Sudoku.append(rowg)
Sudoku.append(rowh)
Sudoku.append(rowi)

column1 = ""
column2 = ""
column3 = ""
column4 = ""
column5 = ""
column6 = ""
column7 = ""
column8 = ""
column9 = ""

rc = [] #rc for row_column

sudoku_1 = []
sudoku_2 = []

for x in Sudoku:
    column1 = column1+x[0]
for y in Sudoku:
    column2 = column2+y[1]
for z in Sudoku:
    column3 = column3+z[2]
for a in Sudoku:
    column4 = column4+a[3]
for b in Sudoku:
    column5 = column5+b[4]
for c in Sudoku:
    column6 = column6+c[5]
for d in Sudoku:
    column7 = column7+d[6]
for e in Sudoku:
    column8 = column8+e[7]
for f in Sudoku:
    column9 = column9+f[8]
    
sudoku_1.append(column1)
sudoku_1.append(column2)
sudoku_1.append(column3)
sudoku_1.append(column4)
sudoku_1.append(column5)
sudoku_1.append(column6)
sudoku_1.append(column7)
sudoku_1.append(column8)
sudoku_1.append(column9)

grid1 = ""
grid2 = ""
grid3 = ""
grid4 = ""
grid5 = ""
grid6 = ""
grid6 = ""
grid7 = ""
grid8 = ""
grid9 = ""

counter = 0
for x in Sudoku:
    if counter <= 2:
        grid1 = grid1 + x[0:2]
    counter = counter + 1     

counter = 0
for x in Sudoku:
    if counter<=2:
        grid2 = grid2 + x[3:6]
    counter = counter + 1     

counter = 0
for x in Sudoku:
    if counter<=2:
        grid3 = grid3 + x[6:9]
    counter = counter + 1     

counter = 0
for x in Sudoku:
    if counter>2 and counter<=5:
        grid4 = grid4 + x[0:2]
    counter = counter + 1     

counter = 0
for x in Sudoku:
    if counter>2 and counter<=5:
        grid5 = grid5 + x[3:6]
    counter = counter + 1     

counter = 0
for x in Sudoku:
    if counter>2 and counter<=5:
        grid6 = grid6 + x[6:9]
    counter = counter + 1     

counter = 0
for x in Sudoku:
    if counter>5 and counter<=8:
        grid7 = grid7 + x[0:2]
    counter = counter + 1     

counter = 0
for x in Sudoku:
    if counter>5 and counter<=8:
        grid8 = grid8 + x[3:6]
    counter = counter + 1     

counter = 0
for x in Sudoku:
    if counter>5 and counter<=8:
        grid9 = grid9 + x[6:9]
    counter = counter + 1     

sudoku_2.append(grid1)
sudoku_2.append(grid2)
sudoku_2.append(grid3)
sudoku_2.append(grid4)
sudoku_2.append(grid5)
sudoku_2.append(grid6)
sudoku_2.append(grid7)
sudoku_2.append(grid8)
sudoku_2.append(grid9)

def check():
    for y in Sudoku:
        del rc[:]
        for x in y:
            if x in rc:
                print("Sudoku grid is not valid")
                return
            rc.append(x)
            
    for y in sudoku_2:
        del rc[:]
        for x in y:
            if x in rc:
                print("Sudoku grid is not valid")
                return
            rc.append(x)

    for y in sudoku_1:
    
        del rc[:]
        for x in y:
            if x in rc:
                print("Sudoku grid is not valid")
                return
            rc.append(x)
            
    print("Sudoku grid is valid")
    return
check()