#Author: NLXALE001
#Date: 13 May 2014
#Assignment 9


#separate input into rows
rows = []
for i in range (9):
    rows.append(input(""))

valid = True
while valid == True:
    #check rows
    for i in range (9):
        for j in range (1, 10):
            row = rows[i]
            if row.find(str(j)) == -1:
                valid = False
    #check columns
    for i in range (1, 10):
        for j in range (9):
            row = rows[j]
            if row.find(str(i)) == -1:
                valid = False
                
    #check blocks
    blocks = ["", "", "", "", "", "", "", "", ""]
    #split sudoku into blocks
    for i in range (0,3):
        row = rows[i]
        blocks[0] += row[0:3]
        blocks[1] += row[3:6]
        blocks[2] += row[6:9] 
    for i in range (3,6):
        row = rows[i]
        blocks[3] += row[0:3]
        blocks[4] += row[3:6]
        blocks[5] += row[6:9]     
    for i in range (6, 9):
        row = rows[i]
        blocks[6] += row[0:3]
        blocks[7] += row[3:6]
        blocks[8] += row[6:9]
    #check if each block is valid
    for i in range (9):
        for j in range (1, 10):
            block = blocks[i]
            if block.find(str(j)) == -1:
                valid = False
        
    
#print out validity message 
if valid == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")


