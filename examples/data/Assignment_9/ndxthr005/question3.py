"""thrianka naidoo
ndxthr005
assignment 9, question 3: check if sudoku grid is valid"""

grid = []               #create grid (array)
for i in range(9):      
    values = input("")  #allow for user input
    word = []
    for s in range(len(values)):
        word.append(values[s])
    grid.append(word)   #create 2d array

flag_next = True        #declare flag for output
for i in range(len(grid)):  
    for s in range(len(grid[i])-1):
        if grid[i][s+1] == grid[i][s]:  #checks values next to each other
            flag_next = False
            
flag_down = True        #declare 2nd flag for output

for i in range(len(grid)-1):
    for s in range(len(grid[i])):
        if grid[i+1][s] == grid[i][s]:  #checks values below each other
            flag_down = False
            
if flag_next == False or flag_down == False:    #checks flags and outputs
    print("Sudoku grid is not invalid")
    
else:
    print("Sudoku grid is valid")
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
       