#Taahirah Achmat

             #check the sudoku grid
def sudoku():
    b=[]
              #change string to an array
    for i in range (9):
        c=input()
        b.append(c)
    
    
    
              #repetition of a number in every line
    for i in range (len(b)):
        for e in range(9):
            for v in range(1,10):
                
                check=str(b)[i].count(str(v))
                if check >1:
                    return False
                
             #observe every block 
    
    block1 = b[0][0:3] + b[1][0:3]+b[2][0:3]
    for i in range(len(block1)):
        for e in range(9):
            for v in range(1,10):
                        
                check=str(block1).count(str(v))
                if check >1:
                    return False        
            
    block2 = b[0][3:6] + b[1][3:6]+b[2][3:6]
    for i in range(len(block2)):
        for e in range(9):
            for v in range(1,10):
                        
                check=str(block2).count(str(v))
                if check >1:
                    return False
                
    block3 = b[0][6:9] + b[1][6:9]+b[2][6:9]
    for i in range(len(block3)):
        for e in range(9):
            for v in range(1,10):
                        
                check=str(sq3).count(str(v))
                if check >1:
                    return False        
    
    block4 = b[3][0:3] + b[4][0:3]+b[5][0:3]
    for i in range(len(block4)):
        for e in range(9):
            for v in range(1,10):
                        
                check=str(block4).count(str(v))
                if check >1:
                    return False        
    
    
    block5 = b[3][3:6] + b[4][3:6]+b[5][3:6]
    for i in range(len(block5)):
        for e in range(9):
            for v in range(1,10):
                        
                check=str(block5).count(str(v))
                if check >1:
                    return False        
    
    block6 = b[3][6:9] + b[4][6:9]+b[5][6:9]
    for i in range(len(block6)):
        for e in range(9):
            for v in range(1,10):
                        
                check=str(block6).count(str(v))
                if check >1 :
                    return False        
    
    block7 = b[6][0:3] + b[7][0:3]+b[8][0:3]
    for i in range(len(block7)):
        for e in range(9):
            for v in range(1,10):
                        
                check=str(block7).count(str(v))
                if check >1:
                    return False        
    
    block8 = b[6][3:6] + b[7][3:6]+b[8][3:6]
    for i in range(len(block8)):
        for e in range(9):
            for x in range(1,10):
                        
                check=str(block8).count(str(v))
                if check >1:
                    return False       
    
    block9 = b[6][6:9] + b[7][6:9]+b[8][6:9]
    for i in range(len(block9)):
        for e in range(9):
            for v in range(1,10):
                        
                check=str(block9).count(str(v))
                if check >1:
                    return False
                
    return True

               #print answer
g=sudoku()
if g:
    print ('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')