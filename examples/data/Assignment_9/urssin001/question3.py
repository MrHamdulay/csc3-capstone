'''Write a program to check if a complete Sudoku grid is valid or not.
Sinead Urisohn
14 May 2014
'''
#set empty grid
grid=[]

#append default values of 0 to empty grid
for i in range(9):
    grid.append([0]*9)

#get sudoku grid and append values to grid
for row in range(9):
    line =input("")
    #quit if nothing entered
    if line=="": break
    for col in range(9):
        grid[row][col]=line[col]
        
def checkcol(grid):
    '''function that receives grid as parameter and checks if 
    2 cells in the same column have the same value
    returns True or False'''
    #set check to True
    check=True
    #loop through rows and columns of grid
    for row in range(8):
        for col in range(9):
            #loop from next element in row below to length to compare column values
            for j in range(row+1,9):
                #compare items
                if grid[row][col]==grid[j][col]:
                    check =False
    return check
def checkrow(grid):
    '''function that receives grid as parameter and checks if 
       2 cells in the same row have the same value
       returns True or False''' 
    #set check to True
    check=True
    #loop through rows and columns of grid
    for row in range(9):
        for col in range(8):
            #loop from next element in same row to length to compare row values
            for j in range(col+1,9):
                #compare items
                if grid[row][col]==grid[row][j]:
                    check =False
    return check    
def checksubgrid(grid):
    '''function that receives grid as parameter and checks 
    if 2 cells in the same 3x3 sub-grid have the same value
    returns True or False'''
    #set check to True
    check = True
    #set list of numeric string literals 1-9 to see if subgrid valid
    numbers=['1','2','3','4','5','6','7','8','9']
    #set empty subgrid
    subgrid=[]
    #loop through row in steps of 3 to get 3x3 non-overlapping subgrids
    for row in range(0,9,3):
        #loop through column in steps of 3 to get 3x3 non-overlapping subgrids
        for col in range(0,9,3):
            #subrow from row to 3 down
            for subrow in range(row,row+3):
                #subcolumn from col to 3 down
                for subcol in range(col,col+3):
                    #append 3x3 subgrid to list
                    subgrid.append(grid[subrow][subcol])
            subgrid.sort()    
            
            #if subgrid sorted does not equal numbers list it is not valid so
            #check is False
            if subgrid!=numbers:
                check = False
            #set subgrid list to empty for next iteration comparison
            subgrid=[]
    #return results of check
    return check
#print results
if checkcol(grid)==True and checkrow(grid)==True and checksubgrid(grid)==True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")