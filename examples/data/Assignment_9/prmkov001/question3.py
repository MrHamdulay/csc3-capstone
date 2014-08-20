#Kovlin Perumal
#PRMKOV001
#13/05/2014
#Sudoku Checking Program

grid = [] # Initialise empty array to be populated with more arrays
valid = True # Initially grid is valid

for i in range(9) : #For each line entered into the sudoku grid populate a new array into the empty grid array forming a 2D array containing the whole puzzle 
    line = []
    sudoku = input()
    for i in sudoku:
        line.append(int(i))
    grid.append(line)

for i in range(9) : #Check each row by putting each value in the row into an array and then checking if the next value is already in the array
    takenRow = [] 
    
    for j in range(9) :
        
        if  grid[i][j] in takenRow :
            valid = False #If value repeated sudoku grid isnt valid
        else :
            takenRow.append(grid[i][j])
            

for j in range(9):  #Check each column by putting each value in the row into an array and then checking if the next value is already in the array
    takenColumn = []
    for i in range(9):
        if  grid[i][j] in takenColumn :
            valid = False 
        else :
            takenColumn.append(grid[i][j])       
                    
for k in range (0,9,3) : #Use two for loops for i and j to make sure next for loops iterate over the 9x9 grids
    for x in range(0, 9, 3):
        taken = []
        for i in range (k, k + 3) : #for each mini 9x9 grid check if a value is repeated using the method used above
            
            
            for j in range (x, x + 3) :
                
                if  grid[i][j] in taken :
                    valid = False 
                else :
                    taken.append(grid[i][j])            

if valid == False : #Output whether sudoku grid is valid or not
    print("Sudoku grid is not valid")
else :
    print("Sudoku grid is valid")