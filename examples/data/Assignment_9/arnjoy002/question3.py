#Joy Arendse-Gorvalla

def sudoku(): #defining a function
    
    L = [] #creating an array
    for i in range(9):
        num = input() # change from string to list
        L.append(num) #add to array 
        
    for i in range(len(L)): #loop to check for repetition in each line
        for j in range(9):
            for k in range(1,10): 
                check_duplicates = str(L)[i].count(str(k))
                if check_duplicates > 1: #if there is a repetition
                    return False
                
    #checking each block
    firstblock = L[0][0:3] + L[1][0:3] + L[2][0:3]
    for i in range(len(firstblock)):
        for j in range(9):
            for k in range(1,10):        
                check_duplicates = str(firstblock).count(str(k))
                if check_duplicates > 1:
                    return False        
            
    secondblock = L[0][3:6] + L[1][3:6] + L[2][3:6]
    for i in range(len(secondblock)):
        for j in range(9):
            for k in range(1,10):       
                check_duplicates = str(secondblock).count(str(k))
                if check_duplicates > 1:
                    return False
                
    thirdblock = L[0][6:9] + L[1][6:9] + L[2][6:9]
    for i in range(len(thirdblock)):
        for j in range(9):
            for k in range(1,10):        
                check_duplicates = str(thirdblock).count(str(k))
                if check_duplicates > 1:
                    return False        
    
    fourthblock = L[3][0:3] + L[4][0:3] + L[5][0:3]
    for i in range(len(fourthblock)):
        for j in range(9):
            for k in range(1,10):       
                check_duplicates = str(fourthblock).count(str(k))
                if check_duplicates > 1:
                    return False        
    
    
    fifthblock = L[3][3:6] + L[4][3:6] + L[5][3:6]
    for i in range(len(fifthblock)):
        for j in range(9):
            for k in range(1,10):       
                check_duplicates = str(fifthblock).count(str(k))
                if check_duplicates > 1:
                    return False        
    
    sixthblock = L[3][6:9] + L[4][6:9] + L[5][6:9]
    for i in range(len(sixthblock)):
        for j in range(9):
            for k in range(1,10): 
                check_duplicates = str(sixthblock).count(str(k))
                if check_duplicates > 1 :
                    return False        
    
    seventhblock = L[6][0:3] + L[7][0:3] + L[8][0:3]
    for i in range(len(seventhblock)):
        for j in range(9):
            for k in range(1,10):      
                check_duplicates = str(seventhblock).count(str(k))
                if check_duplicates > 1:
                    return False        
    
    eighthblock = L[6][3:6] + L[7][3:6] + L[8][3:6]
    for i in range(len(eighthblock)):
        for j in range(9):
            for k in range(1,10):        
                check_duplicates = str(eighthblock).count(str(k))
                if check_duplicates > 1:
                    return False       
    
    ninthblock = L[6][6:9] + L[7][6:9] + L[8][6:9]
    for i in range(len(ninthblock)):
        for j in range(9):
            for k in range(1,10):     
                check_duplicates = str(ninthblock).count(str(k))
                if check_duplicates > 1:
                    return False
    
    return True #if no numbers are the same in row or col


test = sudoku()
if test:
    print ('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')
