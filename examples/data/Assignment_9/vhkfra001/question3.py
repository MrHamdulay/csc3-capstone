'''
program to check if a sudoku grid is valid or not
frans van hoek
13 may 2014
'''




def gridify():
    grid = input('', end='')
    grid = str(grid)
    # split input into 9 rows
    l = grid.split("\n")
    # define the new grid
    g = []
    
    c = -1
    # create an empty list for each of the 9 rows
    for i in range(9):
        g.append([])
      
    # append the values to the grid  
    for i in l:
        c += 1
        for n in i:
                g[c].append(int(n))
    return g


def checkrows(grid):
    row = False
    
    # sum
    rsum = True
    for i in grid:
        rsumv = 0
        for n in i:
            rsumv += n
        if rsumv != 45:
            rsum = False
            break
    
    # duplicates
    rdup = True
    for i in grid:
        for n in range(1, 10):
            if i.count(n) > 1:
                rdup = False
    
    if rsum == True and rdup == True:
        row = True
    
    if row == True:
        return True
    
def checkcolumns(grid):
    col = False
    
    # sum
    csum = True
    for i in range (9):
        csumv = 0
        for n in range(9):
            csumv += grid[n][i]
        if csumv != 45:
            csum = False
            break
        
    # duplicates
    
    
    
def main():
    y = gridify()
    r = checkrows(y)
    c = checkcolumns(y)
    
    if r == True and c == True:
        print ("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

if __name__ == "__main__": main()