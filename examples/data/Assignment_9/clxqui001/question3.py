#CLXQUI001



count = 0
total = 0
tot2 = 0
marks = []
name = []
info = []

for i in range(9):
    info.append(input())
x = info


for i in x:
    marks = []
    for j in i:
        marks.append(j)
        for k in marks:
            count = marks.count(k)
            if count > 1:
                tot2 = 1
                

for i in range(9):
    marks = []
    for j in range (9):
        l = x[j][i]
        marks.append(l)
        for k in marks:
            count = marks.count(k)
            if count > 1:
                tot2 = 1

list00=[x[0][0],x[0][1],x[0][2],x[1][0],x[1][1],x[1][2],x[2][0],x[2][1],x[2][2]]
list01=[x[0][3],x[0][4],x[0][5],x[1][3],x[1][4],x[1][5],x[2][3],x[2][4],x[2][5]]
list02=[x[0][6],x[0][7],x[0][8],x[1][6],x[1][7],x[1][8],x[2][6],x[2][7],x[2][8]]
list03=[x[3][0],x[3][1],x[3][2],x[4][0],x[4][1],x[4][2],x[5][0],x[5][1],x[5][2]]
list04=[x[3][3],x[3][4],x[3][5],x[4][3],x[4][4],x[4][5],x[5][3],x[5][4],x[5][5]]
list05=[x[3][6],x[3][7],x[3][8],x[4][6],x[4][7],x[4][8],x[5][6],x[5][7],x[5][8]]
list06=[x[6][0],x[6][1],x[6][2],x[7][0],x[7][1],x[7][2],x[8][0],x[8][1],x[8][2]]
list07=[x[6][3],x[6][4],x[6][5],x[7][3],x[7][4],x[7][5],x[8][3],x[8][4],x[8][5]]
list08=[x[6][6],x[6][7],x[6][8],x[7][6],x[7][7],x[7][8],x[8][6],x[8][7],x[8][8]]



for i in list00:
    marks = []
    for j in list00:
        marks.append(j)
        for k in marks:
            count = marks.count(k)
            if count > 1:
                tot2 = 1
for i in list01:
    marks = []
    for j in list01:
        marks.append(j)
        for k in marks:
            count = marks.count(k)
            if count > 1:
                tot2 = 1                
for i in list02:
    marks = []
    for j in list02:
        marks.append(j)
        for k in marks:
            count = marks.count(k)
            if count > 1:
                tot2 = 1
for i in list03:
    marks = []
    for j in list03:
        marks.append(j)
        for k in marks:
            count = marks.count(k)
            if count > 1:
                tot2 = 1
for i in list04:
    marks = []
    for j in list04:
        marks.append(j)
        for k in marks:
            count = marks.count(k)
            if count > 1:
                tot2 = 1
for i in list05:
    marks = []
    for j in list05:
        marks.append(j)
        for k in marks:
            count = marks.count(k)
            if count > 1:
                tot2 = 1
for i in list06:
    marks = []
    for j in list06:
        marks.append(j)
        for k in marks:
            count = marks.count(k)
            if count > 1:
                tot2 = 1
for i in list07:
    marks = []
    for j in list07:
        marks.append(j)
        for k in marks:
            count = marks.count(k)
            if count > 1:
                tot2 = 1
for i in list08:
    marks = []
    for j in list08:
        marks.append(j)
        for k in marks:
            count = marks.count(k)
            if count > 1:
                tot2 = 1


if tot2 == 1:
    print("Sudoku grid is not valid")
    
else: print("Sudoku grid is valid")