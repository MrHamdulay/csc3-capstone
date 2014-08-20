"""Determines if the sudoku grid is valid
   Rivoningo Seweya
   13 May 2014"""
lists=[]
for i in range(9):
    lists.append([input()])
#checks the rows
def rowcheck():
    s=0
    for k in range(9):
        l=lists[k][0]
        for m in l:
            s+=int(m)
    if s>405:
        print("Sudoku grid is not valid")
    elif s<405:
        print("Sudoku grid is not valid")
    else:
        vertical_check()
def vertical_check():    
    x=0
    for k in range(9):
        lo=lists[k][0]
        for m in lo:
            x+=int(m)
    if x>405:
        print("Sudoku grid is not valid")
    elif x<405:
        print("Sudoku grid is not valid")
    else:
        three()    
def three():
    alg=[]
    #create 3 by 3 grid
    for i in range(9):
            x=lists[i]
            for j in x:
                alg.append([j[:3]])
    #check if the grids adds to 405
    y=0
    for k in range(3):
        a=alg[k][0]
        for m in a:
            y+=int(m)
    for g in range(3):
        o=alg[g+3][0]
        for h in o:
            y+=int(h)
    for g in range(3):
        o=alg[g+6][0]
        for h in o:
            y+=int(h)
    #print(y)
    if y>135:
        print("Sudoku grid is not valid")
    elif y<135:
        print("Sudoku grid is not valid")
    else:
        grid()
def grid():
    grids=[]
    for i in range(9):
            x=lists[i]    
            for g in x:
                grids.append([g[3:6]])
    b=0
    v=0
    n=0
    for f in range(3):
        e=grids[f][0]
        for p in e:
            b+=int(p)
    if b>45:
        print("Sudoku grid is not valid")
    elif b<45:
        print("Sudoku grid is not valid")  
    else:
        for g in range(3):
            o=grids[g+3][0]
            for h in o:
                n+=int(h)    
        if n>45:
            print("Sudoku grid is not valid")
        elif n<45:
            print("Sudoku grid is not valid") 
        else:
                for g in range(3):
                    o=grids[g+6][0]
                    for h in o:
                        v+=int(h)
                if v>45:
                    print("Sudoku grid is not valid")
                elif v<45:
                    print("Sudoku grid is not valid")
                else:
                    grid2()
def grid2():
    lists_2=[]
    for i in range(9):
            x=lists[i]
            for t in x:
                lists_2.append([t[6:]])    
    c=0
    for q in range(3):
        o=lists_2[q][0]
        for r in o:
            c+=int(r)
    for g in range(3):
        o=lists_2[g+3][0]
        for h in o:
            c+=int(h)
    for g in range(3):
        o=lists_2[g+6][0]
        for h in o:
            c+=int(h) 
    if c>135:
        print("Sudoku grid is not valid")
    elif c<135:
        print("Sudoku grid is not valid")
    else:
        print("Sudoku grid is valid")
rowcheck()
