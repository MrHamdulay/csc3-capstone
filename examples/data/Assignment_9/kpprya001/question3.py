"""Ryan Kopping 13 May
program to find a valid sudoku grid"""
grid = []
isDuplicate = False
square1=""
square2=""
square3=""
square4=""
square5=""
square6=""
square7=""
square8=""
square9=""
#get the input for the soduko grid
grid.append(input())
grid.append(input())
grid.append(input())
grid.append(input())
grid.append(input())
grid.append(input())
grid.append(input())
grid.append(input())
grid.append(input())

#create and populate a 2d array
gridNumbers = [[0 for i in range(9)] for i in range(9)]
#put the input values into the 2d array
for i in range(0,len(grid)):
    count=1
    for j in range(len(grid[i])):
        gridNumbers[i][j]=grid[i][j:count]
        count+=1
    
    
#check the first 3 '3x3' blocks for any duplicates       
for i in range(3):
    for j in range(3):
        if(gridNumbers[i][j] in square1):
            isDuplicate=True
            break
        square1+=gridNumbers[i][j]
        
    for j in range(3,6):
        if(gridNumbers[i][j] in square2):
            isDuplicate=True
            break
        square2+=gridNumbers[i][j]
    for j in range(6,9):   
        if(gridNumbers[i][j] in square3):
            isDuplicate=True
            break
        square3+=gridNumbers[i][j]
            
#check the second 3 '3x3' blocks for any duplicates             
for i in range(3,6):
    for j in range(3):
        if(gridNumbers[i][j] in square4):
            isDuplicate=True
            break
        square4+=gridNumbers[i][j]
        
    for j in range(3,6):
        if(gridNumbers[i][j] in square5):
            isDuplicate=True
            break
        square5+=gridNumbers[i][j]
    for j in range(6,9):   
        if(gridNumbers[i][j] in square6):
            isDuplicate=True
            break
        square6+=gridNumbers[i][j]
            
#check the last 3 '3x3' blocks for any duplicates             
for i in range(6,9):
    for j in range(3):
        if(gridNumbers[i][j] in square7):
            isDuplicate=True
            break
        square7+=gridNumbers[i][j]
        
    for j in range(3,6):
        if(gridNumbers[i][j] in square8):
            isDuplicate=True
            break
        square8+=gridNumbers[i][j]
    for j in range(6,9):   
        if(gridNumbers[i][j] in square9):
            isDuplicate=True
            break
        square9+=gridNumbers[i][j]    

#check each row for duplicates
for i in range (9):
    duplicateHorizontal=""
    for j in range(9):
        #check if current number is anywhere in the row
        if(gridNumbers[i][j] in duplicateHorizontal):
            isDuplicate=True
            break
        duplicateHorizontal+=gridNumbers[i][j]
        
        
#heck each column for duplicates        
for i in range (9):
    duplicateVertical=""
    for j in range(9):
        #check if current number is anywhere in the column
        if(gridNumbers[i][j] in duplicateVertical):
            isDuplicate=True
            break
        duplicateVertical+=gridNumbers[i][j]
        


    
#print the conditional statemnt        
if(isDuplicate):
    print("Sudoku grid is not valid")
else:
    print('Sudoku grid is valid')
    
    