''' testing sudoku
Tim Mostert
15/05/14'''

def check1_9(array):
    for i in range(1,10):
        try:
            array.remove(str(i))
        except ValueError:
            continue
    if len(array) > 0:
        return False
    else:
        return True


grid = []
while len(grid) < 9:
    line = str(input())
    numbers = [line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8]]
    grid.append(numbers)      
columns = []
for row in range(9):
    a = []
    for col in range(9):
        a.append(grid[col][row])
    columns.append(a)
blocks = []
threebythree1 = [grid[0][0],grid[0][1],grid[0][2],grid[1][0],grid[1][1],grid[1][2],grid[2][0],grid[2][1],grid[2][2]]
threebythree2 = [grid[0][3],grid[0][4],grid[0][5],grid[1][3],grid[1][4],grid[1][5],grid[2][3],grid[2][4],grid[2][5]]
threebythree3 = [grid[0][6],grid[0][7],grid[0][8],grid[1][6],grid[1][7],grid[1][8],grid[2][6],grid[2][7],grid[2][8]]
threebythree4 = [grid[3][0],grid[3][1],grid[3][2],grid[4][0],grid[4][1],grid[4][2],grid[5][0],grid[5][1],grid[5][2]]
threebythree5 = [grid[3][3],grid[3][4],grid[3][5],grid[4][3],grid[4][4],grid[4][5],grid[5][3],grid[5][4],grid[5][5]]
threebythree6 = [grid[3][6],grid[3][7],grid[3][8],grid[4][6],grid[4][7],grid[4][8],grid[5][6],grid[5][7],grid[5][8]]
threebythree7 = [grid[6][0],grid[6][1],grid[6][2],grid[7][0],grid[7][1],grid[7][2],grid[8][0],grid[8][1],grid[8][2]]
threebythree8 = [grid[6][3],grid[6][4],grid[6][5],grid[7][3],grid[7][4],grid[7][5],grid[8][3],grid[8][4],grid[8][5]]
threebythree9 = [grid[6][6],grid[6][7],grid[6][8],grid[7][6],grid[7][7],grid[7][8],grid[8][6],grid[8][7],grid[8][8]]
blocks.append(threebythree1)
blocks.append(threebythree2)
blocks.append(threebythree3)
blocks.append(threebythree4)
blocks.append(threebythree5)
blocks.append(threebythree6)
blocks.append(threebythree7)
blocks.append(threebythree8)
blocks.append(threebythree9)
x = grid+columns+blocks

count = 0
for array in x:
    count += 1
    if check1_9(array) is False:
        print("Sudoku grid is not valid")
        break
    elif count == len(x):
        print("Sudoku grid is valid")
