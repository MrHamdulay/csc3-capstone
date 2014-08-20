#Phumelele Ndimande

#variable
bfound = True #This will become false if there is even one error

#input part 
grid = []
grid_com = []
for i in range(9):
    nums = input()
    grid.append(nums)
#making a list of the items in grid


#processing part 
#function to check whether any matching stuff
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

#function to work in rows
def row_check(grid):
    for i in range(len(grid)):
        if check_equal(grid[i]) == True:
            return True
    return False
#function to create grid for columns

def col_check(grid):
    #ensuring the column swapping 
    grid_new = []
    grid_all = []
    for row in range(9):
        string = ""
        for col in range(9):
            string = string + str(grid[col][row]) + "\n"
        all_s = string.split("\n")
        all_s = all_s[:len(all_s)-1]
        grid_new.append(all_s[:len(all_s)])    
    #checking
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
   #checking whether or not they equal
   
    for i in range(len(grid_new)):
        if check_equal(grid_new[i]) == True:
            return True
    return False

def check_All(grid):
    if (row_check(grid) == False) and (col_check(grid) == False) and (check_cells(grid) == False):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
 
check_All(grid)
