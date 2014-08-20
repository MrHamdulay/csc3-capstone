#Mbongeni Mazibuko
#MZBMBO002
#Assignment 9 Q3

grid=[]
for i in range(9):
    solution= input('')
    #iterates 9 times to get the 9 inputs for suduko rows
    for j in range(8):
        solution= list(solution)
        #gets each individual number
        solution[j]=solution[j]+' '
        #add space between individual numbers i.e iterate 8 times
    grid.append(solution)
    #row is appended to grid
    
def valid(grid):
    valid=1
    subtest=[]
    test=[0,0,0,0,0,0,0,0,0]
    for i in range(9):
        htest= list(set(grid[i]))
        #removes repetition of numbers
        if len(htest)<9:
            #checks if a value has been removed i.e. checks if there was repetition
            valid=0
            
        for j in range(9):
            test[j]= grid[j][i]
            #creates columns
        if len(list(set(test)))<9:
            #checks if a value has been removed i.e. checks if there was repetition
            valid=0
            
    count=3                    
    for k in range(0,9,3):
        #count in 3's to get subgrid which occur from every 3rd number in row and column
        for i in range(k,count):
            #get interval of the subgrid row
            for j in range(k,count):
                #get interval of the subgrid column
                subtest.append(grid[i][j])
                #appends values to subtest grid
                
        if len(list(set(subtest)))<9:
            #checks if a value has been removed i.e. checks if there was repetition
            valid=0
        count+=3
                     
    if valid==0:
        #valid is 0 when repetition occured in row, column or sub grid
        return False
    else: return True
    
solved =valid(grid)
if solved==False:
    print('Sudoku grid is not valid')
elif solved==True:
    print('Sudoku grid is valid')