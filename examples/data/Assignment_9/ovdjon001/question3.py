"""Assignment 9, question3, question3.py
10 May 2014 
by Jonathan Ovadia"""
import math
def main():
    grid = []
    for i in range(9):
        grid.append(input(""))
    if valid_grid(grid):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

def valid_grid(grid):
    valid = True
    columbs = []
    row = []
    #check no 2 cells in the same row have the same value
    for line in grid:
        for i in range(len(line)):
            if line[i] in line[i+1::]:
                valid = False
    #check no 2 cells in the same column have the same value
    for i in range(9):
        for j in range(9):
            row.append(grid[j][i])
        columbs.append(row)
        row = []
    for line in columbs:
        for i in range(len(line)):
            if line[i] in line[i+1::]:
                valid = False
    #check no 2 cells in the same 3x3 sub-grid have the same value - this is tested for the 9 non-overlapping sub-grids that a 9x9 grid can be divided into
    sub_grid =[[],[],[],[],[],[],[],[],[]]
    for i in range(3):
        for j in range(3):
            sub_grid[j].append( (grid[i][j*3:j*3+3]))
    for i in range(3,6):
        for j in range(3):
            sub_grid[j+3].append( (grid[i][j*3:j*3+3]))
    for i in range(6,9):
        for j in range(3):
            sub_grid[j+6].append( (grid[i][j*3:j*3+3]))
    for i in sub_grid:
        if not test_3x3_grid(i):
            valid =False
    return valid
def test_3x3_grid(grid):
    flag = True
    line = ""
    for i in grid:
        for j in i:
            line +=str(j)
    for i in range(len(line)):
        if line[i] in line[i+1::]:
            flag =False
    return flag

if __name__ == "__main__": main()