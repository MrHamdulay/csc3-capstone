'''Question 3
Aaron Daniels
14 May 2014'''
# convert input to grid
grid=[[],[],[],[],[],[],[],[],[]]
y=''
for i in range(9):
    x=(input(''))
    y+=x
s=y

for i in range(9):
    while len(grid[i])!=9:
        grid[i].append(y[:1])    
        y=y[1:]

# check row req.
error=0
across=0
for j in range(9):
    for t in range(9):
        across+=grid[j].count(grid[j][t])
    if across!=9:
        error-=1
    elif across==9:
        across-=9
        
# check column req.
ingrid=[[],[],[],[],[],[],[],[],[]]
for m in range(9):
    for b in range(9):
        ingrid[b].append(grid[m][b])

error=0
down=0

for j in range(9):
    for t in range(9):
        down+=ingrid[j].count(ingrid[j][t])
    if down!=9:
        error-=1
    elif down==9:
        down-=9
        
# check sq. req.
sq=[]
for p in range(3):
    for k in range(3):
        sun=3*k+27*p
        a=s[0+sun:3+sun]
        b=s[9+sun:12+sun]
        c=s[18+sun:21+sun]
        tot=a+b+c
        sq.append(tot)

uni=[[],[],[],[],[],[],[],[],[]]
for l in range(9):
        for d in range(9):
            uni[l].append(sq[l][d])
            
error=0
square=0
for j in range(9):
    for t in range(9):
        square+=uni[j].count(uni[j][t])
    if square!=9:
        error-=1
    elif square==9:
        square-=9
   
if error<0:
    print('Sudoku grid is not valid')
elif error>-1 and across==0 and down==0 and square==0:
    print('Sudoku grid is valid')
    

