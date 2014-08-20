""" Q3 of Assignment 9: Sudoku Grid Validator
Shaheel Kooverjee - KVRSHA004
15 May 2014 """

sdkgrid = []
for i in range(9):
    sdkgrid.append(list(input())) #append all inputted numbers in 2D list

def xtest(sdkgrid):
    for y in range(9):
        for x in range(8):
            for i in range(x+1, 9):
                if sdkgrid[y][x] == sdkgrid[y][i]:
                    return False #invalid if any repeated characters in horizontal lines
    return True

def ytest(sdkgrid):
    for x in range(9):
        for y in range(8):
            for i in range(y+1, 9):
                if sdkgrid[y][x] == sdkgrid[i][x]:
                    return False #invalid if any repeated characters in vertical lines
    return True

def subgridtest(sdkgrid): #repeated characters in subgrid
    startx, starty = 0, 0
    alltested = False
    
    while alltested != True: #runs until all 9 subgrids have been tested
        subgrid = []
        
        for y in range(starty, starty+3):
            for x in range(startx, startx+3):
                if sdkgrid[y][x] in subgrid: #invalid grid if character is repeated
                    return False
                else:
                    subgrid.append(sdkgrid[y][x])
        
        if startx < 6: 
            startx += 3 #start check of next subgrid to the right
        
        elif starty < 6: 
            starty += 3 #start check of next subgrid to the bottom
            startx = 0
        
        elif startx == 6 and starty == 6:
            alltested = True #loop not repeated once all 9 subgrids have been tested
            
    return True

if xtest(sdkgrid) and ytest(sdkgrid) and subgridtest(sdkgrid): #sudoku grid only valid if all tests True
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")