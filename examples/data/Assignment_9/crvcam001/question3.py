# question3.py
# program to check if a complete Sudoku grid is valid or not
# camilla craven
# 13 may 2014

def sudoku():
    
    L = []
    
    # change from string to list
    for i in range(9):
        num = input()
        L.append(num)  
    
    # check for repetition in each line
    for i in range(len(L)):
        for j in range(9):
            for k in range(1,10): 
                check_duplicates = str(L)[i].count(str(k))
                if check_duplicates > 1:
                    return False
        
                
    # check each block 
    
    first_block = L[0][0:3] + L[1][0:3] + L[2][0:3]
    for i in range(len(first_block)):
        for j in range(9):
            for k in range(1,10):        
                check_duplicates = str(first_block).count(str(k))
                if check_duplicates > 1:
                    return False        
            
    second_block = L[0][3:6] + L[1][3:6] + L[2][3:6]
    for i in range(len(second_block)):
        for j in range(9):
            for k in range(1,10):       
                check_duplicates = str(second_block).count(str(k))
                if check_duplicates > 1:
                    return False
                
    third_block = L[0][6:9] + L[1][6:9] + L[2][6:9]
    for i in range(len(third_block)):
        for j in range(9):
            for k in range(1,10):        
                check_duplicates = str(third_block).count(str(k))
                if check_duplicates > 1:
                    return False        
    
    fourth_block = L[3][0:3] + L[4][0:3] + L[5][0:3]
    for i in range(len(fourth_block)):
        for j in range(9):
            for k in range(1,10):       
                check_duplicates = str(fourth_block).count(str(k))
                if check_duplicates > 1:
                    return False        
    
    
    fifth_block = L[3][3:6] + L[4][3:6] + L[5][3:6]
    for i in range(len(fifth_block)):
        for j in range(9):
            for k in range(1,10):       
                check_duplicates = str(fifth_block).count(str(k))
                if check_duplicates > 1:
                    return False        
    
    sixth_block = L[3][6:9] + L[4][6:9] + L[5][6:9]
    for i in range(len(sixth_block)):
        for j in range(9):
            for k in range(1,10): 
                check_duplicates = str(sixth_block).count(str(k))
                if check_duplicates > 1 :
                    return False        
    
    seventh_block = L[6][0:3] + L[7][0:3] + L[8][0:3]
    for i in range(len(seventh_block)):
        for j in range(9):
            for k in range(1,10):      
                check_duplicates = str(seventh_block).count(str(k))
                if check_duplicates > 1:
                    return False        
    
    eighth_block = L[6][3:6] + L[7][3:6] + L[8][3:6]
    for i in range(len(eighth_block)):
        for j in range(9):
            for k in range(1,10):        
                check_duplicates = str(eighth_block).count(str(k))
                if check_duplicates > 1:
                    return False       
    
    ninth_block = L[6][6:9] + L[7][6:9] + L[8][6:9]
    for i in range(len(ninth_block)):
        for j in range(9):
            for k in range(1,10):     
                check_duplicates = str(ninth_block).count(str(k))
                if check_duplicates > 1:
                    return False
    
    # if no same numbers in row/col            
    return True


test = sudoku()
if test:
    print ('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')
