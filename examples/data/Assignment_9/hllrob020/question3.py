#Sudoku grid checker
#Robin Hall
#16/05/2014

grid = []

for i in range(9):
        num_grid = input()
        grid.append(num_grid) #creates 9x9 grid from user's input
        
grid_valid = True #grid is acceptable until an error is located

#loops here check each row of the appended grid
for a in range(9): 
        for b in range(9):
                x = 1
                while b + x < 9 and grid_valid == True: #b + x must be less than 9 to stay within grid parameters
                        if grid[a][b] == grid[a][b + x]: 
                                grid_valid = False #makes boolean for grid false if two numbers in a row are the same
                        x += 1
                        
#loops here check each column of the appended grid                      
for a in range(9):
        for b in range(9):
                x = 1
                while a + x < 9 and grid_valid == True: #same constraints as for rows
                        if grid[a][b] == grid[a + x][b]:
                                grid_valid = False #makes boolean for grid false if two numbers in a column are the same
                        x += 1
#loops here check each 3x3 set of numbers in appended grid
for a in range(0,7,3):
        for b in range(0,7,3):
                small_grid = [] #will make a new list for each new 3x3 grid being checked
                for x in range(3):
                        for y in range(3):
                                if grid[a + x][b + y] not in small_grid:
                                        small_grid.append(grid[a + x][b + y])
                                        #adds each number to small_grid if it's not already there. This means that if the number of values in the small grid is less than 9, then there was a duplicate of a number.
                if len(small_grid) < 9:
                        grid_valid = False #if duplicate indicated, makes boolean for grid false
                        
if grid_valid == True:
        print('Sudoku grid is valid')
else:
        print('Sudoku grid is not valid')
        