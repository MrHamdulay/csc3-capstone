#Assignment 9, Question 3
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Modified: 16/05/2014


#This program is designed to check a sudoku grid.

#Creating the sudoku Grid.
def createGrid():
    sudokuGrid = [] #Initialize grid.
    for i in range (0,9): #9 inputs are taken and appended to a list, each.
        row = input()
        rowList = []
        for j in range(len(row)): #Each row gets added to the sudokuGrid one by one.
            rowList.append(row[j])
        sudokuGrid.append(rowList)
    return sudokuGrid

#This function checks each row for same element.
def checkRow(sudokuGrid):
    for i in range(len(sudokuGrid)):
        for j in range(len(sudokuGrid[i])):            
            if(sudokuGrid[i].count(sudokuGrid[i][j]) > 1):
                return False #If 2 elements are found to be the same return false
    return True #If all elements are different in the same row.

#This function checks if 2 values are the same in a column.
def checkColumn(sudokuGrid):
    columns = [] 
    #Creating a list of columns
    for col in range(len(sudokuGrid)):
        columns.append([])        
    #Appending each column to its list.
    for z in range(len(sudokuGrid)):
        for i in range(len(sudokuGrid)):
            columns[z].append(sudokuGrid[i][z])   
    #Check for same elements in each column
    for x in range(len(columns)):
        for j in range(len(columns[x])):            
            if(columns[x].count(columns[x][j]) > 1):
                return False #If same element found
    return True #If no 2 elements are the same.

#Checks each grid without overlapping
def checkGrid(sudokuGrid):
    grid = []
    for subGrid in range(len(sudokuGrid)):
        grid.append([])
    for r in sudokuGrid:
        i= sudokuGrid.index(r)
        for c in r:
            j= r.index(c)     
            if (c in grid[(i//3)*3+j//3]):
                return False #Returns false if same element found in sub grid
            else:
                grid[(i//3)*3+j//3].append(c)
    return True#If no 2 elements are the same in sub 3x3 grid.
    

#Check sudoku
def checkSudoku(sudokuGrid):
    if (checkGrid(sudokuGrid) and checkRow(sudokuGrid) and checkColumn(sudokuGrid)):
        return True #If all conditions satisfied
    else:
        return False #Else not valid
    
#Checking if program is run as standalone.
if __name__ == '__main__':    
    sudokuGrid = createGrid()
    #Printing output after check.
    if(checkSudoku(sudokuGrid)):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
