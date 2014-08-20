def check_soduku():
    #take the input of 9 lines and convert them into a 2D grid
    x = []
    for i in range (9):
        soduko = input()
        y=list(soduko)
        x.append(y)
        
    #loop over grid, checking that every number occurs only once in the "row"    
    for row in range(9):
        for col in range (9):
            if x[row].count(x[row][col])>1:
                return "Sudoku grid is not valid"
            
    #create a new 2D grid, which takes all the values in each "column" and converts them into one row (one list)
    column=[]
    for i in range(9):
        column.append([])
        for j in range(9):
            column[i].append(x[j][i])
            
    #loop over the grid, cheking that every number only occurs once the (new) row
    for row in range(9):
        for col in range(9):
            if column[row].count(column[row][col])>1:
                return "Sudoku grid is not valid"
        
    #create a 3x3 subgrid:
    three_by_three=[]
    for row in range(3):
        three=x[row]
        for col in range(3):
            three_by_three.append(three[col])
        
    #check that every number in the subgrid only occurs once
    for i in range(9):
        if three_by_three.count(three_by_three[i])>1:
            return "Sudoku grid is not valid"
            
    return "Sudoku grid is valid" 
print(check_soduku())





    