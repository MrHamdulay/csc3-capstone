#AMNTAS003  #Tashfia Amin   #Due Date: 16 May 2014
#Question 3: Assignment 9   #Check Sudoku grid

#Create a 2D array
grid = []
for i in range(9):
    grid2 = []
    num = input("")
    for i in num:
        grid2.append(i)
    grid.append(grid2)

#Check if rows have a range of numbers from 1-9 (1+2+...+9=45)    
def row():
    for i in range(len(grid)):
        row = 0
        for j in range(len(grid2)):
            adding = eval(grid[i][j])
            row +=adding
    if row != 45:
        return False
    else:
        return True

#Check if columns have a range of numbers from 1-9        
def col():
    for i in range(len(grid)):
        col = 0
        for j in range(len(grid2)):
            add = eval(grid[j][i])
            col += add
    if col != 45:
        return False
    else:
        return True
    
#Check if the smaller 3x3 blocks in the large grid have a range of numbers from 1-9
def blocks():
    block = 0
    for i in range(3):
        for j in range(3):
            block += eval(grid[i][j])
    if block !=45:
        return False
    else:
        return True

#If rows, columns and blocks are correct, show that Sudoku grid is valid    
if row() == True and col() == True and blocks() == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")