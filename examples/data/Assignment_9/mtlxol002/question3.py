"""CSC1015F Assignment 9 Question 3
Xola Matlanyane MTLXOL002
20 May 2014"""

temparr = []   #create list as a "temporary array"
for i in range(9):
    numbers = input() #goes until the end of the inpiut
    temparr.append(numbers) #putting each row in a temporary array
    
    
grid = [[0 for i in range(9)] for i in range(9)] #in order to create a 9x9 grid
for i in range(9):
    a = temparr[i]
    for j in range(9):
        grid[i][j] = eval(a[j]) #"increase" array with values from the temporary array
        
corr = True   #if correct

for i in range(9):
    for j in range(9):
        for k in range(9):
            if grid[i][j] == grid[i][k] and j != k:
                corr = False    #if "corr" is false
             
if corr == True:
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if grid[j][i] == grid[k][i] and j!=k:
                    corr = False   

if corr == True:
    for i in range(1,8,3):
        for j in range(1,8,3):
            if grid[i][j] == grid[i-1][j-1] or grid[i][j] == grid[i+1][j+1] or grid[i][j] == grid[i+1][j-1] or grid[i][j] == grid[i-1][j+1] or grid[i+1][j] == grid[i][j+1]:
                corr = False
                
if corr == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")



# PS: again, i've received much help with this. i actually do not know much about what is going on. i don't know what i'm going to do in the exam (if i even get there). oh well. c'est la vie.
