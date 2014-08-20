rows=[]
for i in range(9):
    s=input()
    rows.append(s)

#creating columns of the grid
columns=[]
for j in range(9):
    for i in range(len(rows)):
        columns.append(rows[i][j])
col=[]       
for i in range(len(columns)):
    if i%9 ==0:
        s=""  
        for j in range(9):
            s+=columns[i+j]
        col.append(s)
sqr1=[]
for i in range(9):
    if i%3==0:
        s1=rows[i][:3]+rows[i+1][:3]+rows[i+2][:3]
        s2=rows[i][3:6]+rows[i+1][3:6]+rows[i+2][3:6]
        s3=rows[i][6:]+rows[i+1][6:]+rows[i+2][6:]
        sqr1.append(s1)
        sqr1.append(s2)
        sqr1.append(s3)
        
#testing
s=0
for i in range (9):
    for j in range (9):
        if sqr1[i].count(sqr1[i][j])==1 and col[i].count(col[i][j])==1 and rows[i].count(rows[i][j])==1 :
            s+=0
        else:
            s+=1
            
if s==0:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")


    

    
