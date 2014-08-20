"""Program to check if sudoku solution is valid
Pankaj Munbodh
11 May 2014"""


sudoku_grid=[]

#create 9X9 grid"
def create_grid9(grid):
    for i in range(9):
        grid.append([0,0,0,0,0,0,0,0,0])
    return grid

def create_grid3(grid):
    for i in range(3):
        grid.append([0,0,0])
    return grid

#create empty sudoku grid
create_grid9(sudoku_grid)

#create sudoku grid from values inputted
count=0        
while count < 9:
    sudoku_string=input('')
    sudoku_list=[] 
    for num in sudoku_string:
        sudoku_list.append(int(num))
    for number in range(len(sudoku_list)):
        sudoku_grid[count][number]=sudoku_list[number]
    count=count+1

#check each row of sudoku grid by examining the number of times a number occurs(if greater than 1, then sudoku grid is invalid.)
def check_row(sudoku_grid):
    for row in range(9):
        for column in range(9):
            occurence_row=sudoku_grid[row].count(sudoku_grid[row][column])
            if occurence_row >1:
                return False
    return True

#create column to use in check_column below.
def create_column(sudoku_grid,column_number):
        column_vert=[]
        for row in range(9):
            column_vert.append(sudoku_grid[row][column_number])
        return column_vert

#check column by examining the number of times a number occurs(if greater than 1, then sudoku grid is invalid.)           
def check_column(sudoku_grid):   
    for column in range(9):
        column_vert=create_column(sudoku_grid,column)
        for row in range(9):
            
            occurence_column=column_vert.count(sudoku_grid[row][column])
            if occurence_column >1:
                return False
    return True

#check each subgrid within sudku grid using global variables (as multiples to control the range of indices in subgrid)    
control_sub1=0
control_sub2=0
def check_subgrid(row1,sudoku_grid):
    global control_sub1
    global control_sub2
    sub_grid=[]
             
    for row in range(0+row1*control_sub2,3+row1*control_sub2):
        for column in range(0+row1*control_sub1,3+row1*control_sub1):
            sub_grid.append(sudoku_grid[row][column])
    for element in sub_grid:
        if sub_grid.count(element)>1:
            return False
    if control_sub1==2 and control_sub2==2:
        return True
    if control_sub1<2:
        control_sub1+=1
    else:
        control_sub1=0
        control_sub2+=1
        
    return check_subgrid(3,sudoku_grid)

#execute all functions and if one of them returns false, then sudoku grid is invalid, else it is valid.
if check_row(sudoku_grid)==False or check_column(sudoku_grid)==False or check_subgrid(3,sudoku_grid)==False:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")



        
    