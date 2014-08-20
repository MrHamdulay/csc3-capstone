#Assignment 9, question 3
#Dean Bunce
#11 May 2014
#Program to check if a Sudoku grid is valid
 
 
#Create a 2D array from inputs 
grid_2D=[] 
for i in range(9):
            grid=[]
            numbers=input("")
            for j in range(9):
                        grid.append(eval(numbers[j]))
            grid_2D.append(grid)

                                  


def check_row(grid_2D):
            
            #Check for one occurence of each number in a row, set an initial boolean value to true
            valid=True
            for row in range(9):
                        count_list=[0, 0, 0, 0, 0, 0, 0, 0, 0]
                        #Set the values of the row to the indices of a new list, then check that each index has been referenced exactly once
                        for col in range(9):
                                    count_list[grid_2D[row][col]-1]+=1
                                    check_list=count_list[:10]
                        #If it doesn't set initial boolean to false and return it
                        if not check_list==[1,1,1,1,1,1,1,1,1]:
                                                
                                                valid=False
                                                return valid
            return valid
             
#Repeat the process for each column
def check_column(grid_2D):
            valid_2=True
            for row in range(9):
                        count_list=[0,0,0,0,0,0,0,0,0]
                        for col in range(9):
                                    #Check columns instead of rows by changing the order of the indeces from the 2D array
                                    count_list[grid_2D[col][row]-1]+=1
                                    check_list=count_list[:10]
                        
                        if not check_list==[1,1,1,1,1,1,1,1,1]:
                                    
                                    valid_2=False
                                    return valid_2
            return valid_2
            
                        
#Repeat the process for each 3x3 block
def check_block(grid_2D):
            valid_3=True
            
            for row in range(9):
                        count_list=[0,0,0,0,0,0,0,0,0]
                        for col in range(9):
                                    #Adjust indeces to check 3x3 block
                                    count_list[grid_2D[col//3+(row%3)*3][col%3+(row//3)*3]-1]+=1
                                    check_list=count_list[:10]
                                    
                        if not check_list==[1,1,1,1,1,1,1,1,1]:
                                   
                                    valid_3=False
                                    return valid_3
            return valid_3
            
def check_all():
            
            #Check if all booleans are true and give corresponding output
            row = check_row(grid_2D)
            col = check_column(grid_2D)
            block = check_block(grid_2D)
            if row==True and col==True and block==True:
                        print("Sudoku grid is valid")
            elif row==False or col==False or block==False:
                        print("Sudoku grid is not valid")
                        
check_all()