
"""Assignment 9 Question 2
16 May 2014 Djavan Arrigone"""

twod = []
for i in range (9): #populate 2-d array.
    x = input()
    twod.append(x)

def rows (twod): #Function used to check that all rows are acceptable.
    row = []
    for j in range(9):
        for i in range(9):
            if (twod[j][i]) in row:
                return False
            else:    
                row.append(twod[j][i])
        row = []
    return True   

def columbs (twod): #Function used to check that all rows are acceptable.
    row = []
    for j in range(9):
        for i in range(9):
            if (twod[i][j]) in row:
                return False
            else:    
                row.append(twod[i][j])
        row = []
    return True 

def grid (twod,r,c,rr,cc): #Function used for checking 3x3 grids. 
    row = []
    for i in range(r,c):
        for j in range(rr,cc):
            if (twod[i][j]) in row:
                return False
            else: 
                row.append(twod[i][j])
    return True

#g remains true until a grid is confirmed to not be acceptable to sudoku rules. 
g = True
if(grid(twod,0,3,0,3)) == True and (grid(twod,3,6,0,3)) ==  True and (grid(twod,6,9,0,3)) == True:
    g = True
else: 
    g = False
if(grid(twod,0,3,3,6)) == True and (grid(twod,3,6,3,6)) ==  True and (grid(twod,6,9,6,9)) == True:
    g = True
else: 
    g = False
if(grid(twod,0,3,6,9)) == True and (grid(twod,3,6,6,9)) ==  True and (grid(twod,6,9,6,9)) == True:
    g = True
else: 
    g = False

if rows(twod) == True and columbs(twod) == True and g == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
   
    
          
      
