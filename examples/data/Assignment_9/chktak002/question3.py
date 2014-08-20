#takunda chikondo
# a programme to check wheter a sodoku grid is valid or not
value = True
new_array = []
grid = []
tempgrid = []
#Creating the 2D array
for i in range (9):
    
    grid.append ([""] * 9)     

#Writing the grid the 2d array(grid)
for y in range(9):
    num  = input()
    for i in range(9):        
        grid[y][i] = num[i]

#Checking Columns for repeated values
for y in range (9):
    tempgrid=[]
    for x in range (9):
        tempgrid.append(grid[y][x])
    tempgrid.sort() # sorts all the appended values in the list
    
    for x in range (8):
        if tempgrid[x]==tempgrid[x+1]:# comapres the sorted adjacent values and if a value is repeated in the column the grid cannot be valid
            value = False
            
#Checking Rows for repeated values
for y in range (9):
    tempgrid=[]
    for x in range (9):
        tempgrid.append(grid[x][y])
    tempgrid.sort() #sorts all the appended values in the list
             
    for x in range (8):
        if tempgrid[x]==tempgrid[x+1]:# comapres the sorted values adjacent values and if a value is repeated in the row the grid cannot be valid
            value = False

#Checking 3x3 Grids are valid
for h in range(0,3,6):

    for k in range(0,3,6): #checks if the smaller 3x3 grid is valid
        
        
        for y in range(3): 
            
            for i in range (3):        
                new_array.append (grid[y][i+k])
        new_array.sort()   #Adds all the values to a single array

        for x in range (8):
            if new_array[x]==new_array[x+1]:
                value = False
        new_array =[]
        
if value == False:
    print("Sudoku grid is not valid")
if value ==True:
    print("Sudoku grid is valid")
