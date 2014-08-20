""" a program that checks if a sudoku grid is valid 
nelisile mkhwebane
15 May 2014"""

""" creating a big grid for all the lines of numbers"""
big_grid=[]
""" creating a list to split the numbers in each line"""
array = []
""" we want the grid to append for all nine lines of numbers"""
for row in range (9):
    list_values = input()
    """take each number per row and store them as a list in the small array"""
    for col in range (9):
        array.append(list_values[col])
    """take in the small array into the big grid"""
    big_grid.append(array)
    array = []

""" a function that checks if values in the same line are not duplicated """
def horizontal_check(big_grid):
    for row in range(9):
        """we want to append each value in the row to a new string"""
        check_row= ""
        for col in range(9):
            if big_grid[row][col] not in check_row:
                check_row = check_row + big_grid[row][col]
                return True
            else:
                return False
#print(horizontal_check(big_grid))
    
""" a function that checks for duplicates vertically """ 
def vertical_check(big_grid):
    for row in range(9):
        '''an initial empty string to accumulate every character that hasn't been repeated'''
        check_col = ""
        winning=True #we assume the person hasn't lost yet
        for col in range(9):
            """if the number already exists in the initial string"""
            if str(big_grid[row][col]) in check_col: 
                winning = False #the person has lost already!
            else:
                check_col = check_col + str(big_grid[row][col]) # the number doesn't exist yet, so we add it to the string
    if winning: #the person won over all
        return True
    else:
        return False

""" a function that checks if theres's duplicates in internal 3X3 grid """
def check_small_grid(big_grid):
    winning = ""
    """dividing the grid into three"""
    for side in range (0,9,3):
        for down in range (0,9,3): #horizontal movement
            words =""
            for steps in range (side, side+3): #this checks for the three psn horizonally
                for step_down in range(down, down+3): #this checks for the three psn verticaally
                    if found.find(str(big_grid[steps][step_down]))>-1:
                        winning = "over"
                        break
                    else:
                        words +=str(big_grid[steps][step_down])    
            if lost.find("over") >-1:
                break #this breaks the loop immediately matching numbers are found, without having to go through all sub grids
    if winning == "":
        return True
    else:
        return False
""" printing out whether you lost or not"""
if vertical_check == True and horizontal_check == True and check_small_grid==True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
        
                        
        
        
    
    

