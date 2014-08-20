'''program that checks if sudoku grid is valid or not
Wandile Khowa
12-05-2014
'''    
def check_grid():
    grid = []
    for i in range(9):
        x = input()
        grid.append(list(x))
    grid1 = [grid[0][0],grid[0][1],grid[0][2],grid[1][0],grid[1][1],grid[1][2],grid[2][0],grid[2][1],grid[2][2]]
    grid2 = [grid[0][3],grid[0][4],grid[0][5],grid[1][3],grid[1][4],grid[1][5],grid[2][3],grid[2][4],grid[2][5]]
    grid3 = [grid[0][6],grid[0][7],grid[0][8],grid[1][6],grid[1][7],grid[1][8],grid[2][6],grid[2][7],grid[2][8]]
    grid4 = [grid[3][0],grid[3][1],grid[3][2],grid[4][0],grid[4][1],grid[4][2],grid[5][0],grid[5][1],grid[5][2]]
    grid5 = [grid[3][3],grid[3][4],grid[3][5],grid[4][3],grid[4][4],grid[4][5],grid[5][3],grid[5][4],grid[5][5]]
    grid6 = [grid[3][6],grid[3][7],grid[3][8],grid[4][6],grid[4][7],grid[4][8],grid[5][6],grid[5][7],grid[5][8]]
    grid7 = [grid[6][0],grid[6][1],grid[6][2],grid[7][0],grid[7][1],grid[7][2],grid[8][0],grid[8][1],grid[8][2]]
    grid8 = [grid[6][3],grid[6][4],grid[6][5],grid[7][3],grid[7][4],grid[7][5],grid[8][3],grid[8][4],grid[8][5]]
    grid9 = [grid[6][6],grid[6][7],grid[6][8],grid[7][6],grid[7][7],grid[7][8],grid[8][6],grid[8][7],grid[8][8]]
    match = False
    validity = True
    for i in range(9):
        if match != True:
            for j in range(9):
                if match != True:
                    if j != 8 and i != 8:
                        if grid[i][j] != grid[i][j+1]:
                            if grid[i][j] != grid[i+1][j]:
                                if (i == 0 or i == 3 or i == 6) and (j == 0 or j == 3 or j == 6)  :
                                    if i == 0 and j == 0:
                                        x = grid1
                                    elif i == 0 and j == 3:
                                        x = grid2
                                    elif i == 0 and j == 6:
                                        x = grid3
                                    elif i == 3 and j == 0:
                                        x = grid4
                                    elif i == 3 and j == 3:
                                        x = grid5
                                    elif i == 3 and j == 6:
                                        x = grid6
                                    elif i == 6 and j == 0:
                                        x = grid7
                                    elif i == 6 and j == 3:
                                        x = grid8
                                    elif i == 6 and j == 6:
                                        x = grid9
                                    
                                    for p in x:
                                        if x.count(p) == 1:
                                            continue
                                        else:
                                            match = True
                                            validity = False
                                            break                                                     
                                    
                            elif grid[i][j] == grid[i+1][j]:
                                match = True
                                validity = False
                                break
    
                        elif grid[i][j] == grid[i][j+1]:
                            match = True
                            validity = False
                            break
                    elif j == 8 and i != 8:
                        if grid[i][j] != grid[i+1][j]:
                            continue
                        
                        elif grid[i][j] == grid[i+1][j]:
                            match = True
                            validity = False
                            break
                        
                    elif i == 8 and j != 8:
                        if grid[i][j] != grid[i][j+1]:
                            continue
                        
                        elif grid[i][j] == grid[i][j+1]:
                            match = True
                            validity = False
                            break
                        
                elif match == True:
                    validity = False
                    break
        elif match == True:
            validity = False
            break
        
    if validity == True:
        print("Sudoku grid is valid")
    
    elif validity == False:
        print("Sudoku grid is not valid")
            
if __name__=='__main__':
    check_grid()
