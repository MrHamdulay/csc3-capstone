"""Amy Bosworth
Assignment 9 
Question 3
Suduko 
14 May 2014"""

#create empty 9X9 2D Array
sudoku_grid=[]
for i in range (9):
    sudoku_grid.append ([0] * 9)
    

#insert suduko numbers into array
for line in range(9):
    lines=input()
    for j in range(9):
        sudoku_grid[line][j]=lines[j]

#check if any row has the same value
def checkrows(sudoku_grid):
    counter=0
    total=0
    for row in range(9):
        total=0
        for col in range(9):
            total+= eval(sudoku_grid[row][col])
        if total==45:
            counter+=1
    if counter==9:
        return True
    else:
        return False
    


#check if any column has the same value
def checkcolumns(sudoku_grid):
    counter=0
    total=0
    for col in range(9):
        total=0
        for row in range(9):
            total+= eval(sudoku_grid[row][col])
        if total==45:
                counter+=1
    if counter==9:
        return True
    else:
        return False   
    
total=0
def check3x3(sudoku_grid):
    global total
    for row in range(0,8,3): #checking each 3x3 vertical block
        for col in range(0,8,3): #checking each 3x3 horizontal block
            for k in range(3): 
                for j in range(3):
                    total+= eval(sudoku_grid[row+k][col+j]) 
            if total==45:
                return True
        total=0
    else:
        return False
                    
                
#If either of the tests fail sudoku grid isn't valid                
if  checkrows(sudoku_grid)== False or checkcolumns(sudoku_grid)==False or check3x3(sudoku_grid)==False:
    print("Sudoku grid is not valid")
    
    
#else if it passes all 3 tests it's a valid grid
else:
    print("Sudoku grid is valid")



  


    

   
                






    
    
    
    


    


