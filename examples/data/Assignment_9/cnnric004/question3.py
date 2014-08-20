"""Ricky Conn
CNNRIC004
Checks if an input sudoku grid is valid"""

#the grid is by default valid and if it does not pass won of the checks it is set to invalid
valid = True
columnA = []
row = []
for count in range(9):
    #User inputs the next line
    line = input("")
    #Cycles through each number in line and appends it to an array
    for num in line:
        row.append(num)
    #appends the array of numbers to new array to form a 2 dimentional array
    columnA.append(row)
    row = []

columnB = []
columnC = []
columnD = []

#breaks the 9*9 array up into a 2 dimentional array with 3 numbers in each array
#this is used to check if numbers in the 3*3 non overlapping blocks of the array are not repeating
for count in range(3):
    for count2 in range(3):
        for row in range(3):
            for column in range(3):
                columnB.append(columnA[row+3*count][column+3*count2])
            columnC.append(columnB)
            columnB=[]

for p in range(3):
    #Slips the 9*9 2 dimentional array into 9 3*3 2 dimentional arrays  
    columnD.append(columnC[0+3*p])
    columnD.append(columnC[1+3*p])
    columnD.append(columnC[2+3*p])
    for i in range(column,len(columnD[0])):
        for row in range(3):
            for column in range(3):
                #checkes if there are any repeating numbers in the 3*3 2 dimentional array
                #if so than the grid is invalid
                if((columnD[p][i] == columnD[row][column])and(i != column)):
                    valid = False
                    
    #for column in range(3):
        #for row in range(3):
            #for i in range(column,len(columnD[0])):
                #if((columnD[i][column] == columnD[row][column])and(i != row)):
                    #valid = False
                    #print("F")
    columnD = []
    

#checks if every horizontal row is has no repeating number and if it does it is invalid
for row in range(len(columnA[0])):
    for column in range(len(columnA)):
        for i in range(column,len(columnA)):
            if((columnA[row][i] == columnA[row][column])and(i != column)):
                valid = False
                
#checks if every horizontal column is has no repeating number and if it does it is invalid                
for column in range(len(columnA[0])):
    for row in range(len(columnA)):
        for i in range(column,len(columnA)):
            if((columnA[i][column] == columnA[row][column])and(i != row)):
                valid = False
      
#If the grid has not failed any of the tests it is valid otherwise it is invalid         
if(valid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
