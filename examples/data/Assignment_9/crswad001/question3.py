'''Wade Cresswell
Question3'''
lists =[]
for i in range(9):
    lists.append(input()) #add inputs to a list with each line in a different element
flag = True
for t in range (9): #test for across to see if there are no duplicates
    for i in range(9):
        for z in range(9):
            if i!=z:    
                if lists[t][i]==lists[t][z]:
                    flag=False
for t in range (9): #test for down to see if there are no duplicates
    for i in range(9):
        for z in range(9):
            if i!=z:    
                if lists[i][t]==lists[z][t]:
                    flag=False
for x in range(3,10,3): #check the first 3 sub 9x9 grids to see if they contain all 1-9 numbers
    es=''
    for i in range(3):
        es+= lists[i][x-3:x]
    for z in range(1,10):
        if str(z) not in es: #if 1-9 are not in grid, flag variable is false
            flag = False          
for x in range(3,10,3): #check the second 3 sub 9x9 grids to see if they contain all 1-9 numbers
    es=''
    for i in range(3,6):
        es+= lists[i][x-3:x]
    for z in range(1,10):
        if str(z) not in es: #if 1-9 are not in grid, flag variable is false
            flag = False
for x in range(3,10,3): #check the last 3 sub 9x9 grids to see if they contain all 1-9 numbers
    es=''
    for i in range(6,9):
        es+= lists[i][x-3:x]
    for z in range(1,10):
        if str(z) not in es: #if 1-9 are not in grid, flag variable is false
            flag = False 
if flag == False: #if the grid is not valid, say so, otherwise say valid.
    print('Sudoku grid is not valid')
else:
    print('Sudoku grid is valid')