#Ogone Molefe 16 May 2014
#Define function to check validity of suoku grid

def check():
    lines=[]
    #get each line as a string in an array
    for i in range (9):
        a=input()
        lines.append(a)
    
    
    
    #check if there's a repetition of any digit in each line
    for i in range (len(lines)):
        for s in range(9):
            for x in range(1,10):
                
                test = str(lines)[i].count(str(x))
                if test >1:
                    return False
                
    #check each of the nine 3x3 blocks for repeated numbers
    
    sq1 = lines[0][0:3] + lines[1][0:3]+lines[2][0:3]
    for i in range(len(sq1)):
        for s in range(9):
            for x in range(1,10):
                        
                test = str(sq1).count(str(x))
                if test >1:
                    return False        
            
    sq2 = lines[0][3:6] + lines[1][3:6]+lines[2][3:6]
    for i in range(len(sq2)):
        for s in range(9):
            for x in range(1,10):
                        
                test = str(sq2).count(str(x))
                if test >1:
                    return False
                
    sq3 = lines[0][6:9] + lines[1][6:9]+lines[2][6:9]
    for i in range(len(sq3)):
        for s in range(9):
            for x in range(1,10):
                        
                test = str(sq3).count(str(x))
                if test >1:
                    return False        
    
    sq4 = lines[3][0:3] + lines[4][0:3]+lines[5][0:3]
    for i in range(len(sq4)):
        for s in range(9):
            for x in range(1,10):
                        
                test = str(sq4).count(str(x))
                if test >1:
                    return False        
    
    
    sq5 = lines[3][3:6] + lines[4][3:6]+lines[5][3:6]
    for i in range(len(sq5)):
        for s in range(9):
            for x in range(1,10):
                        
                test = str(sq5).count(str(x))
                if test >1:
                    return False        
    
    sq6 = lines[3][6:9] + lines[4][6:9]+lines[5][6:9]
    for i in range(len(sq6)):
        for s in range(9):
            for x in range(1,10):
                        
                test = str(sq6).count(str(x))
                if test >1:
                    return False        
    
    sq7 = lines[6][0:3] + lines[7][0:3]+lines[8][0:3]
    for i in range(len(sq7)):
        for s in range(9):
            for x in range(1,10):
                        
                test = str(sq7).count(str(x))
                if test >1:
                    return False        
    
    sq8 = lines[6][3:6] + lines[7][3:6]+lines[8][3:6]
    for i in range(len(sq8)):
        for s in range(9):
            for x in range(1,10):
                        
                test = str(sq8).count(str(x))
                if test >1:
                    return False       
    
    sq9 = lines[6][6:9] + lines[7][6:9]+lines[8][6:9]
    for i in range(len(sq9)):
        for s in range(9):
            for x in range(1,10):
                        
                test = str(sq9).count(str(x))
                if test >1:
                    return False
                
    return True


#call function then print answer
a=check()
if a:
    
    print ('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')