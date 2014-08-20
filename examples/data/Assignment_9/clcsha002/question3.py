"""assignment 9 question 3
shannon clacey
13 may 2014"""

def check(variable): #this function checks if there is no duplicates in the array
    
    boolean = True #assume the line is correct or true

    for loop1 in variable:
        position = 0
        for loop2 in loop1:
            position += 1
            if (loop2 in loop1[position:]):
                return False #checks if the loop2 is found in loop1 before its current positin. If this happens, return false and in doing so terminate function 
                break
    return True

def column_converter(variable): #here the column is converted to a one dimensional array
    columnarray = []
    column2D = []
    for loop in range(0,9): #take position of each line of two dimensional array sent to function and add it to one dimensional array. All columns then sent to a 2 dimensional array which is sent to validate the function
        for loop2 in variable:
            columnarray.append(loop2[loop]) #add the line (loop2) in the position of loop which is the pos of the line to the array. This is then repeated for each line and added to a 2 dimensional column
        column2D.append(columnarray)        
        columnarray = []#resets the array for each column
    return check(column2D)

def box_converter(variable): #create function to add the values in the box to a string which can then be added to a 1 dimensional array and then into a two dimensional array for all the boxes   
    boolean = True   #assume true to start 
    
    boxarray = [] #assignment or initiation of variables
    boxstring = ""
    box2d = []    
    
    for outerloop in range(0,3):
        for innerloop in range(0,3):
            for loop1 in variable[outerloop*3:(outerloop+1)*3]: #in the two dimensional array, go from position 0 to three, repeated 3 times i.e. for three lines
                for loop2 in loop1[innerloop*3:(innerloop+1)*3]: #try put all elements of box in string
                    boxstring += loop2 + " "
            boxarray = boxstring.split(" ") #convert the string to an array which is then added to a 2 dimensional array
            box2d.append(boxarray[0:9])
            boxarray = [] #this resets the variables
            boxstring = ""
    
    boolean = check(box2d) 
    return boolean


boolean = False #with the functions being finished, user inputs some lines to the sudoku. If the input is correct return true, else return false
sudokuarray2D = []

for loop in range (0,9):
    sudokustring = input("")
    sudokuarray = []
    for loop2 in range(0,9):
        line = sudokustring[loop2:loop2+1]
        sudokuarray.append(line)
    sudokuarray2D.append(sudokuarray) #after being given the 2 dimensional array, it is possible to check whether or not it is valid.

columntrue = False
rowtrue = check(sudokuarray2D)
final = False

if columntrue == True:
    final = box_converter(sudokuarray2D)

if rowtrue == True:
    columntrue = column_converter(sudokuarray2D)

if final == True:
    print("Sudoku grid is valid")

else:
    print("Sudoku grid is not valid")
