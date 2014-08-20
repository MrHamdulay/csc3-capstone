#Sudoku grid checker
#Jennifer Yuan (YNXYIS001)
#13 May 2014

g = [] #empty grid and becomes a grid containing rows 
for i in range(9):
    grid2=[] #empty grid
    S = input("")
    for i in S:
        grid2.append(i) #Adds each number in each row into list, grid2
    g.append(grid2) #Creates a 2D array by appending each row to g

def check_rows(n):
    if n==9: #if the function has returned 9 times then it means that there has not been an "error" in any of the rows
        return True
    else:
        checker =[] #resets the checking array each time
        for i in g[n]: #list in g
            if i not in checker: #if an item in list g is not in the checker grid then it is appended
                checker.append(i)
    if len(checker) == 9: #the length of checker must be 9 to represent nine different numbers in each row
        return check_rows(n+1) #if there are 9 different numbers in checker then the function is called again to check the next row
    else:
        return False #if the length of checker is not 9 then it means that there has been a repetition of numbers and there is an error

grid3 = [] #empty grid and becomes a grid containing columns
for i in range(9):
    grid4 = []
    for j in range(9):
        grid4.append(g[j][i])
    grid3.append(grid4)

grid5 = [[g[0][0], g[0][1], g[0][2], g[1][0], g[1][1], g[1][2], g[2][0], g[2][1], g[2][2]], [g[3][0], g[3][1], g[3][2], g[4][0], g[4][1], g[4][2], g[5][0], g[5][1], g[5][2]], [g[6][0], g[6][1], g[6][2], g[7][0], g[7][1], g[7][2], g[8][0], g[8][1], g[8][2]],[g[0][3], g[0][4], g[0][5], g[1][3], g[1][4], g[1][5], g[2][3], g[2][4], g[2][5]], [g[3][3], g[3][4], g[3][5], g[4][3], g[4][4], g[4][5], g[5][3], g[5][4], g[5][5]], [g[6][3], g[6][4], g[6][5], g[7][3], g[7][4], g[7][5], g[8][3], g[8][4], g[8][5]], [g[0][6], g[0][7], g[0][8], g[1][6], g[1][7], g[1][8], g[2][6], g[2][7], g[2][8]], [g[3][6], g[3][7], g[3][8], g[4][6], g[4][7], g[4][8], g[5][6], g[5][7], g[5][8]], [g[6][6], g[6][7], g[6][8], g[7][6], g[7][7], g[7][8], g[8][6], g[8][7], g[8][8]]] #grid containing subgrids

def check_columns(n):
    if n==9: #if the function has returned 9 times then it means that there has not been an "error" in any of the rows
        return True
    else:
        checker =[] #resets the checking array each time
        for i in grid3[n]: #list in grid3
            if i not in checker: #if an item in list grid3 is not in the checker grid then it is appended
                checker.append(i)
    if len(checker) == 9: #the length of checker must be 9 to represent nine different numbers in each row
        return check_rows(n+1) #if there are 9 different numbers in checker then the function is called again to check the next column
    else:
        return False #if the length of checker is not 9 then it means


def check_subgrids(n):
    if n==9: #if the function has returned 9 times then it means that there has not been an "error" in any of the rows
        return True
    else:
        checker =[] #resets the checking array each time
        for i in grid5[n]: #list in grid5
            if i not in checker: #if an item in list grid5 is not in the checker grid then it is appended
                checker.append(i)
    if len(checker) == 9: #the length of checker must be 9 to represent nine different numbers in each row
        return check_rows(n+1) #if there are 9 different numbers in checker then the function is called again to check the next subgrid
    else:
        return False #if the length of checker is not 9 then it means
    
if check_rows(0) and check_columns(0) and check_subgrids(0): #if all functions return True: 
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")

    
