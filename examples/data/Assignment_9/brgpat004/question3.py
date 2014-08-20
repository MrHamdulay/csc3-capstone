'''program to check if a complete Sudoku grid is valid
Patrick Boroughs
10 May 2014
'''

#input lines
line1=list(input())
line2=list(input())
line3=list(input())
line4=list(input())
line5=list(input())
line6=list(input())
line7=list(input())
line8=list(input())
line9=list(input()) 

#create 2d array
grid=[line1,line2,line3,line4,line5,line6,line7,line8,line9]

#test for repeated characters along vertical lines
def testvertical(grid):
    for x in range(9):
        for y in range(8):
            for j in range(y+1,9):
                if grid[y][x]==grid[j][x]:
                    return False
    return True

#test for repeated characters along horizontal lines
def testhorizontal(grid):
    for y in range(9):
        for x in range(8):
            for j in range(x+1,9):
                if grid[y][x]==grid[y][j]:
                    return False
    return True

#test for repeated characters within subgrids
def testsquare(grid):
    xstart = 0
    ystart = 0
    
    #flag that all 9 grids have been tested
    flag=True
    while flag:
        
        #array where values already in subgrid are stored
        subgrid = []
        for y in range(0+ystart,3+ystart):
            for x in range(0+xstart,3+xstart):
                
                #repition found
                if grid[y][x] in subgrid:
                    return False
                else:
                    subgrid.append(grid[y][x])
                    
        #test next block to right
        if xstart<6:
            xstart += 3 
            
        #test first block in next row
        elif ystart<6:
            ystart += 3 
            xstart = 0
            
        #all blocks checked
        elif xstart == 6 and ystart ==6:
            flag=False 
            
    return True

#if all tests are true        
if testvertical(grid) and testhorizontal(grid) and testsquare(grid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")