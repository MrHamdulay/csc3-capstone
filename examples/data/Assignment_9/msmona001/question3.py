"""Write a program to check if a complete Sudoku grid is valid or not.
Onalerona Mosimege
13 May 2014"""

#True if no error exists
bTrue = True 

###input values 
grid = []
grid_com = []
for i in range(9):
    nums = input()
    grid.append(nums)


#if equal cells:
def check_equal(line):  
    count = 0
    for i in line:
        for j in line:
            if i == j:
                count = count + 1
    if count > 9:
        return True
    else:
        return False

#Check if rows have no error
def row_check(grid):
    for i in range(len(grid)):
        if check_equal(grid[i]) == True:
            return True
    return False

#Check if columns have no error
def col_check(grid):
    grid_new = []
    grid_all = []
    for row in range(9):
        string = ""
        for col in range(9):
            string = string + str(grid[col][row]) + "\n"
        all_s = string.split("\n")
        all_s = all_s[:len(all_s)-1]
        grid_new.append(all_s[:len(all_s)])    
    
    for i in range(len(grid_new)):
        if check_equal(grid_new[i]) == True:
            return True
    return False
        
def rows_(grid):  
    string = ""
    grid_now= []   
    for row in range(3):
        for col in range(3):
            string = string + "\n" + str(grid[row][col])
            if len(string[1:len(string)].split("\n")) == 9:
                string = string[1:len(string)].split("\n")
                grid_now.append(string)
                string = ""
    for row in range(3):
        for col in range(3,6):
            string = string + "\n" + str(grid[row][col])
            if len(string[1:len(string)].split("\n")) == 9:
                string = string[1:len(string)].split("\n")
                grid_now.append(string)
                string = ""
    for row in range(3):
        for col in range(6,9):
            string = string + "\n" + str(grid[row][col])
            if len(string[1:len(string)].split("\n")) == 9:
                string = string[1:len(string)].split("\n")
                grid_now.append(string)
                string = ""    
    for row in range(3,6):
        for col in range(3):
            string = string + "\n" + str(grid[row][col])
            if len(string[1:len(string)].split("\n")) == 9:
                string = string[1:len(string)].split("\n")
                grid_now.append(string)
                string = ""
    for row in range(3,6):
        for col in range(3,6):
            string = string + "\n" + str(grid[row][col])
            if len(string[1:len(string)].split("\n")) == 9:
                string = string[1:len(string)].split("\n")
                grid_now.append(string)
                string = ""
    for row in range(3,6):
        for col in range(6,9):
            string = string + "\n" + str(grid[row][col])
            if len(string[1:len(string)].split("\n")) == 9:
                string = string[1:len(string)].split("\n")
                grid_now.append(string)
                string = "" 
    for row in range(6,9):
        for col in range(3):
            string = string + "\n" + str(grid[row][col])
            if len(string[1:len(string)].split("\n")) == 9:
                string = string[1:len(string)].split("\n")
                grid_now.append(string)
                string = ""
    for row in range(6,9):
        for col in range(3,6):
            string = string + "\n" + str(grid[row][col])
            if len(string[1:len(string)].split("\n")) == 9:
                string = string[1:len(string)].split("\n")
                grid_now.append(string)
                string = ""
    for row in range(6,9):
        for col in range(6,9):
            string = string + "\n" + str(grid[row][col])
            if len(string[1:len(string)].split("\n")) == 9:
                string = string[1:len(string)].split("\n")
                grid_now.append(string)
                string = ""    
              
    return grid_now
 
#function to check if cells are equal
def check_equal(line):  
    count = 0
    for i in line:
        for j in line:
            if i == j:
                count = count + 1
    if count > 9:
        return True
    else:
        return False  
 
def check_cells(grid):
    grid_new = rows_(grid)
   #checking if the 3X3 cells have no error
   
    for i in range(len(grid_new)):
        if check_equal(grid_new[i]) == True:
            return True
    return False

#Checking if all other checks are true, thus display appropriate output
def check_All(grid):
    if (row_check(grid) == False) and (col_check(grid) == False) and (check_cells(grid) == False):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
 
check_All(grid)
