'''program for checking if a sudoku grid is complete
nicole henning
due 16 may 2014'''

line1 = input("")
line2 = input("")
line3 = input("")
line4 = input("")
line5 = input("")
line6 = input("")
line7 = input("")
line8 = input("")
line9 = input("")

listed = [line1,line2,line3,line4,line5,line6,line7,line8,line9] #create list of input strings

valid = 0
    
for row in range(9):
    total_sum = 0
    for col in range(9):
        value = eval(listed[row][col])
        total_sum+=value
        if total_sum == 45: #ie, the sum of numbers from 1-9
            valid+=1 #ie count no of columns that is true for
            
if valid == 9: #ie sum = 45 for all columns: check rows
    
    valid = 0
    for col in range(9):
        total_sum = 0
        for row in range(9):
            value = eval(listed[row][col])
            total_sum+=value 
            if total_sum == 45: #sum 1-9
                valid+=1 #count when true
                
    if valid == 9: # if all rows add up to 45: check 9x9 blocks
        
        valid = 0
        for row in range(3):
            total_sum=0
            for col in range(3):
                value = eval(listed[row][col])
                total_sum +=value
            valid+=total_sum #if adds up to 45, grid is valid
        if valid == 45:
            print("Sudoku grid is valid")
        
        elif valid != 45: #if not all conditions are met, considered invalid
            print("Sudoku grid is invalid")
    
    elif valid != 9:
        print("Sudoku grid is invalid")
        
elif valid != 9:
    print("Sudoku grid is invalid")
    
    