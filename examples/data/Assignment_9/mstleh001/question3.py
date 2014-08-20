""" a program to check if a sudoku grid is valid or not
Lehlogonolo Masetla
13 May 2014"""

sudokugrid = []                              # create empty 1-D grid array  

for i in range(9):                                                  
    i = input("")                                                     
    row = []                                 # create empty row variable
    for l in range(9):                       # create 9 columns
        row.append(i[l])                     # add the numbers to each column in the row
    sudokugrid.append(row)                   # append the list to sudoku list

def check1(sudokugrid): 
    
    for row in range(9):                                            
        for check1 in range(1,10):                                 
            if sudokugrid[row].count(str(check1))>1:                   
                return False                                        
    else: return True                                               

def check2(sudokugrid): 

    for column in range(9):                                         
        for row in range(8):                                        
            for check2 in range(row+1,9):                          
                if sudokugrid[row][column] == sudokugrid[check2][column]:    
                    return False                                    
    else: return True                                              

def check3(sudokugrid): 

    for grids1 in range(3):                                        
        for grids2 in range(3):                                    
            grid = []                                                 
            for row in range((3*grids1),(3*(grids1+1))):          
                for column in range((3*grids2),(3*(grids2+1))):   
                    grid.append(sudokugrid[row][column])                
            for number in range(1,10):                              
                if grid.count(str(number))>1:                       
                    return False                                    
    else: return True                                               

if check1(sudokugrid) and check2(sudokugrid) and check3(sudokugrid):         
    print("Sudoku grid is valid")                                   
else:                                                              
    print("Sudoku grid is not valid")                               