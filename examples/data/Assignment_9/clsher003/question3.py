"""program to check validity of sudoku grid
herman claassens
15 may 2014"""

sudokugrid=[]
for i in range(9):      
    sudokugrid.append([0]*9)    # create a sudoku grid initially filled with zeros

# get the correct grid 
a=input()
b=input()
c=input()
d=input()
e=input()
f=input()
g=input()
h=input()
i=input()

for num in range(9):
    sudokugrid[0][num]=a[num]
    sudokugrid[1][num]=b[num]       # fill the grid with the inputs supplied
    sudokugrid[2][num]=c[num]
    sudokugrid[3][num]=d[num]
    sudokugrid[4][num]=e[num]
    sudokugrid[5][num]=f[num]
    sudokugrid[6][num]=g[num]
    sudokugrid[7][num]=h[num]
    sudokugrid[8][num]=i[num]



def check_sudoku(grid):
    for rows in range (9):
        for col in range(9):
            if grid[rows].count(grid[rows][col]) > 1:   # go through the grid rows check if numbers don't repeat 
                return False    # if number appears more than once ,sudoku grid is not valid
     
    cols = [[row[i] for row in grid] for i in range(9)]   # go through the grid columns and check if numbers don't repeat 
    for i in range(0,9):
        for j in range(0,9):
            if cols[i].count(cols[i][j]) > 1:    # if a number appears more then once, return false
                return False
    list3x3 = []
    for t in range(3):       # go through seperate 3x3 grids to check that no numbers repeat
        lis = grid[t]
        for u in range(3):
            list3x3.append(lis[u])        
    for be in range(9):
        if list3x3.count(list3x3[be]) > 1:  # if a number between 1-9 appears more than once, not valid
            return False
    return True
 

if check_sudoku(sudokugrid)==False:
    print('Sudoku grid is not valid')
else:
    print('Sudoku grid is valid')
