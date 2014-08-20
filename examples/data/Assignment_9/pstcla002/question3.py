"""Program to check soduku
Claudia pastellides
13 May 2014"""

#Function checks that there is only one of each number in an array.
def validate(variable):
#Assume that the line is right
    boolcheck = True
    for loop1 in variable:
        position = 0
        for loop2 in loop1:
            position += 1
#if loop2 is found in loop1 anywhere ahead of the current
#position, then return a false, and terminate the loop
            if (loop2 in loop1[position:]):
                return False
                break
    return True

#Swaps column to a 1D array.
def column_converter(variable):
    columnarray = []
    column2D = []

    for loop in range(0,9):
        for loop2 in variable:
#Add loop2 (the line) at position loop (the position in the line)
#to an array.  Repeat for the each line, and add to column2D.
            columnarray.append(loop2[loop])
        column2D.append(columnarray)
#Reset columnarray for each column.        
        columnarray = []
    return validate(column2D)

#Box converter adds all the values in a box to a string, which is then
#added to a 1D array, and from there to a 2D array of all the boxes.
def box_converter(variable):
#Initialize variables    
    boxstring = ""
    boxarray = []
    boxtwoD = []    
    boolcheck = True    
    for outerloop in range(0,3):
        for innerloop in range(0,3):
#Now, in our 2D array that is sent here, we go from position 0 to 3, for 3 lines.
            for loop1 in variable[outerloop*3:(outerloop+1)*3]:
                for loop2 in loop1[innerloop*3:(innerloop+1)*3]:
#Attempts to put all elements of box into string.
                    boxstring += loop2 + " "
#Splits the string into an array, and adds that to a 2D array.
            boxarray = boxstring.split(" ")
            boxtwoD.append(boxarray[0:9])
#Resets the variables.
            boxarray = []
            boxstring = ""
    boolcheck = validate(boxtwoD)
    return boolcheck

#allow the user to input a few lines of a sudoku.  If all the rows, boxes and columns are good, then return true, else return a false.

boolcheck = False
sudokuarray2D = []
for loop in range (0,9):
    sudokustring = input("")
    sudokuarray = []
    for loop2 in range(0,9):
        line = sudokustring[loop2:loop2+1]
        sudokuarray.append(line)
    sudokuarray2D.append(sudokuarray)
#start checking it's valid

columntrue = False
final = False
rowtrue = validate(sudokuarray2D)
if rowtrue == True:
    columntrue = column_converter(sudokuarray2D)
if columntrue == True:
    final = box_converter(sudokuarray2D)
if final == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
