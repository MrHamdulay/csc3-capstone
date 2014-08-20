"""program to check if a complete Sudoku grid is valid or not
Gary Finkelstein
14 May 2014"""

row = []
num = []

#Getting user input and adding it to 3D array
for i in range(9):
    line = input("")
    for number in line:
        row.append(number)
    num.append(row)
    row = []

valid = True

#Check horizontally across to see if number is the same as another
for i in range(9):
    tempary_variable = ""
    for j in range(9):
        if num[i][j] in tempary_variable:
            valid = False
            break
        tempary_variable = tempary_variable + num[i][j]        

#Checking vertically to see if number is same as another

    
#Checking each of the 9 3x3 grid
#starting with the top 3 rows (0,1,2)
tempory_value1 = ""
tempory_value2 = ""
tempory_value3 = ""

for i in range(3):
   
    for j in range(3):
        if num[i][j] in tempory_value1:
            valid = False
            break
        tempory_value1 = tempory_value1 + num[i][j]
   
    for j in range(3,6):
        if num[i][j] in tempory_value2:
            valid = False
            break
        tempory_value2 = tempory_value2 + num[i][j]   
    
    for j in range(6,9):
        if num[i][j] in tempory_value3:
            valid = False
            break
        tempory_value3 = tempory_value3 + num[i][j]

tempory_value4 = ""
tempory_value5 = ""
tempory_value6 = ""
for i in range(3,6):
    for j in range(3):
        if num[i][j] in tempory_value4:
            valid = False
            break
        tempory_value4 = tempory_value4 + num[i][j]
    for j in range(3,6):
        if num[i][j] in tempory_value5:
            valid = False
            break
        tempory_value5 = tempory_value5 + num[i][j]     
    for j in range(6,9):
        if num[i][j] in tempory_value6:
            valid = False
            break
        tempory_value6 = tempory_value6 + num[i][j]

tempory_value7 = ""
tempory_value8 = ""
tempory_value9 = ""
for i in range(6,9):
    for j in range(3):
        if num[i][j] in tempory_value7:
            valid = False
            break
        tempory_value7 = tempory_value7 + num[i][j]
    for j in range(3,6):
        if num[i][j] in tempory_value8:
            valid = False
            break
        tempory_value8 = tempory_value8 + num[i][j]     
    for j in range(6,9):
        if num[i][j] in tempory_value9:
            valid = False
            break
        tempory_value9 = tempory_value9 + num[i][j]

#printing if valid or not
if valid == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")