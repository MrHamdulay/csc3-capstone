#Gillian Wachira
#a program to check if a complete Sudoku grid is valid or not.
#15/05/2014

def main(): 
    valid = True  
    grid = []  
    for i in range(9):#check the row
        grid.append([])#add empty list
        line = input()
        for j in range(9):#check the column
            num = line[j]
            if line.count(num)>1:  #check if the number repeats itself
                valid =False
               
            else:
                grid[i].append(num) #if not add in the number
            
    for i in range(9):
        line=""  
        for j in range(9):
            line+=grid[j][i]   
        for k in range(9):
            num = line[k]
            if line.count(num)>1:
                valid =  False
                
                
              
 #check each block in steps of 3   
            
    for i in range(0,9,3): 
        block=""
        for j in range(i,i+3):
            for k in range(0,3):
                block+=grid[j][k]


        for k in range(9):
            num = block[k]                   
            if block.count(num)>1:    
                valid =  False
                
               
    
    
    for i in range(0,9,3): 
        block=""
        for j in range(i,i+3):
            for k in range(3,6):
                block+=grid[j][k]
                
        for k in range(9):
            num = block[k]                   
            if block.count(num)>1:
                valid =  False
                
                
                               
    for i in range(0,9,3): 
        block=""
        for j in range(i,i+3):
            for k in range(6,9):
                block+=grid[j][k]
                                              
   
        for k in range(9):
            num = block[k]                   
            if block.count(num)>1:  
                valid =  False
                
                       
    if valid == True:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")


main()