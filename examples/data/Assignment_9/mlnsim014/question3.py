'''Program to check if a soduku grid is valid or if it is not
Simangaliso Mlangeni
16 May 2014'''

grid = []

#create function
def check():
    '''Function to iterate through a soduku grid and check if it is valid'''
    #create new grid variable
    grid = []
    for i in range(9):#create 9x9 grid
        grid.append([0]*9)  
    for row in range(9):
        rowInput = input("")
        for u in range(9):
            grid[row][u] = rowInput[u]
            
    valid = True
    #Check rows to ensure validity
    for row in range(9):
        if CheckValid(grid[row]):
            continue
        else:
            valid = False
            print("Sudoku grid is not valid")
            break
    
    #Check each column to ensure validity    
    if valid:
        T = []
        for col in range(9):
            for row in range(9):
                T.append(grid[row][col])
            if CheckValid(T) and CheckValid(grid[row]):
                T = []
                continue
            else:
                valid = False
                print("Sudoku grid is not valid")   
                break
    
    #Check last part of the grid.(3x3)
    if valid:
        T = []
        for horizontal in [0,3,6]:
            for vertical in [0,3,6]:
                for row in range(3):
                    for col in range(3):
                        T.append(grid[row+horizontal][col+vertical])
                if CheckValid(T):
                    T = []
                    continue
                else:
                    valid = False
                    print("Sudoku grid is not valid") 
                    break
            if not valid:
                break
    if valid:#if grid is valid
        print("Sudoku grid is valid")    



def CheckValid(array):
    '''recursive function to go over items checking whether there is a value zero on the grid''' 
    if len(array) == 1:#base case
        return True
    if array[0] in array[1:]:
        return False
    else:
        return CheckValid(array[1:])
    
check()