"""program to check whether sudoku grid is valid
nasha somoina meoli
11th may 2014"""
def check_grid():
    """check grid validity"""
    y = 0
    element =input("")
    grid = [element]
    for i in range(8):
        grid.append(input(""))
    #check if any two items in a row are similar
    for i in grid:
        for j in range(1,10):
            unique = i.count(str(j))
            if unique > 1:
                y = 1
    grid_2 = []
    #form 2-d list
    for i in grid:
        smaller_grid = []
        for j in range(9):
            smaller = i[j]
            smaller_grid.append(smaller)
        grid_2.append(smaller_grid) 

    #check if any two items in a column are similar
    
    for col in range(9):
        
        for row in range(9):
                check = grid_2[col][row]
                s = grid_2[col].count(check)
                if s >1:
                    y = 1
                    break
    #check if a 3 by 3 grid has similar items
    grid_3 = []
    for j in range(0,9,3):
        for i in range(9):
            sliced = grid_2[i][j:j+3]
            grid_3.append(sliced)
    for i in range(0,25,3):
        check = grid_3[i:i+3]
        check_2 = check[0]+check[1]+check[2]
        for a in check:
            for b in a:
                validity = check_2.count(b)
                
                if validity >1:
                    y = 1
                    break
    # all checks return y= 1 if the grid is invalid
    if y == 1:
        print("Sudoku grid is not valid")
    else:
        print("Sudoku grid is valid")
check_grid()