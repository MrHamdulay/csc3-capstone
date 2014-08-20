"""Question 3-Assignment9
FRNHAN004
16 May 2014"""
grid1=[]

sudoku=input()#get the sudoku grid that you want to check
grid1.append(sudoku)

for i in range(0,8):
    sudoku=input()
    grid1.append(sudoku)



#Create 2D array with 81 empty grids
grid = []
height = 9
for i in range(height):
    grid.append([grid1[i]]) #fill empty grid with input

def row_check(): 
    for i in range(0,len(grid)): #access each number is list across
        list1=[]
        for j in range(0,len(grid)):
            if grid[i][0][j] in list1:
                return False
            else: 
                list1.append(grid[i][0][j])
    return True

def col_check(): 
    for j in range(0,len(grid)): #access each number is list down
        list2=[]
        for i in range(0,len(grid)):
            if grid[i][0][j] in list2:
                return False
            else: 
                list2.append(grid[i][0][j])
    return True

def grid_check():
    for j in range(0,9,3): #access each number is list of 3 and then move down a line
        list3=[]
        for col in range(j,j+3): #looking for every three
            for row in range(j,j+3):
                list3.append(grid1[col][row])
        list4=[]
        for j in list3:
            if j in list4:
                return False
            else: 
                list4.append(j)
    return True  
    
if row_check()==True and col_check()==True and grid_check()==True: #if all true then grid is valid
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")

    
        
    