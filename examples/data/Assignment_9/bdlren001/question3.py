# a program to check if a complete Sudoku grid is valid or not
# Budeli Rendani
# BDLREN001
# 14/05/2014

def main():
# initial values
    horizontal = True
    vertical = True
    gridler = True
    sudoku = []  

    # populating sudoku grid
    length=9
    for i in range(length):
        row = input("")
        sudoku.append(row)

    # grid test
    length=9
    gchecklist = []
    for i in range(length):
        line = sudoku[i]
        # converts the entire sudoku  grid into a liner array
        for i in range(length):
            gchecklist.append(line[i:i+1])

    # vertical test
    length=9    
    for x in range(length):
        vchecklist = []
        for i in range(length):
            line = sudoku[i]
            vchecklist.append(line[x:x+1])
        for i in range(length):
            if vchecklist.count(vchecklist[i]) > 1:
                vertical = False
            
    # horizontal check
    length=9
    for i in range(length):
        line = sudoku[i]
        hchecklist = []
        # converting the sudoku column into a string
        for i in range(length):
            hchecklist.append(line[i:i+1])
        for i in range(length):
            if hchecklist.count(hchecklist[i]) > 1:
                horizontal = False

    counter = 0
    # constructs grids from the linear array of the sudoku grid and checks them
    for i in range(len(gchecklist)-27):
        grid = ""
        if i%9 ==0:
            counter += 1
        if counter%4 == 0 or counter == 1:
            if i%3 == 0:
                for l in range(3):
                    grid += gchecklist[i + l]
                for l in range(3):
                    grid += gchecklist[i + 9 + l]        
                for l in range(3):
                    grid += gchecklist[i + 18 + l]
                    num = 0
                for k in range(9):
                    num += int(grid[k:k+1])
                if num != 45:
                    gridler = False
                    grid = "" 
    if horizontal == True and vertical == True and gridler == True:
        print("Sudoku grid is valid")
    else:   
        print("Sudoku grid is not valid")
main()