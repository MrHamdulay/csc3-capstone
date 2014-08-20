#Darryl Gounden
#11/05/14
#Checks if a sudoku grid is correct or not

import sys
sys.setrecursionlimit (30000)

grid = []

for i in range(9):
    row = input("")
    row_new = []
    for j in range(9):
        row_new.append(row[j])
    grid.append(row_new)


#_____________________________________________________#

#Checks each row for like numbers
def check_one_row(row):
    global i #My counter, so I know what index of the list I'm passing through the function. 
    global grid 

    if len(row) == 1: #If the length of the row I pass into the function is = 1, skip to the next row.
        i += 1 #Adds 1 to my counter every time I'm done with a row.
        if i<9: #9 is the cutoff because the last row index will be 8, but I added 1 to it above.
            return check_one_row(grid[i]) #Calls the function with the next row.
        else:
            return True #If it has gone through the entire grid and no like numbers are in a column, first test passed.
        
    else:
        for j in range(1,len(row)): #Start with index 1 because I'm using index 0 to compare. Go up to the end of the row.
        
            if row[0] == row[j]: #If like numbers are found in a row, test failed.
                return False
        
        return check_one_row(row[1:]) #Returns the same row but leaves out index 0 because we have already compared it above.
                                      #Therefore passing in a smaller form of the row until it reaches sentinel length, 1.
    return True
i = 0
row_ans = check_one_row(grid[i])

#The same method is used for every other "Check" function.

#_____________________________________________________#


#_____________________________________________________#

#Making a list of the columns
inv_grid = [[],[],[],[],[],[],[],[],[]]

for k in range(9):
    for j in range(9):
        inv_grid[k].append(grid[j][k])

#_____________________________________________________#

#_____________________________________________________#

#Checks each column for like numbers
def check_one_column(col):
    global c 
    global inv_grid

    if len(col) == 1:
        c += 1
        if c<9:
            return check_one_column(inv_grid[c])
        else:
            return True
        
    else:
        for j in range(1,len(col)):
        
            if col[0] == col[j]:
                return False
        
        return check_one_column(col[1:])
    
    return True

c = 0

col_ans = check_one_column(inv_grid[c])

#_____________________________________________________#

#_____________________________________________________#
#Transforms the grid into a list of blocks starting at the top left hand corner.
block = [[],[],[],[],[],[],[],[],[]]
x = 0
p = 0 #Starts with the block position at the left.
q = 0 #Starts with the block position at the top.

#Makes a list of the 9x9 blocks from top left. Going left.
def create_blocks(grid):
    global x
    global p
    global q
    
    for i in range(p,p+3):
        
        for j in range(q,q+3):
            block[x].append(grid[i][j]) #Adds to the respective index of block.
            
    q += 3
    x += 1
    
    if q == 9:
        q = 0 #Brings the block position back to the left.
        p += 3 #Moves the block position down.
        
    if x == 9:
        return block
    
    return create_blocks(grid) #Calls the function again with the block position shifted 3 right.
                               #After it lists the top 3 blocks, shiftsblock position 3 down.
BLOCKS = create_blocks(grid)

#Checks for like numbers in each block
def check_blocks(block):
    global y 
    global BLOCKS

    if len(block) == 1:
        y += 1
        if y<9:
            return check_blocks(BLOCKS[y])
        else:
            return True
        
    else:
        for j in range(1,len(block)):
        
            if block[0] == block[j]:
                return False
        
        return check_blocks(block[1:])
    
    return True

y = 0

block_ans = check_blocks(BLOCKS[y])

#_____________________________________________________#


#Checks if all 3 checks are passed. If so, the grid is valid.
if row_ans == True and col_ans == True and block_ans == True:
    print("Sudoku grid is valid")
    
else:
    print("Sudoku grid is not valid")