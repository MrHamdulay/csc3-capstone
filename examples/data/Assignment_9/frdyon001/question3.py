"""checking if sudoku grid is valid or not
Yonela Ford
12 May 2014"""
#create a sudoku grid
a_grid = []
def make_grid(griddy):
    for s in range (9):
        griddy.append ([0] * 9)
    return griddy

make_grid(a_grid)

#get input values for each row in the sudoku grid
for a_row in range(9):
    x = input()
    for a_col in range(9):
        a_grid[a_row][a_col] = x[a_col]
"""check if each row satisfies then sudoku conditions"""
def row_checker():
    count = {} 
    #check the row
    for d in range(9):
        #check each number in the row
        for q in a_grid[d]:
            #add each unique number to my dictionary
            if not (q in count):
                count[q]=1
                pass
            #if number already exists in dictionary then it"s false
            else:
                return False
        #for each row create a new and cleared dictionary
        count = {}  
    return True
"""check if each column satisfies the sudoku contions"""
def col_checker():
    count = {} 
    #check each row
    for l in range(9):
        #check each coloumn
        for r in range(9):
            #for each value in the column
            for k in a_grid[r][l]:
                #add each unique value in the column to my dictionary
                if not (k in count):
                    count[k]=1
                    pass
                #if the number in the current column is already in the dictionary then it's False (not a valid sudoku)
                else:
                    return False
        count = {}  
    return True
"""check is 3-by-3 square"""
def check_3_by_3_grid():
    count = {}
    #check the row of 3 numbers at a time
    for x in range(3):
        #check the column
        for p in range(3):
            #checking the rows 3 at a time and moving along horizontally
            for i in range(3*x,3*x+3):
                #check the columns 3 at a time and moving down 3 at a time
                for j in range(3*p,3*p+3):
                    #check the indivual values, adding them to my dictionary if they are unique
                    for g in a_grid[i][j]:
                        if not (g in count):
                            count[g]=1
                            pass
                        else:
                            return False
            count = {}
    return True
#if all three conditions are met then it is a grid else it is not
if row_checker() and col_checker() and check_3_by_3_grid():
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")