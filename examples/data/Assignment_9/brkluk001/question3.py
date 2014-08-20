grid = []

for i in range(9):
    grid.append([])
    numbers=input()
    for j in numbers:
        grid[i].append(j)

def check_valid(grid):
    
    for i in range(9):
        characters =""
        
        for j in range(9):
            
            
            if str(grid[i][j]) in characters: 
                return False
            else: 
                characters+= str(grid[i][j])
                
                
    for i in range(9):
        characters =""
                        
        for j in range(9):
                            
                            
            if str(grid[j][i]) in characters: 
                return False
            else: 
                characters+= str(grid[j][i])        
                
                
    for i in range(0,9,3):
        characters =""
        for t in range(3):
            for j in range(3):
                if str(grid[i+t][j]) in characters:
                    return False
                else: 
                    characters +=str(grid[i+t][j])
                    
                    
                            
    for i in range(0,9,3):
        characters =""
        for t in range(3):
            for j in range(3,6):
                if str(grid[i+t][j]) in characters:
                    return False
                else: 
                    characters +=str(grid[i+t][j])
                    
                    
                                     
    for i in range(0,9,3):
        characters =""
        for t in range(3):
            for j in range(6,9):
                if str(grid[i+t][j]) in characters:
                    return False
                else: 
                    characters +=str(grid[i+t][j])
    return True

if check_valid(grid):
    print('Sudoku grid is valid')
    
else:
    print('Sudoku grid is not valid')
        

    
