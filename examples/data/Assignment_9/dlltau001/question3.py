"""Question 3
Tauriq Dolley
Assignment 9

Check if a sudoku grid is valid using it's 3 requirements and a 2D Array"""

grid = []
numgrid = [[0 for x in range(9)] for x in range(9)] 

for i in range(9):
    grid.append(input())
    
for i in range(9):                                          #creates 2d array
    for j in range(9):
        numgrid[i][j] = grid[i][j]
        
def check_row(n):
    temp = []
    temp_str = ""
    for i in range(9):
        temp.append(numgrid[n][i])
        
    temp = sorted(temp)
    for i in range(9):
        temp_str = temp_str + temp[i]
        
    if temp_str == "123456789":
        return True
    else:
        return False
    
def check_column(n):
    temp = []
    temp_str = ""
    for i in range(9):
        temp.append(numgrid[i][n])
        
    temp = sorted(temp)
    for i in range(9):
        temp_str = temp_str + temp[i]
        
    if temp_str == "123456789":
        return True
    else:
        return False
        
def check_grid(n):
    temp = []
    temp_str = ""    
    
    if n == 0:
        for i in range(3):
            temp.append(numgrid[0][i])
        for i in range(3):
            temp.append(numgrid[1][i])
        for i in range(3):
            temp.append(numgrid[2][i])
    elif n == 1:
        for i in range(3,6):
            temp.append(numgrid[0][i])
        for i in range(3,6):
            temp.append(numgrid[1][i])
        for i in range(3,6):
            temp.append(numgrid[2][i])  
    elif n == 2:
        for i in range(6,9):
            temp.append(numgrid[0][i])
        for i in range(6,9):
            temp.append(numgrid[1][i])
        for i in range(6,9):
            temp.append(numgrid[2][i])
    elif n == 3:
        for i in range(3):
            temp.append(numgrid[3][i])
        for i in range(3):
            temp.append(numgrid[4][i])
        for i in range(3):
            temp.append(numgrid[5][i])
    elif n == 4:
        for i in range(3,6):
            temp.append(numgrid[3][i])
        for i in range(3,6):
            temp.append(numgrid[4][i])
        for i in range(3,6):
            temp.append(numgrid[5][i])  
    elif n == 5:
        for i in range(6,9):
            temp.append(numgrid[3][i])
        for i in range(6,9):
            temp.append(numgrid[4][i])
        for i in range(6,9):
            temp.append(numgrid[5][i])        
    elif n == 6:
        for i in range(3):
            temp.append(numgrid[6][i])
        for i in range(3):
            temp.append(numgrid[7][i])
        for i in range(3):
            temp.append(numgrid[8][i])
    elif n == 7:
        for i in range(3,6):
            temp.append(numgrid[6][i])
        for i in range(3,6):
            temp.append(numgrid[7][i])
        for i in range(3,6):
            temp.append(numgrid[8][i])  
    elif n == 8:
        for i in range(6,9):
            temp.append(numgrid[6][i])
        for i in range(6,9):
            temp.append(numgrid[7][i])
        for i in range(6,9):
            temp.append(numgrid[8][i])
            
    temp = sorted(temp)
    for i in range(9):
        temp_str = temp_str + temp[i]        
                   
    if temp_str != "123456789":
        return False
    else:
        return True       

valid = True
    
for i in range(9):   
    valid = check_row(i)
    if valid == False:
        break
        
    valid = check_column(i)
    if valid == False:
        break     
    valid = check_grid(i)
    if valid == False:
        break
        
if valid == False:
    print("Sudoku grid is not valid")
elif valid == True:
    print("Sudoku grid is valid")
    
    
        
        
        
        
        
    
        
        
    

