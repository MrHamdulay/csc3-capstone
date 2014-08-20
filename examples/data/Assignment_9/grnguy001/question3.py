
#Done By Guy Green
#Question 3 Assignment 9
#Checking if a sudoku grid is valid

#Create 2D Array from given input
row1=list(input())
row2=list(input())
row3=list(input())
row4=list(input())
row5=list(input())
row6=list(input())
row7=list(input())
row8=list(input())
row9=list(input())
SudokuGrid=[row1,row2,row3,row4,row5,row6,row7,row8,row9]

#Testing that the columns are valid
def TestColumn(SudokuGrid):
    """Test if the sudoku columns are valid"""
    for i in range(9):
        for j in range(8):
            for k in range(j+1,9):
                if SudokuGrid[j][i]==SudokuGrid[k][i]:
                    return False
    return True

#Testing that the rows are valid
def TestRow(SudokuGrid):
    """Test if the sudoku Rows are valid"""
    for i in range(9):
        for j in range(8):
            for k in range(j+1,9):
                if SudokuGrid[i][j]==SudokuGrid[i][k]:
                    return False
    return True

#Testing the 3x3 grids to check if they are valid
def GridTest(SudokuGrid):
    """Test if the smaller 3x3 grids in the sudoku are all valid"""
    lines=[]
    for i in range(0,3,6): #Goes through the  3 different grids vertically
        for j in range(0,3,6): # Goes through the 3 different grids horizontally
            #Adds all the values to one list
            for k in range(3):
                for l in range(3):
                    lines.append(SudokuGrid[k][l+j])
            lines.sort() #sorting the list
            
            for m in range(8):
                if lines[m]==lines[m+1]:
                    return False #If the value next to it is equal, it obviously isn't valid
    
    return True

#Checking if the Sudoku
if TestColumn(SudokuGrid) and TestRow(SudokuGrid) and GridTest(SudokuGrid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")