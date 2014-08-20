# Question 3 - Assignment 9
# Oliver Harrison
# 14 May 2014
# Program to check Sodoku grid


# get input and make grid
global grid
grid = []

#newline = input()        #########
for i in range(9):
    grid.append([])
    newline = input()
    for j in range(9):
        grid[i].append(newline[j:j+1])
    

# create fuctions for each condition

# 1 - Check row


def check_row():
    check_grid = []
    for i in range(9):
        check_grid.append([])
        for j in range(9):
            #print(grid[i][j])  
            #print(check_grid)
            if grid[i][j] in check_grid[i]:
                return False
            else:
                check_grid[i].append(grid[i][j])
    return True



# 2 - check column

def check_col():
    check_grid = []
    for i in range(9):
        check_grid.append([])
        for j in range(9):
            if grid[j][i] in check_grid[i]:
                return False
            else:
                check_grid[i].append(grid[j][i])
    return True

# - check 3x3 grid 

def check_3x3():
    for i in (1, 4, 7):
        for j in (1, 4,7):
             for k in (-1, 1):
                 if grid[i][j] != grid[i+k][j] and grid[i][j] != grid[i][j+k] and grid[i][j] != grid[i-k][j+k] and grid[i][j] != grid[i+k][j-k]:
                     continue
                 else:
                    return False
    return True 



def main():
    check_row()
    check_col()
    check_3x3()
    if check_row() == True and check_col() == True and check_3x3() == True:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
        
main()


            