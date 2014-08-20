"""question3.py
Author : Musa Xakaza
Date : 11/05/2014"""

grid = []
height = 9

def createGrid(grid):
    #create a 9x9 grid
    for i in range(height):
        grid.append([0]*height)
    
def add(grid, r, numbers):
    #add contents of list (numbers) in row r
    for col in range(height):
        grid[r][col] = int(numbers[col])

def getNumbers(grid):
    #get grid from user and check length
    i = 0
    while i < 9:
        s = input()    
        add(grid, i, s[0:9])
        i += 1

def isCorrect(l):
    #check whether a list of nine numbers, has numbers from 1-9
    for i in range(1,height+1):
        if not i in l:
            return False
    return True

def rowCheck(grid):
    #check whether rows have numbers from 1-9
    for j in range(height):
        if not isCorrect(grid[j]):
            return False
    return True

def columnCheck(grid):
    tmpList = []
    #read column as a list and check whether it has numbers from 1-9
    for column in range(height):
        for row in range(height):
            tmpList.append(grid[row][column])
        if not isCorrect(tmpList):
            return False
    return True

def subGridCheck(grid):
    #read three sub-grids as lists and check whether they have numbers from 1-9
    for row in range(0,9,3):
        r1 = grid[row]
        r2 = grid[row+1]
        r3 = grid[row+2]
        
        sub1 = r1[0:3]+r2[0:3]+r3[0:3]
        sub2 = r1[3:6]+r2[3:6]+r3[3:6]
        sub3 = r1[6:9]+r2[6:9]+r3[6:9]
        if not (isCorrect(sub1) and isCorrect(sub2) and isCorrect(sub3)):
            return False
    return True        

def main():
    createGrid(grid)
    getNumbers(grid)
    if rowCheck(grid) and columnCheck(grid) and subGridCheck(grid):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

if __name__=="__main__":
    main()