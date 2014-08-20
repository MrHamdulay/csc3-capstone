"""
14 May 2014
Assignment9 Question 3
MDLCAR002 
Program to check if a soduku grid is valid or not
"""


def main():
    #Part One
   
    valid= True# this is a variable which stores the value "True"
    grid=[]
   
    #checks the rows
    for i in range(9):
        line1=[]
        line = input()# input the first line of 9 numbers. There will be no prompt, user will just input the numbers and press enter. All 9 rows will be entered this way
        for i in range(9):
            line1.append(line[i])# adds each number to the list1
        for j in range(9):
            if (line1.count(str(j+1))>1):#counts the occurance of the numbers 1-9, if a certain number occurs more than once the the grid is false
                valid=False
        grid.append(line1)# adds the single list to a 2D list
    
    #Part Two
    #checks the columns downwards   
    for i in range(9):
        line1=[]
        for j in range(9):
            line1.append(grid[j][i])
        for i in range(9):
            if (line1.count(str(i+1))>1):
                valid=False 
    line2=[]
    
    #Part Three
    #checks the first 3x3 grid for multiple occurrences of numbers and output if numbers occur more than once
    
    for i in range(9):# takes the first three numbers of each row and adds it to a string
        
        for j in range(3):
            line2.append(grid[i][j])
        if(i==2 or i==5):
            for i in range(9):
                if (line2.count(str(i+1))>1):
                    valid=False
            line2=[]
    line2=[]
        
    #checks the second 3X3 grid. This code takes the numbers from position 3-6 and adds it the string          
    for i in range(9):
        for j in range(3,6):
            line2.append(grid[i][j])
        if(i==2 or i==5):
            for i in range(9):
                if (line2.count(str(i+1))>1):
                    valid=False 
            line2=[]
    line2=[]
        
    #checks the third 3x3 grid which is the last 3 numbers from each row
    for i in range(9):
        for j in range(6,9):
            line2.append(grid[i][j])
        if(i==2 or i==5):
            for i in range(9):
                if (line2.count(str(i+1))>1):
                    valid=False 
            line2=[]
    line2=[]
             
            
    if(valid):                              # if "valid" stayed true then the grid is valid
        print("Sudoku grid is valid")
    else:                                   # if valid turned false anywhere
        print("Sudoku grid is not valid")
               

main()