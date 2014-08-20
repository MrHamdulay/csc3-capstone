#VHRJOC001
#question3 assignment 9 
#checking a sudoku board to win
#the answers to the sudoku
line1=list(input())
line2=list(input())
line3=list(input())
line4=list(input())
line5=list(input())
line6=list(input())
line7=list(input())
line8=list(input())
line9=list(input())

#ake the grid
grid=[line1,line2,line3,line4,line5,line6,line7,line8,line9]

#checking for repteaded numbers going up
def testvertical(grid):
    for x in range(9):
        for y in range(8):
            for j in range(y+1,9):
                if grid[y][x]==grid[j][x]:
                    return False
    return True

#checking for repeated numbers going across
def testhorizontal(grid):
    for y in range(9):
        for x in range(8):
            for j in range(x+1,9):
                if grid[y][x]==grid[y][j]:
                    return False
    return True

#checking for the repeated values within the mini grid
def testsquare(grid):
    xstart = 0
    ystart = 0

    #teller
    flag=True
    while flag:

        #mini grid 
        subgrid = []
        for y in range(0+ystart,3+ystart):
            for x in range(0+xstart,3+xstart):

                #discovered error
                if grid[y][x] in subgrid:
                    return False
                else:
                    subgrid.append(grid[y][x])

        #testing mini grids1
        if xstart<6:
            xstart += 3

        #testing mini grids2
        elif ystart<6:
            ystart += 3
            xstart = 0

        #testing mini gridsall
        elif xstart == 6 and ystart ==6:
            flag=False

    return True

#if the sudoku is correct
if testvertical(grid) and testhorizontal(grid) and testsquare(grid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
