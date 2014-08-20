'''This program checks if a sudoku grid is valid or not
Sandile Christopher Mahlangu
14 April 2014'''

def get_grid():
    '''This function gets an input from the user and adds the numbers into a grid'''
    global grid
    the_row_grid=[] #The row array
    for adding in range(9):
        row=input()
        for number in row:
            the_row_grid.append(eval(number))
        grid.append(the_row_grid)
        the_row_grid=[]
         
        


def sudoku_check_vertical_and_horizontal(grid):
    '''This function checks is there are any vertical or horizontal numbers that are equal in a given sudoku grid'''
    
    #If there are duplicates then they won't be added into the set buy that we can realise that the grid is invalid
    
    
    #checking the row
    check_row=set()
    for ver in range(9):
        #using the set to check for horizontal duplicates
        for hor in range (9):
            check_row.add(grid[ver][hor])
        if len(check_row)<9:
            #When there are duplicates the len of the set will be less than nine
            return False
        check_row=set()
        
        #Checking the col
        check_col=set()
        for ver in range(9):
            #using the set to check for vertical duplicates
            for hor in range (9):
                check_col.add(grid[hor][ver])
            if len(check_col)<9:
                return False
            check_col=set()
        return True

def sudoku_check_3by3(grid):
    '''This function checks if the 3by3 grids are equal'''
    grid_with_3=[] #This is a grid with 3 colums and rows
    
    #Sets of 3by3, to check if there are any duplicates
    check1=set()
    check2=set()
    check3=set()    
    while grid:
        grid_with_3=grid[:3] #Taking 3 colums from the grid
        grid=grid[3:]  #removing the three culumns from the grid
        
        
        
        #for the first set
        for i in range(3):
            for j in range(3):
                check1.add(grid_with_3[i][j])
        if len(check1)<9:
            return False
        #for the second set
        for k in range(3):
            for l in range(3,6):
                check2.add(grid_with_3[k][l])
        if len(check2)<9:
            
            return False 
        
        #for the third set
        for m in range(3):
            for n in range(6,9):
                check3.add(grid_with_3[m][n])
        if len(check3)<9:
            return False 
        
        check1=set()
        check2=set()
        check3=set()
    return True
            
    
            
if __name__=='__main__':
    grid=[]
    get_grid()
    check_row_col=sudoku_check_vertical_and_horizontal(grid)
    check_3by3=sudoku_check_3by3(grid)
    
    
    if check_3by3 and check_row_col:
        print('Sudoku grid is valid')
    else:
        print('Sudoku grid is not valid')