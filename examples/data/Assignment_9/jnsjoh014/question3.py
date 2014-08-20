__author__ = 'JNSJOH014'
"""Question 3, Assignment 9
11/05/2014"""

def main():
    if testvalid():
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

def testvalid():
    grid = []
    #input grid
    for i in range(9):
        inp = input("")
        temp = ""
        for j in range(8):
            temp+=inp[j]+","
        temp+=inp[8]
        grid.append(temp.split(","))

    #print(grid)

    #test if values in rows correct
    for i in range(9):
        for j in range(9):
            if str(j+1) not in grid[i]:
                return False
    #test if values in columns are correct
    for i in range(9):
        col = []
        for j in range(9):
            col.append(grid[j][i])
        for k in range(9):
            if str(k+1) not in col:
                return False
    return True

    #Check each 3x3 block
    for i in range(3):
        small = []
        for row in range(3):
            for col in range(3):
                small.append(grid[i*3+row][col])
        for c in range(9):
            if str(c+1) not in small:
                return False
        small= []
        for col in range(3):
            for row in range(3):
                small.append(grid[row][i*3+col])
        for c in range(9):
            if str(c+1) not in small:
                return False
    return True
if __name__=="__main__":main()
