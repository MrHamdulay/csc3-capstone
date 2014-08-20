'''Question 3 Assignment 9
Charlie Shang
SHNHUA002
2014.05.15'''

def checkvalidity():      
    valid = False #initialising variable    
    
    #put input into a list
    grid = []
    for i in range(9): #every row
        inputstr = input()
        
        for i in range(9):#value in the row
            grid.append((inputstr[i]))
    
           
    #Assign a co ordinate to each value
    count = 0
    co_ordinates = []
    for j in range(9): 
        for i in range(9):       
            co_ordinates.append([grid[count],i+1,0-j]) #[value,row,col]
            count += 1
    
    
    temprow = []
    #check for repeats in row
    for y in range(9): #put all the values from the y'th row into one list
        for x in range(9): 
            
            if co_ordinates[x][1] == y:#append if the y coordinate of the value == y
                temprow.append(co_ordinates[x][0])
            
        for k in range(9): #check if any values are repeated
            if co_ordinates[x][0] in temprow:
                valid = False
            else: 
                valid = True
                
    tempcol = []            
    #Check for repeats in columns
    for x in range(9): #puts all the values from the x'th column to one list
            for y in range(9):
                if co_ordinates[x][2] == x: #append if the x coordinate of the value == x
                    tempcol.append(co_ordinates[x][0])
                    
            for k in range(9):
                if co_ordinates[x][0] in tempcol: #tests for repetition
                    valid = False
                else: 
                    valid = True   
    count2 = 0 
    tempgrid = []
    #Divide grid into sub-grid
    for y in range(0,81,27): #there is a difference of 27 between each subgrid vertically according to the co-ordinates
        for x in range(0,9,3): #difference of 3 between every horizontal subgrid
            tempgrid = []
            
            for j in range(0,27,9): #check the first, second and thrid row in subgrid
                for k in range(3):
                    tempgrid.append(grid[j+k+x+y]) #append the value in the subgrid to tempgrid 
            
            #Check for repeats in the sub-grid          
            for m in range(9):
                count2 = 0
                
                for n in range(9):
                    if tempgrid[m] == tempgrid[n]:
                        count2 += 1
                        
                if count2 > 1: #if a charater is repeated, it is invalid
                    valid = False
                    break
    
    if valid == True:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

checkvalidity()