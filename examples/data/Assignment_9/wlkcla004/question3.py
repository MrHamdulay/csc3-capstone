"""question 3
clare walker 
12 may 2014"""

#addd inputs to 2 d array
grid=[]
for i in range(9):
    line=input("")
    linelist=[]
    for number in line:
        linelist.append(eval(number))
    grid.append(linelist)
# runs through each row (item in the list) to check for duplicates
validRows=True   
for row in range(9):
    values=grid[row]
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            else:
                if values[i]==values[j]:
                    validRows=False
# runs through columns (items in each list that share the same index) to check for duplicates
validCols=True
for col in range(9):
    values=[]
    for row in range(9):
        values.append(grid[row][col])
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            if values[i]==values[j]:
                validCols=False
                
validBlock=True
# following pieces of code run through the 9 not-overlapping block to check for duplicates
#first part creates list containing all values in block
values1=[]
for row in range(3):
    for col in range(3):
        values1.append(grid[row][col])
# second part checks for duplicates
for i in range(9):
    for j in range(9):
        if i ==j:
            continue
        if values1[i]==values1[j]:
            validBlock=False


values2=[]
for row in range(3):
    for col in range(3,6):
        values2.append(grid[row][col])

for i in range(9):
    for j in range(9):
        if i ==j:
            continue
        if values2[i]==values2[j]:
            validBlock=False

values3=[]
for row in range(3):
    for col in range(6,9):
        values3.append(grid[row][col])

for i in range(9):
    for j in range(9):
        if i ==j:
            continue
        if values3[i]==values3[j]:
            validBlock=False

values4=[]
for row in range(3,6):
    for col in range(3):
        values4.append(grid[row][col])

for i in range(9):
    for j in range(9):
        if i ==j:
            continue
        if values4[i]==values4[j]:
            validBlock=False

values5=[]
for row in range(3,6):
    for col in range(3,6):
        values5.append(grid[row][col])

for i in range(9):
    for j in range(9):
        if i ==j:
            continue
        if values5[i]==values5[j]:
            validBlock=False

values6=[]
for row in range(3,6):
    for col in range(6,9):
        values6.append(grid[row][col])

for i in range(9):
    for j in range(9):
        if i ==j:
            continue
        if values6[i]==values6[j]:
            validBlock=False
            
            
values7=[]
for row in range(6,9):
    for col in range(3):
        values7.append(grid[row][col])

for i in range(9):
    for j in range(9):
        if i ==j:
            continue
        if values7[i]==values7[j]:
            validBlock=False
            
values8=[]
for row in range(6,9):
    for col in range(3,6):
        values8.append(grid[row][col])

for i in range(9):
    for j in range(9):
        if i ==j:
            continue
        if values8[i]==values8[j]:
            validBlock=False

values9=[]
for row in range(6,9):
    for col in range(6,9):
        values9.append(grid[row][col])

for i in range(9):
    for j in range(9):
        if i ==j:
            continue
        if values9[i]==values9[j]:
            validBlock=False
# if any above code encounters a duplicate, the corresponding variable will be given a False boolean value

# if this has not happen (thus no duplicates found), print valid
if validBlock and validRows and validCols:
    print("Sudoku grid is valid")
#if not some duplicate has been found and grid is not valid
else:
    print("Sudoku grid is not valid")
    