# Program to check validity of Soduku grid
# GVNMER006-Merosha Govender
#16 May 2014

def main():
    
    valid= True#variable that stores the value "True"
    grid=[]# begins an array called grid
    for i in range(9):
        line1=[]#begins an array called line1
        line = input()# input the first line of 9 numbers. Will not ask for the 9 numbers. Input and press enter Then input the 2nd row of 9 numbers etc until the 9th row
        for x in range(9):
            line1.append(line[x])# adds each new value into the array
        for i in range(9):
            if (line1.count(str(i+1))>1):#counts  occurances of the numbers 1-9. if more than one occurence of a particular number is found then the grid is immediately incorrect 
                valid=False
        grid.append(line1)# adds the single array to a 2D array
        
    for i in range(9):# Same as above except this checks the columns going downwards. not the rows like the code above
        line1=[]
        for x in range(9):
            line1.append(grid[x][i])
        for i in range(9):
            if (line1.count(str(i+1))>1):
                valid=False 
    line2=[]# creates an array called line2
    
    for i in range(9):# Now this code. It takes the first 3 numbers of each row and adds it to a string. so the first row itl take the first 3. Then itl move to the next row and take the first 3 etc until the 3rd row. Coz thats a 3x3 grid. Itl check for multiple numbers. and output if numbers occur more than once.
        for x in range(3):
            line2.append(grid[i][x])
        if(i==2 or i==5):
            for i in range(9):
                if (line2.count(str(i+1))>1):
                    valid=False
            line2=[]
    line2=[]
        
                    
    for i in range(9):# This code takes the numbers from 3-6. the code above took the first 3 numbers from each row. This code takes the numbers from pos. 3-6 and adds it to a string. Then it checks if the numbers occur in the 3x3 grid in the middles 
        for x in range(3,6):
            line2.append(grid[i][x])
        if(i==2 or i==5):
            for i in range(9):
                if (line2.count(str(i+1))>1):
                    valid=False 
            line2=[]
    line2=[]
        
    
    for i in range(9):# finally this checks the last 3x3 grid. I.E THE last 3 numbers from each row forming the 3x3 grid. And checks them like above
        for x in range(6,9):
            line2.append(grid[i][x])
        if(i==2 or i==5):
            for i in range(9):
                if (line2.count(str(i+1))>1):
                    valid=False 
            line2=[]
    line2=[]
             
            
    if(valid):# if valid stayed true for the entire search then the grid is valid so if(valid) means if(True)...output that
        print("Sudoku grid is valid")
    else:# if valid turned false anywhere. Then itl print the code below.
        print("Sudoku grid is not valid")
         # Method is kind of complicated.im sure there are easier methods but i couldnt think of any at the time       

main()
