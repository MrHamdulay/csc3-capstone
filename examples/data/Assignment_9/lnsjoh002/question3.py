"""Program to check whether a Sudoko grid is valid or not
JP Lanser
10 May 2014"""


#Prompt user for input 9 times, each time add the input to a temporary list, then append to the grid so that a 2D list is created
grid =[]
for i in range(9):
    temp_list=[]
    numbers =input()
    #loop through each number and add it to the temporary list
    for j in numbers:
        temp_list.append(j)
    grid.append(temp_list) #append temp list to grid
    
    


#function to check if a grid is valid, return false if it isn't. 

def check_valid(grid):
    
    #Check that all rows are valid  
    for i in range(9):
        numbers ='' #empty string initially. Add numbers to it (line 30). This is to check whether numbers are repeated, to determine whether the grid is valid or not
        for j in range(9):
            
            if str(grid[i][j]) in numbers:
                return False
            else: numbers+=(str(grid[i][j]))  
            
    #Check that all columns are valid
    for i in range(9):
        numbers=''
        for j in range(9):
            
            if str(grid[j][i]) in numbers:
                return False
            else: numbers+=(str(grid[j][i]))
            
    #Now check that all the 3X3 sub grids are vaid
    #This loop is to check whether the first three sub_grids (vertical) are valid
    for i in range(0,9,3):
        numbers =''
        
        for k in range(3):
            
            for j in range(3):
                
                if str(grid[i+k][j]) in numbers:
                    return False
                else:
                    numbers+=(str(grid[i+k][j]))
                    
                    
    #This loop is to check whether the second three sub_grids (vertical) are valid               
    for i in range(0,9,3):
        numbers =''
                            
        for k in range(3):
                                
            for j in range(3,6):
                                    
                if str(grid[i+k][j]) in numbers:
                    return False
                else:
                    numbers+=(str(grid[i+k][j]))
                    
                    
    #This loop is to check whether the third three sub_grids (vertical) are valid                
    for i in range(0,9,3):
        numbers =''
                                               
        for k in range(3):
                                                   
            for j in range(6,9):
                                                       
                if str(grid[i+k][j]) in numbers:
                    return False
                else:
                    numbers+=(str(grid[i+k][j]))
                    
                    
    return True

if check_valid(grid): 
    print("Sudoku grid is valid")
    
else:
    print("Sudoku grid is not valid")
                    
        
                
    
            
            
  
    
   
