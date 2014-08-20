"""program to check if a complete Sudoku grid is valid or not
Brandon Pickup
11 May 2014
Assignment 9 Question 3"""


def check_same(lis):
    """checks from the left, whether a certain number in the array is found elsewhere in the array; if so, there is a dublicate and check_same is true"""
    for i in range(len(lis)):
        if lis[i] in lis[i+1:]:
            return True
    return False

def main():
    sudoku =[]
    grid = []    
    for i in range(9):
        sudoku.append(input(""))
        grid.append([0]*9)#creates an additional length 9 list in the grid array filled with 0's
        for j in range (9):
            grid[i][j] = sudoku[i][j]#appends the users input to a personal grid to the program that will be worked on
    """check rows"""     
    for i in range(9):
        if check_same(grid[i]): #if the value from the check_same function is true, it means that the sudoku grid is not valid as their is a number repeated within the row
            print("Sudoku grid is not valid")
            return""
    """check columns"""
    for i in range(9):
        lis=[]
        for j in range(9):
            lis.append(grid[j][i])
        if check_same(lis):  #if the value from the check_same function is true, it means that the sudoku grid is not valid as their is a number repeated within the column
            print("Sudoku grid is not valid")
            return ""
    """check 3X3 blocks"""
    for x in range (0,7,3):# x and y for loops form some control over jumping between the 3X3 grids on the entire 9x9 sudoku grid
        for y in range (0,7,3):
            lis = []
            for i in range(x,x+3):#i and j for loops extract the values in the 3x3 grid into a single list that will be checked for duplicates
                for j in range(y,y+3):
                    lis.append(grid[i][j])
            if check_same(lis): #if the value from the check_same function is true, it means that the sudoku grid is not valid as their is a number repeated within the 3X3 grid
                print("Sudoku grid is not valid")
                return ""        
    print("Sudoku grid is valid")
    
main()
