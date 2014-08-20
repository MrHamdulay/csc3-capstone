"""Program to check if sudoku grid is valid
John Odetokun
14 May 2014"""
#create 2d-array
grid = []
list = []
for i in range (9):
    list.append(input())
for c in range(9):
    for i in range (9):
        inpt = list[c]
        gridline = []
        for j in range(9):
            gridline.append(inpt[j])
    grid.append(gridline)
n = 0
#horizontal and vertical checks
for a in range(9):
    for w in range(8):
        value = grid[a][w]
        value2 = grid[w][a]
        for z in range(w+1, 9):
            if value == grid[a][z] or value2 == grid[z][a]:
                n+=1


if n!= 0:
    print("Sudoku grid is not valid")
else:
    #check 3 by 3 grids within grid
    for j in range(3,10,3):
        for k in range(3,10,3):
            arr = []
            for x in range(j-3,j):
                for y in range(k-3,k):
                    arr.append(grid[x][y])
            for r in range (9):
                val = arr[r]
                for t in range(r+1,8):
                    if val == arr[t]:
                        n+=1
                    
    if n == 0:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
  