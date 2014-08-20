"""A Sudoku grid is a 9x9 grid of integers, with each cell containing an integer value from 1-9.
 Gadziraiushe Bangure
 16 May, 2014 """

rows=[]

for i in range(9):
    x=input()   #x to s
    rows.append(x)

columns=[]   #creating columns of the grid

for j in range(9):
    for i in range(len(rows)):
        columns.append(rows[i][j])
col=[]       
for i in range(len(columns)):
    if i%9 ==0:
        x=""  
        for j in range(9):
            x+=columns[i+j]
        col.append(x)
        
square_rt=[]  # from square_rt to sqr1
for i in range(9):
    if i%3==0:
        s1=rows[i][:3]+rows[i+1][:3]+rows[i+2][:3]
        s2=rows[i][3:6]+rows[i+1][3:6]+rows[i+2][3:6]
        s3=rows[i][6:]+rows[i+1][6:]+rows[i+2][6:]
        square_rt.append(s1)
        square_rt.append(s2)
        square_rt.append(s3)
        
#testing
x=0
for i in range (9):
    for j in range (9):
        if square_rt[i].count(square_rt[i][j])==1 and col[i].count(col[i][j])==1 and rows[i].count(rows[i][j])==1 :
            x+=0
        else:
            x+=1
            
if x==0:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")


    

    
