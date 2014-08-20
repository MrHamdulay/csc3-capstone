"""A program to check whether completed sudoku grid is valid
Jason Findlay
12/05/2014"""

#Populate grid
grid=[""]*9

#Take input and put into grid
print(end="")
for i in range(9):
    grid[i]=input()
    
#Check if the rows are valid
valid=True
for i in range(9):
    if "1" in grid[i] and "2" in grid[i] and "3" in grid[i] and "4" in grid[i] and "5" in grid[i] and "6" in grid[i] and "7" in grid[i] and "8" in grid[i] and "9" in grid[i]:
        valid=True
    else:
        valid=False

#Check if the cols are valid
for i in range(9):
    line=""
    for j in range(9):
        line+=grid[j][i]
    if "1" in line and "2" in line and "3" in line and "4" in line and "5" in line and "6" in line and "7" in line and "8" in line and "9" in line and valid:
        valid=True
    else:
        valid=False

#Check if the 3X3 blocks are valid
#Check if the (1,1) block is valid
block=""
for i in range(3):
    block+=grid[i][:3]
if "1" in block and "2" in block and "3" in block and "4" in block and "5" in block and "6" in block and "7" in block and "8" in block and "9" in block and valid:
    valid=True
else:
    valid=False
#Check if the (2,1) block is valid
block=""
for i in range(3,6):
    block+=grid[i][:3]
if "1" in block and "2" in block and "3" in block and "4" in block and "5" in block and "6" in block and "7" in block and "8" in block and "9" in block and valid:
    valid=True
else:
    valid=False
#Check if the (3,1) block is valid
block=""
for i in range(6,9):
    block+=grid[i][:3]
if "1" in block and "2" in block and "3" in block and "4" in block and "5" in block and "6" in block and "7" in block and "8" in block and "9" in block and valid:
    valid=True
else:
    valid=False

    
#Check if the (1,2) block is valid
block=""
for i in range(3):
    block+=grid[i][3:6]
if "1" in block and "2" in block and "3" in block and "4" in block and "5" in block and "6" in block and "7" in block and "8" in block and "9" in block and valid:
    valid=True
else:
    valid=False
#Check if the (2,2) block is valid
block=""
for i in range(3,6):
    block+=grid[i][3:6]
if "1" in block and "2" in block and "3" in block and "4" in block and "5" in block and "6" in block and "7" in block and "8" in block and "9" in block and valid:
    valid=True
else:
    valid=False
#Check if the (3,3) block is valid
block=""
for i in range(6,9):
    block+=grid[i][3:6]
if "1" in block and "2" in block and "3" in block and "4" in block and "5" in block and "6" in block and "7" in block and "8" in block and "9" in block and valid:
    valid=True
else:
    valid=False

    
#Check if the (1,3) block is valid
block=""
for i in range(3):
    block+=grid[i][3:]
if "1" in block and "2" in block and "3" in block and "4" in block and "5" in block and "6" in block and "7" in block and "8" in block and "9" in block and valid:
    valid=True
else:
    valid=False
#Check if the (2,3) block is valid
block=""
for i in range(3,6):
    block+=grid[i][6:]
if "1" in block and "2" in block and "3" in block and "4" in block and "5" in block and "6" in block and "7" in block and "8" in block and "9" in block and valid:
    valid=True
else:
    valid=False
#Check if the (3,3) block is valid
block=""
for i in range(6,9):
    block+=grid[i][6:]
if "1" in block and "2" in block and "3" in block and "4" in block and "5" in block and "6" in block and "7" in block and "8" in block and "9" in block and valid:
    valid=True
else:
    valid=False

if valid:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
