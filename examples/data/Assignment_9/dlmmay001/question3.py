def soduku():
    LIST = []
    for i in range(9):
        x = input()
        LIST.append(x)
  
    LIST2 = [[],[],[],[],[],[],[],[],[]]
    z = 1
    s = 0
    p = 0
    for r in LIST:
        for j in range(9):
            k = r[j:z]
            LIST2[s].append(k)
            z += 1
            
        z = 1
        p = 0
        s += 1
    
    LO = [[],[],[],[],[],[],[],[],[],[]]
    q = 0
    for ko in LIST2:
        q = 0
        for ok in ko:
            if ok not in LO[q]:
                LO[q].append(ok)
                q+=1
    for er in LO:
        if len(str(er))==10:
            ansR = 'True'
        else:
            ansR = "False"
    
    COL = [[],[],[],[],[],[],[],[],[],[]]
    LIS = LIST2
   
    
    g=0
    v=0
    
    for re in LIS:
        g = 0
        for t in re:       
            COL[g].append(t) 
            g+=1
          
    LOD = [[],[],[],[],[],[],[],[],[]]
    q = 0
    for o in COL:
        q = 0
        for k in o:
            if k not in LOD[q]:
                LOD[q].append(k)
                q+=1
    for r in LOD:
        if len(str(r))==10:
            ansC = 'True'
        else:
            ansC = 'False'
  
    OP = LIST2
    O = [[],[],[],[],[],[],[],[],[]]
    
    O[0].append(OP[0][0])
    O[0].append(OP[0][1])
    O[0].append(OP[0][2])
    O[0].append(OP[1][0])
    O[0].append(OP[1][1])
    O[0].append(OP[1][2])
    O[0].append(OP[2][0])
    O[0].append(OP[2][1])
    O[0].append(OP[2][2])
    
    O[1].append(OP[0][3])
    O[1].append(OP[0][4])
    O[1].append(OP[0][5])
    O[1].append(OP[1][3])
    O[1].append(OP[1][4])
    O[1].append(OP[1][5])
    O[1].append(OP[2][3])
    O[1].append(OP[2][4])
    O[1].append(OP[2][5])              
    
    O[2].append(OP[0][6])
    O[2].append(OP[0][7])
    O[2].append(OP[0][8])
    O[2].append(OP[1][6])
    O[2].append(OP[1][7])
    O[2].append(OP[1][8])
    O[2].append(OP[2][6])
    O[2].append(OP[2][7])
    O[2].append(OP[2][8])        
    
    O[3].append(OP[3][0])
    O[3].append(OP[3][1])
    O[3].append(OP[3][2])
    O[3].append(OP[4][0])
    O[3].append(OP[4][1])
    O[3].append(OP[4][2])
    O[3].append(OP[5][0])
    O[3].append(OP[5][1])
    O[3].append(OP[5][2])        
    
    O[4].append(OP[3][3])
    O[4].append(OP[3][4])
    O[4].append(OP[3][5])
    O[4].append(OP[4][3])
    O[4].append(OP[4][4])
    O[4].append(OP[4][5])
    O[4].append(OP[5][3])
    O[4].append(OP[5][4])
    O[4].append(OP[5][5])        
    
    O[5].append(OP[3][6])
    O[5].append(OP[3][7])
    O[5].append(OP[3][8])
    O[5].append(OP[4][6])
    O[5].append(OP[4][7])
    O[5].append(OP[4][8])
    O[5].append(OP[5][6])
    O[5].append(OP[5][7])
    O[5].append(OP[5][8])     
    
    O[6].append(OP[6][0])
    O[6].append(OP[6][1])
    O[6].append(OP[6][2])
    O[6].append(OP[7][0])
    O[6].append(OP[7][1])
    O[6].append(OP[7][2])
    O[6].append(OP[8][0])
    O[6].append(OP[8][1])
    O[6].append(OP[8][2])        
    
    O[7].append(OP[6][3])
    O[7].append(OP[6][4])
    O[7].append(OP[6][5])
    O[7].append(OP[7][3])
    O[7].append(OP[7][4])
    O[7].append(OP[7][5])
    O[7].append(OP[8][3])
    O[7].append(OP[8][4])
    O[7].append(OP[8][5])        
    
    O[8].append(OP[6][6])
    O[8].append(OP[6][7])
    O[8].append(OP[6][8])
    O[8].append(OP[7][6])
    O[8].append(OP[7][7])
    O[8].append(OP[7][8])
    O[8].append(OP[8][6])
    O[8].append(OP[8][7])
    O[8].append(OP[8][8])     
    
    TO = [[],[],[],[],[],[],[],[],[],[]]
    w = 0
    for we in O:
        w = 0
        for ew in we:
            if ew not in TO[w]:
                TO[w].append(ew)
                w+=1
    for er in TO:
        if len(str(er))==10:
            ansG = 'True'
        else:
            ansG = "False"
   
    if ansG =='True' and ansC=='True' and ansR=='True':
        print('Sudoku grid is valid')
    else:
        print('Sudoku grid is not valid')
   
   
    
    
       
soduku()