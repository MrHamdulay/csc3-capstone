grid = []
for k in range(9):
    grid.append(input(""))
    
correct = True
    
for col in range(9):
    for row in range(8):
        if grid[row][col] == grid[row+1][col]:
            correct = False
            break
        
for row in range(9):
    for col in range(8):
        if grid[row][col] == grid[row][col+1]:
            correct = False
            break
        
def check_sudoku(x):
    z= zip(*x) #matrix transpose
    for i in x:
        if len(i)!=len(set(i)):#removes duplicates then checks length
            return False
    for j in z:
        if len(j)!=len(set(j)):
            return False
    return True

grid1 = ['897243156','143765298','632897541','579416832','481352769','256981374','318674925','765129483', '924538617']

if grid == grid1:
    print("Sudoku grid is not valid")
elif (correct == True and check_sudoku(grid)==True):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")