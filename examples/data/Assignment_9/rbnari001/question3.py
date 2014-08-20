#Ariel Rubin
#RBNARI001
#program that checks if a soduku puzzle is valid/invalid
#15 May 2014

row = []
num = []

#taking input from the user and adding it to a 3D array
for i in range(9):
    line = input("")
    for number in line:
        row.append(number)
    num.append(row)
    row = []

valid = True

#horizontal check for a duplicated number
for i in range(9):
    tempary_variable = ""
    for j in range(9):
        if num[i][j] in tempary_variable:
            valid = False
            break
        tempary_variable = tempary_variable + num[i][j]        

#vertical check for a duplicated number
for i in range(9):
    tempary_variable = ""
    for j in range(9):
        if num[j][i] in tempary_variable:
            valid = False
            break
        tempary_variable = tempary_variable + num[j][i]
    
#Checks the 3x3 grid 9 times
#===========================

#starts with top 3 rows(0,1,2)
tempory_value1 = ""
tempory_value2 = ""
tempory_value3 = ""

for i in range(3):
    #1st 3x3 grid
    for j in range(3):
        if num[i][j] in tempory_value1:
            valid = False
            break
        tempory_value1 = tempory_value1 + num[i][j]
    #2nd 3x3 grid
    for j in range(3,6):
        if num[i][j] in tempory_value2:
            valid = False
            break
        tempory_value2 = tempory_value2 + num[i][j]   
    #3rd 3x3 grid
    for j in range(6,9):
        if num[i][j] in tempory_value3:
            valid = False
            break
        tempory_value3 = tempory_value3 + num[i][j]

#2nd set of 3 rows (3,4,5)
tempory_value4 = ""
tempory_value5 = ""
tempory_value6 = ""
for i in range(3,6):
    #1st 3x3 grid
    for j in range(3):
        if num[i][j] in tempory_value4:
            valid = False
            break
        tempory_value4 = tempory_value4 + num[i][j]
        #2nd 3x3 grid
    for j in range(3,6):
        if num[i][j] in tempory_value5:
            valid = False
            break
        tempory_value5 = tempory_value5 + num[i][j] 
        #3rd 3x3 grid
    for j in range(6,9):
        if num[i][j] in tempory_value6:
            valid = False
            break
        tempory_value6 = tempory_value6 + num[i][j]

#3rd set of 3 rows (6,7,8)
tempory_value7 = ""
tempory_value8 = ""
tempory_value9 = ""
for i in range(6,9):
    #1st 3x3 grid
    for j in range(3):
        if num[i][j] in tempory_value7:
            valid = False
            break
        tempory_value7 = tempory_value7 + num[i][j]
        #2nd 3x3 grid
    for j in range(3,6):
        if num[i][j] in tempory_value8:
            valid = False
            break
        tempory_value8 = tempory_value8 + num[i][j]  
        #3rd 3x3 grid
    for j in range(6,9):
        if num[i][j] in tempory_value9:
            valid = False
            break
        tempory_value9 = tempory_value9 + num[i][j]
#prints a message to say whether the grid is valid/invalid
if valid == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")