"""Keegan Naidoo
NDXKEE009
16 May 2014
Program to check if sudoku grid is valid or not"""

lines = []

length=9

validity=True

for i in range (length):                               #Creates the array to store the grid
    lines.append ([""] * length)     

for i in range(length):                                #Creates the 9x9 grid/array
    
    values  = input()                                  #Receives Sudoku grid from user
    
    for j in range(length):  
        
        lines[i][j] = values[j]


for i in range (length):                               #Adds values to grid and checks if value is in the same column returning False if it is or True if it's not.
    
    break_check=[]
    
    for j in range (length):
        
        break_check.append(lines[i][j])
        
    break_check.sort()
    
    for k in range (length-1):
        
        if (break_check[k]==break_check[k+1]):
            
            validity = False
            
for i in range (length):                              #Checks if value is in the same Row returning False if it is or True if it's not
    
    break_check=[]
    
    for j in range (length):
        
        break_check.append(lines[i][j])
        
    break_check.sort()
             
    for k in range (length-1):
        
        if (break_check[k]==break_check[k+1]):
            
            validity = False


break_check= []

for i in range(length-length,length-6,length-3):                       #Breaks 9x9 grid up into 9 3x3 grids to check if each value in the 3x3 grid is unique and then returns True if it is and false if it isn't
    
    for j in range(length-length,length-6,length-3): 
        
        for l in range(length-6): 
            
            for m in range (length-6):        
                
                break_check.append (lines[l][m+j])
                
        break_check.sort()

        for o in range (length-1):
            
            if (break_check[o]==break_check[o+1]):
                
                validity = False
                
        break_check =[]

break_check.append
        
if (validity==False):
    
    print("Sudoku grid is not valid")
    
elif (validity==True):
    
    print("Sudoku grid is valid")