#Kiuran Naidoo
#Assignment 9
#Question 3

inputs =[] #Get Input
for i in range(9):
    inputs.append(input(""))

 #Create two dimensional grid
grid =[] 
for i in range(9):
    grid.append([])
    for j in range(9):
        grid[i].append(inputs[i][j])

current =[]  #Create a variable to hold the current row/box/row being analysed 
valid = True #Variable that keeps track if grid is valid or not

#Check rows to see if they are valid
for i in range(9):
    current = grid[i]
    if len(set(current)) < 9:
        valid = False
        break

#Check columns to see if they are valid
if valid == True:
    for i in range(9):
        current =[]
        for j in range(9):
            current.append(grid[j][i]) #Making a list out of each column
        if len(set(current)) < 9:
            valid = False
            break
        if valid == False:
            break
  
startRow = 0 #Start row of boxes being analysed
startColumn = 0 #Start column of boxes being analysed

#Checking boxes to see if valid
if valid == True:
    for boxRows in range(3):
        for boxColumns in range(3):
            current =[]
            for rows in range(3): 
                for columns in range(3):
                    current.append(grid[startRow+rows][startColumn+columns])
            if len(set(current)) < 9:
                valid = False
                break
            startColumn +=3 #Move to next box right
        if valid == False:
            break
        
        startRow+=3 #Move to boxes below
        startColumn = 0 #Start from left box again
    
 #Print output
if valid == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
 

    


 
