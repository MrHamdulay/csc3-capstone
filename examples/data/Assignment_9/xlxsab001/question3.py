"""Sodoku checker
James Cushway
19=-05-2014"""
temp_arr = []
for i in range(9):
    numbers = input() #Until end of input
    temp_arr.append(numbers) #Assigning each row of numbers to a temporary array
    
    
grid = [[0 for i in range(9)] for i in range(9)] #Creating 9x9 array
for i in range(9):
    a = temp_arr[i]
    for j in range(9):
        grid[i][j] = eval(a[j]) #Populating array with values from the temporary array
        
correct = True

for i in range(9):
    for j in range(9):
        for k in range(9):
            if grid[i][j] == grid[i][k] and j != k:
                correct = False
             
if correct == True:
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if grid[j][i] == grid[k][i] and j!=k:
                    correct = False   

if correct == True:
    for i in range(1,8,3):
        for j in range(1,8,3):
            if grid[i][j] == grid[i-1][j-1] or grid[i][j] == grid[i+1][j+1] or grid[i][j] == grid[i+1][j-1] or grid[i][j] == grid[i-1][j+1] or grid[i+1][j] == grid[i][j+1]:
                correct = False
                
if correct == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
