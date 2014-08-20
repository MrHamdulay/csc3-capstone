def push_up(grid):
    
    #To find zeros and pull numbers to the top of the column
    def find_zeros(grid):
    
        for counting in range(4):
            
            for i in range(4):
                
                for j in range(3):
                    if grid[j][i] == 0:
                        grid[j][i] = grid[j+1][i]
                        grid[j+1][i] = 0
                        
                    else:
                        continue
                    
        return grid
    
    #Creates the list with numbers at top of column
    find_zeros(grid)
    
    #Uses the new list to add adjacent like numbers in a column. Starts at top. Multiplies first occurance by 2 and the second occurance becomes 0.
    for n in range(4):
        
        for m in range(3):
            
            if grid[m][n] == grid [m+1][n]:
                grid[m][n] *= 2
                grid[m+1][n] = 0
            
            else:
                continue
    #Uses the added list to eliminate zeros and to bring all numbers to the top of the column. 
    find_zeros(grid)
    
    return(grid)


                    
def push_down(grid):
    
    #Finds zeros creates a new list with all numbers at the bottom of the column.
    def find_zeros(grid):
    
        for counting in range(4):
                    
                    for i in range(4):
                        
                        for j in range(3,0,-1):
                            if grid[j][i] == 0:
                                grid[j][i] = grid[j-1][i]
                                grid[j-1][i] = 0
                                
                            else:
                                continue
    
        return grid
    
    #Calls the function to make the new list.
    find_zeros(grid)
    
    #Uses the new list to add like adjacent numbers in a column. Starting from the bottom. First occurance is multiplied by 2, second occurance becomes 0.
    for n in range(4):
            
            for m in range(3,0,-1):
                
                if grid[m][n] == grid [m-1][n]:
                    grid[m][n] *= 2
                    grid[m-1][n] = 0
                
                else:
                    continue    
    
    #Uses the updated list with added numbers to eliminate zeros in between numbers and bring all numbers to the bottom of the column.            
    find_zeros(grid)
    
    return grid


def push_left(grid):
    
    #Finds zeros and brings numbers to left of the row, eliminating zeros.
    def find_zeros(grid):
        
            for counting in range(4):
                
                for i in range(4):
                    
                    for j in range(3):
                        if grid[i][j] == 0:
                            grid[i][j] = grid[i][j+1]
                            grid[i][j+1] = 0
                            
                        else:
                            continue  
            
            return grid
        
    #Calls the function to bring numbers to the left.    
    find_zeros(grid)
    
    #Adds adjacent and like numbers in a row. Starts from left. First occurance is multiplied by 2, second occurance becomes 0.
    for n in range(4):
                
                for m in range(3):
                    
                    if grid[n][m] == grid [n][m+1]:
                        grid[n][m] *= 2
                        grid[n][m+1] = 0
                    
                    else:
                        continue
    
    #Uses the updated list to eliminate zeros.                
    find_zeros(grid)
    
    return grid 

def push_right(grid):
    
    #Finds zeros and brings numbers to the right of the row.
    def find_zeros(grid):
            
                for counting in range(4):
                    
                    for i in range(4):
                        
                        for j in range(3,0,-1):
                            if grid[i][j] == 0:
                                grid[i][j] = grid[i][j-1]
                                grid[i][j-1] = 0
                                
                            else:
                                continue
                            
                return grid
    
    #Calls the function to bring numbers to the right of the row.        
    find_zeros(grid)
    
    #Adds adjacent like numbers in a row. Starts from the right. Multiplies first occurance by 2, makes second occurance 0.
    for n in range(4):
                    
                    for m in range(3,0,-1):
                        
                        if grid[n][m] == grid [n][m-1]:
                            grid[n][m] *= 2
                            grid[n][m-1] = 0
                        
                        else:
                            continue 
                        
    #Uses the updated list with added like adjacent numbers to find zeros and bring numbers to the right of the row.
    find_zeros(grid)
    
    return grid 