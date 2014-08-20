'''program to check complete Sudoku grid
nasreen hoosain
11/05/14'''    

#function to check the grid        
def check(grid):
    for l in grid:
        l.sort() #sort in numerical order
        if l[0] != '1': #if first number is not one
            return False
        elif l[8] != '9': #if first number is not 9
            return False
        else: # check if two same numbers next to each other
            for i in range(8):
                if l[i] == l[i+1]:
                    return False
    else:
        return True
    
if __name__ == '__main__':
  
    grid = []
    for row in range (9):
        x = input()
        grid.append(x)    

    #get rows
    rows = []
    for j in range(9):
        row = []
        for i in range(9):
            row.append(grid[j][i])
        rows.append(row)
    
    #get columns
    cols = []
    for i in range(9):
        c = []
        for j in range(9):
            x = rows[j][i]
            c.append(x)
        cols.append(c)  
        
    #get blocks
    blocks = []
    for i in range(9):
        b = []
        for j in range(9):
            x = rows[3*(i//3) + j//3][3*(i%3) + j%3] #put 3x3 blocks in row
            b.append(x)
        blocks.append(b)              

    #check rows, columns and blocks
    if check(rows) == True and check(cols) == True and check(blocks) == True:
        print('Sudoku grid is valid')
    else:
        print('Sudoku grid is not valid')