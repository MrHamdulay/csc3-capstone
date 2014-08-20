#assignment 9 Q3 - sudoku grid checker
#Kavir Ranchod RNCKAV001
#14/04/2014

def row_checker(List): 
    #check each horizontal line in the grid
    horizontal=[]
    for i in range(len(List)): 
        for j in range(len(List[i])): 
            if List[i][j] in horizontal:
                return False
            else: 
                horizontal.append(List[i][j]) 
        horizontal = [] 
    return True

def column_checker(List): 
    #check each vertical line in the grid
    vertical = [] 
    for i in range(9): 
        for j in range(9): 
            if List[j][i] in vertical: 
                return False
            else: 
                vertical.append(List[j][i]) 
        vertical = [] 
    return True

def block_checker(List): 
    #Check each 3x3 block in the grid
    vertcount=0
    horicount=0
    for line1 in range(3): 
        grid=[] 
        for i in range(vertcount,vertcount+3):
            for j in range(horicount,horicount+3): 
                if List[i][j] in grid: 
                    return False
                else: 
                    grid.append(List[i][j]) 
        vertcount += 3
        grid=[] 
    horicount=3
    vertcount=0
    for line2 in range(3): 
        grid=[] 
        for i in range(vertcount,vertcount+3): 
            for j in range(horicount,horicount+3): 
                if List[i][j] in grid: 
                    return False
                else:     
                    grid.append(List[i][j])                 
        vertcount += 3
        grid=[] 
    vertcount=0    
    horicount=6
    for line3 in range(3): 
        grid=[] 
        for i in range(vertcount,vertcount+3): 
            for j in range(horicount,horicount+3): 
                if List[i][j] in grid: 
                    return False
                else:     
                    grid.append(List[i][j])                 
        vertcount += 3
        grid=[]         
    return True

values=[]         
for i in range(9): 
    #Get the grid from the user line by line
    line = input() 
    values.append(line) 
if row_checker(values) == True and column_checker(values) == True and block_checker(values) == True: 
    print('Sudoku grid is valid') 
else: 
    print('Sudoku grid is not valid')