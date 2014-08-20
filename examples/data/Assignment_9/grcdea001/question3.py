"""Program to determine if a suduko grid is valid
Dean Gracey
15/5/2014"""
grid = []
for i in range (0,9):
    grid.append(input(""))
    

valid = True

for y in range(0,9):
    numinrow = []
    del numinrow[0:len(numinrow)]
    for x in range (0,9):
        if((grid[y][x]) in numinrow)==True:

            valid = False
            
        else:
            numinrow.append(grid[y][x])
            
for x in range(0,9):
    numincolumn = []
    del numincolumn[0:len(numincolumn)]
    for y in range(0,9):
        if grid[y][x] in numincolumn:

            valid = False
            
        else:
            numincolumn.append(grid[y][x])
        
        
#check 3 by 3 blocks
def check3x3 (yi,ye,xi,xe):
    numfound = []
    del numfound[0:len(numfound)]
    for y in range (yi,ye):
        
        for x in range (xi,xe):
           
            if grid[y][x] in numfound:   
                global valid 
                valid = False
                
            else:
                numfound.append(grid[y][x])

check3x3 (0,3,0,3)
check3x3 (0,3,3,6)
check3x3 (0,3,6,9)
check3x3 (3,6,0,3)
check3x3 (3,6,4,6)
check3x3 (3,6,6,9)
check3x3 (6,9,0,3)
check3x3 (6,9,3,6)
check3x3 (6,9,6,9)

if valid==True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")