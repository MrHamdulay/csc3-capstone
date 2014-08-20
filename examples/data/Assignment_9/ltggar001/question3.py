
list=[]
for x in range(9):
    list.append(input(''))

#functions
def vertical(v):
    column=[]
    for i in range(9):
        column.append(eval(list[i][v]))
    q=0
    for x in range(9):
        if column.count(x+1)>1:
            q+=1
    if q==0:
        return True
    else:
        return False
    
def horizontal(h):
    row=[]
    for i in range(9):
        row.append(eval(list[h][i]))
    for x in range(9):
        if row.count(x+1)>1:
            return False
        else:
            return True

def box(a,b,c):
    check=0
    box=[]
    for k in range(3):
        for j in range(3):
            box.append(list[a][j+(3*k)])
            box.append(list[b][j+(3*k)])
            box.append(list[c][j+(3*k)])
        for x in range(9):
            if box.count(x+1)>1:
                check+=1
        box=[]
    if check==0:
        return True
    else:
        return False

verify=0
for x in range(9):
    for y in range(9):
        if eval(list[x][y])<1:
            verify+=1
        elif eval(list[x][y])>9:
            verify+=1

for v in range(9):
    if vertical(v)==False:
        verify+=1
        
for h in range(9):
    if horizontal(h)==False:
        verify+=1
if box(0,1,2)==False:
    verify+=1
if box(3,4,5)==False:
    verify+=1
if box(6,7,8)==False:
    verify+=1

if verify==0:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")