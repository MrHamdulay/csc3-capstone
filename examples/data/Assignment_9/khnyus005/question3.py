'''
Created on 12 May 2014
Sudoku checker
@author: Yusuf Khan
KHNYUS005
'''
def check_rows(grid):#check rows
    for i in range(9):
        temp = []#to fill with numbers in row
        for c in range(9):#nested loop to loop through values
            temp.append(grid[i][c])#create list with values
        for t in range(1,10,1):#loop through ints 1-9 to check for repetition
            if temp.count(str(t))>1:#check for repetition
                return False#exit and return false if invalid
    return True#if false isn't triggered
            
def check_cols(grid):
    for c in range (9):
        temp = []
        for i in range(9):
            temp.append(grid[i][c])#create list with values
        for t in range(1,10,1):
            if temp.count(str(t))>1:#check for repetition
                return False#exit and return false if invalid      
    return True#if false isn't triggered
    
def check_subs(grid):#check mini 3*3 grids
    for c in range(0,7,3):
        for i in range(0,7,3):
            temp = []#inititiate out of loop
            for t in range (c, c+3, 1):
                for l in range(i,i+3,1):
                    temp.append(grid[t][l])#create list with values
            for t in range(1,10,1):
                if temp.count(str(t))>1:#check for repetition
                    return False#exit and return false if invalid
    return True#if false isn't triggered

grid = [[],[],[],[],[],[],[],[],[]]#hard coded 2D array

for i in range(9):#input sudoku grid in 2D array
    temp = input()
    for c in range(9):
        grid[i].append(temp[c])
        
valid = check_rows(grid)*check_cols(grid)*check_subs(grid)#True if all true, false if at least one false
if valid == True:
    print('Sudoku grid is valid')
else:#outputs
    print('Sudoku grid is not valid')                              