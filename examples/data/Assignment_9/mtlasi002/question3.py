#Asil Motala
#MTLASI002
#Assignment 9
#Question 3
#09 May 2014

sudoku=[]                                                           #initialize empty list
for i in range(9):                                                  #create 9 rows
    i=input("")                                                     #get 9 rows of input from user
    row=[]                                                          #intialize empty row variable
    for j in range(9):                                              #create 9 columns
        row.append(i[j])                                            #add data to each column in the row
    sudoku.append(row)                                              #add the list to sudoku list

def check_1(sudoku):                                                #checks if more than one of same number in the same row
    for row in range(9):                                            #loops through each row
        for check_1 in range(1,10):                                 #loops through each sudoku number
            if sudoku[row].count(str(check_1))>1:                   #checks if any sudoku number appears more than once
                return False                                        #returns sudoku grid is not valid
    else: return True                                               #returns sudoku grid may be valid

def check_2(sudoku):                                                #checks if more than one of same number in column
    for column in range(9):                                         #loops through each column
        for row in range(8):                                        #loops through each row
            for check_2 in range(row+1,9):                          #loops through row below row
                if sudoku[row][column]==sudoku[check_2][column]:    #check if any of same number in column
                    return False                                    #returns sudoku grid is not valid
    else: return True                                               #returns sudoku grid may be valid

def check_3(sudoku):                                                #checks if any of the same number within smaller grid
    for grids_1 in range(3):                                        #loops through each horizontal grid of 3x3
        for grids_2 in range(3):                                    #loops through each vertical grid of 3x3
            grid=[]                                                 #intialize empty list for each grid
            for row in range((3*grids_1),(3*(grids_1+1))):          #loop through each row in each grid
                for column in range((3*grids_2),(3*(grids_2+1))):   #loop through each column in each grid
                    grid.append(sudoku[row][column])                #add all data from each grid to a list
            for number in range(1,10):                              #loop through sudoku numbers
                if grid.count(str(number))>1:                       #check if each sudoku number appears more than once
                    return False                                    #returns sudoku grid is not valid
    else: return True                                               #returns sudoku grid may be valid

if check_1(sudoku) and check_2(sudoku) and check_3(sudoku):         #checks if all three conditions are valid
    print("Sudoku grid is valid")                                   #prints that sudoku grid is valid
else:                                                               #if any of the one condition fails
    print("Sudoku grid is not valid")                               #prints that sudoku grid is not valid