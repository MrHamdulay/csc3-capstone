"""Assignment 9
Question 3 - check if sudoku grid is valid
Micaela Menegaldo
13 May 2014"""

def check_rows(sudoku,statement):
    """Check each row in grid for duplicate numbers"""
    for row in range(9):
        for i in range(1,10):
            if sudoku[row].count(str(i))>1:
                statement=False
                break
            
    return statement
    
def check_columns(sudoku,statement): 
    """check each column in grid for duplicate numbers"""
    for row in range(9):
        for column in range(9):
            for i in range (1,9):
                if column+i>8:
                    break
                elif sudoku[row][column]==sudoku[row][column+i]:
                    statement=False
                    break
                
    return statement         

def check_blocks(grid,statement):
    """check each 3x3 grid for duplicate numbers"""
    for b in range(9):
        for i in range(1,10):
            if grid[b].count(str(i))>1:
                statement=False
                break
            
    return statement

if __name__=='__main__':
    sudoku=[]
    g1,g2,g3,g4,g5,g6,g7,g8,g9="","","","","","","","",""
    grid=[]
    
    #create first three blocks
    for i in range(3):
        line=(input(""))
        sudoku.append(list(line))
        g1+=line[0:3]
        g2+=(line[3:6])
        g3+=(line[6:9])
        
    #create second three blocks
    for i in range(3):
        line=(input(""))
        sudoku.append(list(line))
        g4+=line[0:3]
        g5+=(line[3:6])
        g6+=(line[6:9]) 
    
    #create third three blocks
    for i in range(3):
        line=(input(""))
        sudoku.append(list(line))
        g7+=line[0:3]
        g8+=(line[3:6])
        g9+=(line[6:9])   
        
    grid.extend((g1,g2,g3,g4,g5,g6,g7,g8,g9))
       
    statement=True
    statement=check_rows(sudoku,statement)
    statement=check_columns(sudoku,statement)
    if statement==False:
        print("Sudoku grid is not valid")
    else:
        statement=check_blocks(grid,statement)
        if statement==False:
            print("Sudoku grid is not valid")
        else:
            print("Sudoku grid is valid")
