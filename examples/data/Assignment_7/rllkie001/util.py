#Kieran Reilly, RLLKIE001
#Utility Functions
#Assignment 7, Question 2
#01/05/14

height = 4

def create_grid(grid):
    for i in range(height):
        grid.append([0]*4)
        
def print_grid(grid):
    out = "{" ":<5}"

    print("+--------------------+")
    for row in range(height):
        tempString = ""
        for col in range(height):
            newColumn = grid[row][col]
            newColumn = str(newColumn)
            if newColumn == "0":
                newColumn = newColumn.replace("0", " ")
            newColumn = out.format(newColumn)
            #grid[row][col] = newColumn
            tempString = tempString + newColumn #grid[row][col]
        #tempString = tempString.replace("0", " ")
        print("|"+tempString+"|")
                    
    print("+--------------------+")
    
    
def check_lost(grid):
    gameLost = False
    adjacentValues = True
    countNonZeros = 0
    
    for row in range(height):
        for col in range(height):
            if grid[row][col] != 0:
                countNonZeros += 1
    
    for row in range(height):
        for col in range(height):
            if row == 0:
                if grid[row][col] != grid[row+1][col]:
                    adjacentValues = False
            elif row == 3:
                if grid[row][col] != grid[row-1][col]:
                    adjacentValues = False
            elif col == 0:
                if grid[row][col] != grid[row][col+1]:
                    adjacentValues = False
            elif col == 3:
                if grid[row][col] != grid[row][col-1]:
                    adjacentValues = False
            elif (row != 0 and col != 0) or ( row != 3 and col != 3):
                if grid[row][col] != grid[row+1][col]:
                    adjacentValues = False
                elif grid[row][col] != grid[row-1][col]:
                    adjacentValues = False
                elif grid[row][col] != grid[row][col+1]:
                    adjacentValues = False
                elif grid[row][col] != grid[row][col-1]:
                    adjacentVAlues = False
                    
    if countNonZeros == 16 and adjacentValues == False:
        return True
    else:
        return False
    
    
def check_won(grid):
    highestValue = grid[0][0]
    for row in range(height):
        for col in range(height):
            if highestValue <= grid[row][col]:
                highestValue = grid[row][col]
    
    if highestValue >= 32:
        return True
    

'''    grid = [[1,2,3,4],[4,3,2,5],[6,7,9,1],[2,5,10,2]]
    create_grid(grid)
    print_grid(grid)
    check_lost(grid)
    check_won(grid)'''