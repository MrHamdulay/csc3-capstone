"""Assignment9 Question 3
Gyu Park
16 05 2014"""


def crgrid(x):
    grid=[]  
    for row in range(9):
        accr=[]  #creates a list for the rows
        for col in range(9):
            accr.append(eval(x[row][col]))  #puts values in rows
        
        grid.append(accr) #puts rows into grid
    return grid
        
        
    

#iterate through rows
def rowcheck(grid):
    for rows in range(9):
        rowlists=[] #creates a list for the rows
        for col in range(9):
            rowlists.append(grid[rows][col]) #puts values across the row into list
        for i in rowlists:
            if rowlists.count(i)!=1: #if a value appears more than once
                return False
            else: 
                continue #continues for the rest of the rows
    return True        

#iterate through columns            
def colcheck(grid):
    for col in range(9):
        col_list=[]
        for rows in range(9):
            col_list.append(grid[rows][col])
        for i in col_list:
            if col_list.count(i) !=1:
                return False
            else:
                continue
    return True
            

#iterate through subgrid
def subgridcheck(grid, row1,row2, col1, col2): #these are parameters for the ranges
    subgrid1=[]
    for row in range(row1, row2): #row1 and row2 will change depending on the subgrid
        for col in range(col1, col2):
            subgrid1.append(grid[row][col])
    for i in subgrid1:
        if subgrid1.count(i)!=1:
            return False
        else:
            return True
        
        
def checkall():
    num_list=[]
    while len(num_list)!=9:
        enter=input("")
        num_list.append(enter)
    
    sudo=crgrid(num_list)
    
    ye="Sudoku grid is valid"
    nop="Sudoku grid is not valid"
    
    if rowcheck(sudo)==False:
        print(nop)
    elif colcheck(sudo)==False:
        print(nop)
    elif subgridcheck(sudo, 0, 3, 0, 3)==False:
        print(nop)
    elif subgridcheck(sudo, 0, 3, 3, 6)==False:
        print(nop)
    elif subgridcheck(sudo, 0, 3, 6, 9)==False:
        print(nop)
    elif subgridcheck(sudo, 3, 6, 0, 3)==False:
        print(nop)
    elif subgridcheck(sudo, 3, 6, 3, 6)==False:
        print(nop)
    elif subgridcheck(sudo, 3, 6, 6, 9)==False:
        print(nop)
    elif subgridcheck(sudo, 6, 9, 0, 3)==False:
        print(nop)
    elif subgridcheck(sudo, 6, 9, 3, 6)==False:
        print(nop)
    elif subgridcheck(sudo, 6, 9, 6, 9)==False:
        print(nop)
    else:
        print(ye)
        
        
  
  
checkall()      
    