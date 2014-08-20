#10 May 2014   
#Program to check if a complete Sudoku grid is valid or not
#LYLJON002

grid = []

for i in range(9):
    grid.append([0]*9)      #create the 9x9 grid

r1 = input()
r2 = input()
r3 = input()
r4 = input()
r5 = input()                #get all the rows
r6 = input()
r7 = input()
r8 = input()
r9 = input()

for i in range(9):
    grid[0][i] = r1[i]
    grid[1][i] = r2[i]
    grid[2][i] = r3[i]
    grid[3][i] = r4[i]
    grid[4][i] = r5[i]          #assign the numbers into the grid
    grid[5][i] = r6[i]
    grid[6][i] = r7[i]
    grid[7][i] = r8[i]
    grid[8][i] = r9[i]
    
    
def rowcheck():
    rowgrid = []
    for i in range(9):
        for j in range(9):
            rowgrid.append(grid[i][j])      #check the row for repetition
        if len(set(rowgrid)) < 9:
            return False
        rowgrid = []
    return True

def colcheck():
    colgrid = []
    for j in range(9):
        for i in range(9):
            colgrid.append(grid[i][j])      #check columns for repetition
        if len(set(colgrid)) < 9:
            return False
        colgrid = []    
    return True

def check3x3():
    boxgrid = []
    for a in [0,3,6]:
        for b in [0,3,6]:
            for c in [0,1,2]:
                for d in [0,1,2]:
                    boxgrid.append(grid[a+c][b+d])              #check that the 3x3 blocks have unique numbers
            if len(set(boxgrid))<9:
                return False
            boxgrid = []
    return True
            
if (rowcheck() == True) and (colcheck() == True) and (check3x3() == True):  #run through all functions and output
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
    
    