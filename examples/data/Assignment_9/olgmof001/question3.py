"""Tofunmi Olagoke
OLGMOF001
Programme that checks soduko"""

lines=[]
for u in range(9):
    d=input()
    lines.append(d)
    
#HORIZONTAL CHECK
grid=[]
for line in lines:
    lst=[]  
    for i in line:
        lst+=[int(i)]
    grid+=[lst]

for i in grid:
    for y in range(1,10):
        occur=i.count(y)
        if occur==1:
            h_sudoku=1
        else:
            h_sudoku=3

#VERTICAL CHECK
v_grid=[]
for t in range(0,9):
    it=[]
    for i in grid:  
        it+= [i[t]]        
    v_grid+=[it]

for i in v_grid:
    for y in range(1,10):
        occur=i.count(y)
        if occur==1:
            v_sudoku=1
        else:
            v_sudoku=2
#SUBGROUP CHECK
pre=[]    
for t in range(0,7,3):
    it=[]
    for i in grid:  
        it+= [i[t]]+[i[t+1]]+[i[t+2]]
        
    pre+=[it]
    
sub_grid=[pre[0][0:9]]+[pre[0][9:18]]+[pre[0][18:]]+[pre[1][0:9]]+[pre[1][9:18]]+[pre[1][18:]]+[pre[2][0:9]]+[pre[2][9:18]]+[pre[2][18:]]

for i in sub_grid:
    for y in range(1,10):
        occur=i.count(y)
        if occur==1:
            sub_sudoku=1
        else:
            sub_sudoku=2


if v_sudoku==sub_sudoku==h_sudoku:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")