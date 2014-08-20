#Shaaheen Sacoor SCRSHA001
#14 May 2014
#Program to check sudoku grid

def main():
    sudoku_lis = []      # Creates 9x9 grid, Adds numbers to grid
    for i in range(9):  
        x = input("")
        sudoku_lis.append([x])
    
    check_count = 0
    sudoku_valid = False        #Variables to check validity
    subsquare = True
    for i in range(len(sudoku_lis)): #
        sum_C =0
        for j in range(9):
            sum_C += eval(sudoku_lis[i][0][j]) #Goes through list and adds each row of numbers together
        if sum_C == 45:                        #Since each number has to be different in sudoku,
            check_count +=1                    #Each line must add up to 45 and if it doesn't then it is invalid
            
    if check_count == 9:
        sec_count = 0
        for i in range(len(sudoku_lis)): #This will check if every column adds up to 45 similar to before
            sum_A =0
            for j in range(9):
                sum_A += eval(sudoku_lis[j][0][i])
            if sum_A == 45:
                sec_count +=1
        if sec_count == 9:                
            sudoku_valid = True
    counter2 = 0        
    for i in range(0,9,3):
        sub_square =[]
        for y in range(3):                #Checks the subsquares in grid 
            for x in range(3):
                sub_square.append(sudoku_lis[y][0][x])
        for j in sub_square:
            x = sub_square.count(j)        #If an item occurs more than once, it is invalid
            if x > 1:
                subsquare = False
        
        
    if sudoku_valid is True and subsquare is True:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
        
main()
    