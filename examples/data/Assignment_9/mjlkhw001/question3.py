# Sudoku grid checker
# Khwezi Majola
# MJLKHW001
# 10 May 2014

def check():
    grid = [] #Empty grid for the values
    
    string = ''
    temp =  'word'
    
    for i in range(9):
        temp = input() #Take in values line by line
        temp.replace('\n', '')
        string += temp #Add them to the string
        
    #Format the input correctly
    for i in range(9):
        grid.append([]) #Make grid 2D by inserting an empty list
        if len(string) != 9:
            stemp = string[:9] #Extract the 9 characters
            string = string[9:] #Delete the extracted characters from the original input string
        else: stemp = string
        for j in range(9):
            grid[i].append(int(stemp[j])) #Insert the numbers into the 2D grid
    
    #Check if valid
    check = True #Create a check variable.
    
    #First test. No 2 cells in the same row have the same value
    if check == True: #Ensures check is true before attempting a validity test
        i = 0
        while (i < 9) and (check == True):
            check_list = [] #Reset check_list 
            for a in range(9): #Populate check_list with numbers 1-9
                check_list.append(a)                      
            for j in range(9):
                if (int(grid[i][j])-1) in check_list: #If the number is not in check_list it means it has come up before thus check is set to False
                    check_list[int(grid[i][j])-1] = -1                    
                else: 
                    check = False
                    break                    
            i += 1
            
    #Second test. No 2 cells in the same column have the same value
    if check == True: #Ensures check is true before attempting a validity test
        j = 0
        while (j < 9) and (check == True):
            check_list = [] #Reset check_list 
            for a in range(9): #Populate check_list with numbers 1-9
                check_list.append(a)              
            for i in range(9):
                if (int(grid[i][j])-1) in check_list: #If the number is not in check_list it means it has come up before thus check is set to False
                    check_list[int(grid[i][j])-1] = -1
                else: 
                    check = False
                    break
            j += 1    
    
    #Third test. #No 2 cells in the same 3x3 sub-grid have the same value
    if check == True: #Ensures check is true before attempting a validity test
        for p in range(3, 10, 3): #Loop variable referencing to the rows
            for k in range(3, 10, 3): #Loop variable referencing to the columns
                check_list = [] #Reset check_list 
                for a in range(9): #Populate check_list with numbers 1-9
                    check_list.append(a)
                i = p - 3 
                while (i < p) and (check == True): #The above statement coupled with while i < k ensures only three rows are checked
                    j = k - 3 
                    while (j < k) and (check == True): #The above statement coupled with while j < k ensures only three columns are checked thus creating a 9x9 grid
                        if (int(grid[i][j])-1) in check_list: #If the number is not in check_list it means it has come up before thus check is set to False
                            check_list[int(grid[i][j])-1] = -1
                        else: check = False #If the number is in the specific value in check_list is set to -1
                        j += 1
                    i += 1
                    
    if check == True:
        print('Sudoku grid is valid')
    else: print('Sudoku grid is not valid')

check()