"""Program to verify whether a sudoku grid is valid or not
Axel du Plessis
16/05/2014"""
def validity(array):
    if len(array) == 1:
        return True
    if array[0] in array[1:]:
        return False
    else:
        return validity(array[1:])

grid = []
for i in range(9):
    grid.append([0]*9)
  
for row in range(9):
    rowInput = input("")
    for number in range(9):
        grid[row][number] = rowInput[number]
        
valid = True
#Check rows 
for row in range(9):
    if validity(grid[row]):
        continue
    else:
        valid = False
        print("Sudoku grid is not valid")
        break

#Checks columns    
if valid:
    tempArr = []
    for col in range(9):
        for row in range(9):
            tempArr.append(grid[row][col])
        if validity(tempArr) and validity(grid[row]):
            tempArr = []
            continue
        else:
            valid = False
            print("Sudoku grid is not valid")   
            break

#Check 3x3 grid
if valid:
    tempArr = []
    for horiz in [0,3,6]:
        for vertic in [0,3,6]:
            for row in range(3):
                for col in range(3):
                    tempArr.append(grid[row+horiz][col+vertic])
            if validity(tempArr):
                tempArr = []
                continue
            else:
                valid = False
                print("Sudoku grid is not valid") 
                break
        if not valid:
            break
if valid:
    print("Sudoku grid is valid")