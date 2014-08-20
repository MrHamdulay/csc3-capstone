'''Luke Joseph
2014-05-15
Question 3 of assignment 9'''

def sudoku():
    inp=""
    grid=[]
    x=0
    y=0
    z=0
    za=0
    w=0
    for i in range(9):
        inp=input("")
        grid.append(inp)    
    
    for i in range(9): # Checking rows
        x=0
        for j in range(9):
            x+=eval(grid[i][j])
        if x ==45 :
            z+=1
    if z==9:
        for i in range(9): # Checking columns
            y=0
            for j in range(9):
                y+=eval(grid[j][i])
                if y==45:
                    za+=1
        if za==9:
            x=0
            for i in range(3): # Checking sub-squares
                for j in range(3):
                    x+=eval(grid[i][j])
            if x==45:
                print("Sudoku grid is valid")
            else:
                print("Sudoku grid is not valid")
        else:
            print("Sudoku grid is not valid")
    else:
        print("Sudoku grid is not valid")
        #print("1")
        #print(x)
sudoku()
        