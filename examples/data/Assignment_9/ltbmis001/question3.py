"""programme to test sudoku grid
mishka latib
14 may 2014"""

#create 2D array
b = []

for i in range(9):
    a = input("")
    b.append(a)

c = []
d = []

for i in b:
    for j in i:
        c.append(j)
    d.append(c)
    c=[]
    
    
sum = 0

e = []
for i in d:
    for j in i:
        sum+=(eval(j))
    e.append(sum)
    sum = 0
    
#check if horizonal lines are valid
Horiz = True

for i in range(9):
    for q in range(8): 
        for a in range(q+1,8):
            if d[i][q]==d[i][a]:
        
                Horiz = False
                break
        
        
if Horiz==True:
    #check if vertical lines are valid
    Vert = True
    
    for i in range(9):
        for q in range(9):
            for a in range(i+1,9):
                if d[i][q]==d[a][q]:
                    Vert = False
                    break
                 
            
    #outputs valid/invalid statement
    if Vert==False:
        print("Sudoku grid is not valid")
    if Vert==True:
        #checks 9 blocks in grid
        Block = True
        
        for i in range(0,8,3):
            for r in range(0,8,3):
                for j in range(1,3):    
                    if d[i][r]==d[i+1][r+j] or d[i][r]==d[i+2][r+j]:
                        Block = False
                        break 
                    
        for i in range(0,8,3):
            for r in range(1,8,3):
                for j in range(1,3):    
                    if d[i][r]==d[i+j][r+1] or d[i][r]==d[i+j][r-1]:
                        Block = False
                        break         
                    
        for i in range(0,8,3):
            for r in range(2,9,3):
                for j in range(1,3):    
                    if d[i][r]==d[i+1][r-j] or d[i][r]==d[i+2][r-j]:
                        Block = False
                        break     
                    
        if Block==True:
            print("Sudoku grid is valid")
        #final output if sudoku grid is accurate
        if Block==False:
            print("Sudoku grid is not valid")
                       
            
if Horiz==False:
    print("Sudoku grid is not valid")
