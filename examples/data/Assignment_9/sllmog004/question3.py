"""Assignment 9 Question 2
Yaseen Sulliman 
11 May 2014"""

sudokugrid=[]  # create empty sudoku list                                                         
for i in range(9):                                                  
    i=input("")                                                     
    row=[] # create empty row variable
    for j in range(9):#create 9 columns
        row.append(i[j]) # add the numbers to each column in the row
    sudokugrid.append(row)  # append the list to sudoku list

def check_1(sudokugrid): 
    """checks to see if more than one of same number is in the same row"""
    for row in range(9):                                            
        for check_1 in range(1,10):                                 
            if sudokugrid[row].count(str(check_1))>1:                   
                return False                                        
    else: return True                                               

def check_2(sudokugrid): 
    """checks to see if more than one of same number is in the column"""
    for column in range(9):                                         
        for row in range(8):                                        
            for check_2 in range(row+1,9):                          
                if sudokugrid[row][column]==sudokugrid[check_2][column]:    
                    return False                                    
    else: return True                                              

def check_3(sudokugrid): 
    """checks to see if any of the same number is within the smaller 3x3 grid"""
    for grids_1 in range(3):                                        
        for grids_2 in range(3):                                    
            grid=[]                                                 
            for row in range((3*grids_1),(3*(grids_1+1))):          
                for column in range((3*grids_2),(3*(grids_2+1))):   
                    grid.append(sudokugrid[row][column])                
            for number in range(1,10):                              
                if grid.count(str(number))>1:                       
                    return False                                    
    else: return True                                               

if check_1(sudokugrid) and check_2(sudokugrid) and check_3(sudokugrid):         
    print("Sudoku grid is valid")                                   
else:                                                              
    print("Sudoku grid is not valid")                               