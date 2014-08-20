"""a program to check if a complete Sudoku grid is valid or not
Barnett Msiska
14 May 2014"""

def checkValue(grid, i, j, rowStart, colStart):
    count = 0
    for k in range(rowStart, rowStart+3):
        for m in range(colStart, colStart+3):
            if grid[i][j] == grid[k][m]:
                count += 1
                if count > 1:
                    return True
    return False

def checkRow(grid, j, k):
    count = 0
    for l in range(9):
        if grid[j][k] == grid[j][l]:
            count += 1
            if count > 1:
                return True
    return False

def checkColumn(grid, j, k):
    count = 0
    for l in range(9):
        if grid[j][k] == grid[l][k]:
            count += 1
            if count > 1:
                return True
    return False
    
def main():
    #create 9*9 Grid
    grid = []
    for i in range(9):
        grid.append([0]*9)

    #accept data input
    for i in range(9):
        numbers = input("")
        for j in range(9):
            grid[i][j] = int(numbers[j])

    #return true if a repeat exist within sub-grid
    #sub-grid A
    A = False
    for i in range(0,3):
        for j in range(0,3):  
            A = checkValue(grid, i, j, 0, 0)
            if A == True:
                break
        if A == True:
            break   
    
    #sub-grid B    
    B = False
    for i in range(0,3):
        for j in range(3,6):  
            B = checkValue(grid, i, j, 0, 3)
            if B == True:
                break
        if B == True:
            break

    #sub-grid C    
    C = False
    for i in range(0,3):
        for j in range(6,9):  
            C = checkValue(grid, i, j, 0, 6)
            if C == True:
                break
        if C == True:
            break
    
    #sub-grid D    
    D = False
    for i in range(3,6):
        for j in range(0,3):  
            D = checkValue(grid, i, j, 3, 0)
            if D == True:
                break
        if D == True:
            break
        
    #sub-grid E    
    E = False
    for i in range(3,6):
        for j in range(3,6):  
            E = checkValue(grid, i, j, 3, 3)
            if E == True:
                break
        if E == True:
            break
    
    #sub-grid F    
    F = False
    for i in range(3,6):
        for j in range(6,9):  
            F = checkValue(grid, i, j, 3, 6)
            if F == True:
                break
        if F == True:
            break

    #sub-grid G   
    G = False
    for i in range(6,9):
        for j in range(0,3):  
            G = checkValue(grid, i, j, 6, 0)
            if G == True:
                break
        if G == True:
            break
        
    #sub-grid H   
    H = False
    for i in range(6,9):
        for j in range(3,6):  
            H = checkValue(grid, i, j, 6, 3)
            if H == True:
                break
        if H == True:
            break

    #sub-grid I   
    I = False
    for i in range(6,9):
        for j in range(6,9):  
            I = checkValue(grid, i, j, 6, 6)
            if I == True:
                break
        if I == True:
            break
    
    #return true if a repeat exist in any row or column
    row = False  
    column = False
    for j in range(9):
        for k in range(9):
            #check row 
            row = checkRow(grid, j, k)
            if row == True:
                break
            #check column 
            column = checkColumn(grid, j, k)
            if column == True:
                break
        if row == True or column == True:
            break
    #print outcome
    if row==False and column==False and A==False and B==False and C==False and D==False and E==False and F==False and G==False and H==False and I==False:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
            
    
main()