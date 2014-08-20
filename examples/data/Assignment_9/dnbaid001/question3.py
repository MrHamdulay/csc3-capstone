#Assignment 9 - Question 3
#Checks validity of completed sudoku grid
#Aidan de Nobrega DNBAID001
#10/05/2014

grid = []

for i in range(9):
    numbers = input() #empty input prompt
    grid.append(numbers) #each row of 9 appended
    
valid = True #the puzzle is valid until a discrepency is located

#this set of loops checks rows
for i in range(9):
    for j in range(9):
        t = 1
        #j + t less than 9 to stay within confines of puzzle
        while j + t < 9 and valid == True: #2nd Boolean to speed up algorithm
            #if two numbers in row alike, puzzle not valid
            if grid[i][j] == grid[i][j+t]:
                valid = False   
            t += 1
            
#this set of loops checks columns
for i in range(9):
    for j in range(9):
        t = 1
        #see line 18
        while i + t < 9 and valid == True: #2nd Boolean to speed up algorithm
            #if two numbers in column alike, puzzle not valid
            if grid[i][j] == grid[i + t][j]:
                valid = False
            t += 1

#this set of loops checks 3x3 grids inside puzzle  
#uses top right corner of each 3x3 as reference to make separate list for checking
for i in range(0, 7, 3):
    for j in range(0, 7, 3):
        templst = [] #reset each time we check new 3x3
        for y in range(3):
            for x in range(3):
                #appends each number in 3x3 to templst if it's not already in templst
                if not grid[i + y][j + x] in templst:
                    templst.append(grid[i + y][j + x])
        #because of line 44, if there are not 9 numbers in templst, at least two numbers are alike and puzzle is invalid.
        if len(templst) < 9:
            valid = False
            
if valid == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
        
            