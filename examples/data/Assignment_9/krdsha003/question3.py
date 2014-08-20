"""Assignment9 question3
check if complete sudoku grid is valid
Shaheen Karodia
KRDSHA003
2014-05-10"""

def create_grid(l):
    """creates a sudokue 2x2 array"""
    sudoku=[]               
    for i in range (len(l)):
        row=[]
        for j in range(9):
            row.append(eval(l[i][j]))  
            
        sudoku.append(row)   #appends each row at a time to the sudoku list
   
    return sudoku

def check_horizontal(grid):
    """checks each row to check invalidity"""
    #create a list to check values of sudoku grid against
    check=[]
    for i in range(1,10):
        check.append(i)
    
    for row in range(9):  #checks within each row 
        for i in range(1,10):  #check numbers through digits 1 to 9
            if i not in check or (grid[row]).count(i)>1:  #checks if there is a duplicate #checks that the value is one from 1 to 9
                return False
                
    return True
        
def check_vertical(grid):
    """check each collumn for invalidy"""
    #create a list to check values of sudoku grid against
    check=[]
    for i in range(1,10):
        check.append(i)    
    
    for col in range(9):
        collumn=[]
        for row in range(9):
            collumn.append(grid[row][col])
            
        for i in range(1,10):
            if i not in check or(collumn).count(i)>1:
                return False
    return True

def sub_grid_check(grid, r_index, c_index):
    """checks each 3 by 3 grid validity"""
    sub_grid=[]
    #populate subgrid
    for row in range(3):
        for col in range(3):
            sub_grid.append(grid[row+r_index][col+c_index])
    
    #check the number of occurences of the numbers one to nine                       
    for i in range(1,10):
        if sub_grid.count(i)>1:
            return False
    return True 

def main():
    
    
    neg=("Sudoku grid is not valid")
    pos=("Sudoku grid is valid")

    lines=[]
    
    #Get each line of sudoku into one list
    while len(lines)!=9:
        x=input("")
        lines.append(x)
    
    # create a sudoku grid from input
    final_grid= create_grid(lines)
    
    if check_horizontal(final_grid)==False:
        print(neg)
    elif  check_vertical(final_grid)==False:
        print(neg)
    elif sub_grid_check(final_grid, 0, 0)==False:
        print(neg)
    elif sub_grid_check(final_grid, 0, 3)==False:
        print(neg)  
    elif sub_grid_check(final_grid, 0, 6)==False:
        print(neg)
    elif sub_grid_check(final_grid, 3, 0)==False:
        print(neg)
    elif sub_grid_check(final_grid, 3, 3)==False:
        print(neg)
    elif sub_grid_check(final_grid, 3, 6)==False:
        print(neg)
    elif sub_grid_check(final_grid, 6, 0)==False:
        print(neg)
    elif sub_grid_check(final_grid, 6, 3)==False:
        print(neg)
    elif sub_grid_check(final_grid, 6, 6)==False:
        print(neg)
    else: 
        print(pos)
   
        
  
        
        
    
    
    
main()


     
         







                    
                