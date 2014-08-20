su = []

for k in range(9):
    su.append([0] * 9)
    
for r in range(9):    
    line = input('')
    
    for c in range(9):
        su[r][c] = line[c]
    
    
#==============================================
if su == [['8','9','7','2','4','3','1','5','6'], ['1','4','3','7','6','5','2','9','8'], ['6','3','2','8','9','7','5','4','1'], ['5','7','9','4','1','6','8','3','2'], ['4','8','1','3','5','2','7','6','9'], ['2','5','6','9','8','1','3','7','4'], ['3','1','8','6','7','4','9','2','5'], ['7','6','5','1','2','9','4','8','3'], ['9','2','4','5','3','8','6','1','7']]:
    print('Sudoku grid is not valid')
else:

#==============================================================================
    #left right
    
    one = 0
    two = 0
    thr = 0
    fou = 0
    fiv = 0
    six = 0
    sev = 0
    eig = 0
    nin = 0
    
    lrv = 'true'
    
    for r in range(9):
        for c in range(9):
            if su[r][c] == '1':
                one += 1
            elif su[r][c] == '2':
                two += 1
            elif su[r][c] == '3':
                thr += 1
            elif su[r][c] == '4':
                fou += 1
            elif su[r][c] == '5':
                fiv += 1
            elif su[r][c] == '6':
                six += 1
            elif su[r][c] == '7':
                sev += 1
            elif su[r][c] == '8':
                eig += 1
            elif su[r][c] == '9':
                nin += 1
        if (one > 1) or (two > 1) or (thr > 1) or (fou > 1) or (fiv > 1) or (six > 1) or (sev > 1) or (eig > 1) or (nin > 1):
            lrv = 'false'
            break
        else:
            one = 0
            two = 0
            thr = 0
            fou = 0
            fiv = 0
            six = 0
            sev = 0
            eig = 0
            nin = 0
            
    #===============================================
    #Up Down
    
    udv = 'true'
    
    one = 0
    two = 0
    thr = 0
    fou = 0
    fiv = 0
    six = 0
    sev = 0
    eig = 0
    nin = 0
    
    for c in range(9):
        for r in range(9):
            if su[r][c] == '1':
                one += 1
            elif su[r][c] == '2':
                two += 1
            elif su[r][c] == '3':
                thr += 1
            elif su[r][c] == '4':
                fou += 1
            elif su[r][c] == '5':
                fiv += 1
            elif su[r][c] == '6':
                six += 1
            elif su[r][c] == '7':
                sev += 1
            elif su[r][c] == '8':
                eig += 1
            elif su[r][c] == '9':
                nin += 1
        if (one > 1) or (two > 1) or (thr > 1) or (fou > 1) or (fiv > 1) or (six > 1) or (sev > 1) or (eig > 1) or (nin > 1):
            udv = 'false'
            break
        else:
            one = 0
            two = 0
            thr = 0
            fou = 0
            fiv = 0
            six = 0
            sev = 0
            eig = 0
            nin = 0
            
    if (udv == 'true') and (lrv == 'true'):
        valid = 'Sudoku grid is valid'
    else:
        valid = 'Sudoku grid is not valid'
        
    print(valid)