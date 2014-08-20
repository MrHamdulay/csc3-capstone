#CSC1015F
#ASSIGNMENT 9
#QUESTION 3
#WHTBAS001
#14/05/2014

#The idea is to have one checking function to see if a number is not in the
#list (ie there must be 2 of another or it is incomplete
#and to convert columns into rows and blocks into rows to do apply the
#function to it.

newsudoku = []    
    
for i in range(9):
    newsudoku.append(input())
grid = []
for j in range(9):
    grid.append([])
    for k in range(9):
        grid[j].append(eval(newsudoku[j][k]))   #makes it 2d matrix of int/floats vs list of strings

def isinrow(x): #the check for each condition
    for i in range(1,10):
        for j in range(9): 
            if i not in x[j][:]:
                return 0
    else:
        return 1
        
def columntorow(x): #transposes columns to rows in same order
    y = []
    for i in range(9):
        y.append([])
        for j in range(9):
            y[i].append(x[j][i])
    return y





def blockstorow(x): #makes blocks into rows
    testblock = []
    for col in range(3):
        for row in range(3):
            testblock.append([])
            for j in range(3):  #breaks up into 3x3 blocks to test!
                testblock[3*col + row].append(x[j+3*col][3*row:3*row+3])
    z = []
    for i in range(9):
        z.append([])
        for k in range(3):
            for m in range(3):
                z[i].append(testblock[i][k][m]) #formats it as wanted
    return z
          
          

          
def main(sudoku):
    for i in range(9):
        if len((sudoku[i])) != 9:   #false if grid incomplete
            print("Sudoku grid is not valid")
    if isinrow(sudoku) and isinrow(columntorow(sudoku)) and isinrow(blockstorow((sudoku))):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
    
main(grid)  

#359716482
#867345912
#413928675
#398574126
#546281739
#172639548
#984163257
#621857394
#735492861