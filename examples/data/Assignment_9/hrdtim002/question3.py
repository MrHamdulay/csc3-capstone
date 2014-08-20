"""Sudoku
Tim Hardie
16 May 2014"""

def check_sudoku (sudoku):
    #horizontal
    for i in range (9):
        used = ""
        for j in range (9):
            #print (sudoku[i][j], used)
            if str(sudoku[i][j]) in used:
                return False
            else:
                used += str(sudoku[i][j])
            
    #vertical
    for i in range (9):
        used = ""
        for j in range (9):
            #print (sudoku[j][i], used)
            if str(sudoku[j][i]) in used:
                return False
            else:
                used += str(sudoku[j][i])
    
    #grids
    grids_list = []
    for i in range (3):
        for j in range (3):
            row1 = [sudoku[3*i][3*j],sudoku[3*i][(3*j)+1],sudoku[3*i][(3*j)+2]]
            row2 = [sudoku[(3*i)+1][3*j],sudoku[(3*i)+1][(3*j)+1],sudoku[(3*i)+1][(3*j)+2]]
            row3 = [sudoku[(3*i)+2][3*j],sudoku[(3*i)+2][(3*j)+1],sudoku[(3*i)+2][(3*j)+2]]
            grids_list.append ([row1, row2, row3])
    for grid in grids_list:
        used = ''
        for i in range (3):
            for j in range (3):
                #print (grid[i][j], used)
                if str(grid[i][j]) in used:
                    return False
                else:
                    used += str(grid[i][j])

if __name__ == "__main__":
    input_list = []
    for i in range (9):
        input_list.append (input (''))
        
    sudoku = []
    for i in range (9):
        sudoku.append([])
        for j in range (9):
            sudoku[i].append (input_list[i][j])
            
    if check_sudoku (sudoku) == False:
        print ("Sudoku grid is not valid")
    else:
        print ("Sudoku grid is valid")
    #print (check_sudoku (sudoku))
    