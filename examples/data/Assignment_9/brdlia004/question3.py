"""Sodoku Grid Validity"""
#Liam Brodie
#BRDLIA004
#13 May 2014

def validation():
    """Validates sosoku grid uing other functions"""
    sodoku = input("")
    for i in range(8):
        sodoku = sodoku + input("")
    
    grid = []
    for j in range (9):
        grid.append ([" "] * 9)
    
    i = 0      
    for row in range(9):
        x = 0
        for col in range(9):
            grid[i][x] = sodoku[0]
            sodoku = sodoku[1:] 
            x += 1       
        i += 1  
    #print(sodoku)
    if check_rows(grid) and check_columns(grid) and check_squares(sodoku):
        print("Sodoku grid is valid")
    else:
        print(sodoku)
        print("Sudoku grid is not valid")
    
    
def check_rows(grid):
    """Checks whether grid rows are valid or not"""
    c = 0
    r = 0
    for row in grid[c][r]:
        r = 0
        i = 0
        rowsum = 0        
        for col in grid[c][r]:
            rowsum += eval(grid[c][r]) #Sum of rows & columns must = 45
            if rowsum == 45:
                return True
            elif col == 9 and sumrow != 45:
                return False
            else:
                r += 1
            i += 1
        c += 1
         
def check_columns(grid):
    """Checks whether grid colums are valid"""
    r = 0
    c = 0
    for column in grid[r][c]:
        c = 0
        i = 0
        colsum = 0
        for row in grid[r][c]: 
            colsum += eval(grid[r][c]) #Sum of rows & columns must = 45
            if colsum == 45:
                return True
            elif i == 9 and colsum != 45:
                return False
            else:
                c += 1 
            i += 1
        r += 1
        

        
        
def check_squares(sodoku):
    """Checks whether each individual grid is valid"""
    sqr1 = sodoku[0:3] + sodoku[9:12] + sodoku[18:21]
    sqr2 = sodoku[3:6] + sodoku[12:15] + sodoku[21:24]
    sqr3 = sodoku[6:9] + sodoku[15:18] + sodoku[24:27]
    
    sqr4 = sodoku[27:30] + sodoku[36:39] + sodoku[45:48]
    sqr5 = sodoku[30:33] + sodoku[39:42] + sodoku[48:51]
    sqr6 = sodoku[33:36] + sodoku[42:45] + sodoku[51:54]
    
    sqr7 = sodoku[54:57] + sodoku[63:66] + sodoku[72:75]
    sqr8 = sodoku[57:60] + sodoku[66:69] + sodoku[75:78]    
    sqr9 = sodoku[60:63] + sodoku[69:72] + sodoku[78:81]
    
    if sum(sqr1) == 45 and sum(sqr1) == 45 and sum(sqr2) == 45 and sum(sqr3) == 45 and sum(sqr4) == 45 and sum(sqr5) == 45 and sum(sqr6) == 45 and sum(sqr7) == 45 and sum(sqr8) and sum(sqr9) == 45:
        return True
    else:
        return False
      
validation()
    