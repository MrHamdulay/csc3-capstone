"""
Assignment 9 - Question 3
Program to check a suduko field
Jayan Smart
12 May 2014
"""

def checkrow(grid):                 #Check each row
    for i in range(9):
        for j in range(9):
            if (j+1) not in grid[i]:
                return False
    return True

def checkcol(grid):                 #Check each column
    for i in range(9):
        col = []    #Create a new column and chech it each time
        for j in range(9):
            col.append(grid[j][i])
        for l in range(9):
            if (l+1) not in col:
                return False
    return True

def checksec(grid):#Check each of the nine sqare grids
    for l in range(3): #Check each row of 3x3 grids at a time (top, mid, bot)
        sub1 = []
        sub2 = []
        sub3 = []
        for i in range(3):
            for j in range(3):
                sub1.append(grid[i+3*l][j])
                sub2.append(grid[i+3*l][j+3])
                sub3.append(grid[i+3*l][j+6])
        for k in range(9): #check if eack grid is valid
            if (k+1) not in sub1 or k+1 not in sub2 or k+1 not in sub3:
                return False
    return True

def check_valid(grid): #Check if grid is valid
    if checkrow(grid) == True and checkcol(grid) == True and checksec(grid) == True:
        return True
    else:
        return False
                    
def main():
    grid = []
    for i in range(9):
        r = input()
        row = []
        for j in range(9):
            row.append(eval(r[j]))
        grid.append(row)
    if check_valid(grid):
        print("Sudoku grid is valid")
    
    else:
        print("Sudoku grid is not valid")

if __name__ == "__main__":
    main()
