#Shaylan Lalloo
#15/05/2014
#Check if sudoku grid is valid


mygrid = []

for i in range(9):
    tmp = []
    x = input()
    for j in x:
        tmp.append(j)
    mygrid.append(tmp)
#read in grid

valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#a to check grid

def crows():
    for i in mygrid:
        x = i + [0,]
        #take row but so that it doesn't alter grid when changed
        x.pop()
        x.sort()
        #sort
        if x != valid:
            return False
        #if same as valid then it's valid otherwise it's not
    return True

def ccols():
    for i in range(9):
        tmp = []
        for j in range(9):
            tmp.append(mygrid[j][i])
            #fetch columns and put them in array
        tmp.sort()
        if tmp != valid:
            return False
        #compare to valid array again
    return True

def cblocks():
    mynums = []
    for i in range(9):
        mynums.append([])
    for i in range(9):
        for j in range(9):
            if 0 <= i % 9 < 3 and 0 <= j % 9 < 3:
                mynums[0].append(mygrid[i][j])
            elif 3 <= i % 9 < 6 and 0 <= j % 9 < 3:
                mynums[1].append(mygrid[i][j])
            elif 6 <= i % 9 < 9 and 0 <= j % 9 < 3:
                mynums[2].append(mygrid[i][j])
            elif 0 <= i % 9 < 3 and 3 <= j % 9 < 6:
                mynums[3].append(mygrid[i][j])
            elif 3 <= i % 9 < 6 and 3 <= j % 9 < 6:
                mynums[4].append(mygrid[i][j])
            elif 6 <= i % 9 < 9 and 3 <= j % 9 < 6:
                mynums[5].append(mygrid[i][j])
            elif 0 <= i % 9 < 3 and 6 <= j % 9 < 9:
                mynums[6].append(mygrid[i][j])
            elif 3 <= i % 9 < 6 and 6 <= j % 9 < 9:
                mynums[7].append(mygrid[i][j])
            elif 6 <= i % 9 < 9 and 6 <= j % 9 < 9:
                mynums[8].append(mygrid[i][j])
    #read all numbers and run through cases of which block it's in
    for i in range(len(mynums)):
        mynums[i].sort()
        if mynums[i] != valid:
            return False
        #check if each block is valid
    return True
        
if cblocks() and crows() and ccols():
    print('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')
#if all are valid then the grid is valid otherwise it's not
