#Riya Desai
#Assignment 9 - Question 3
#15 May 2014



sudokugame = [ ]

check = True

#keep adding numbers to the grid
for i in range(9):
    sudokugame.append(input())

grid = [ ]


for i in range(9):
    grid.append(sudokugame[i][0:3])

for i in range(9):
    grid.append(sudokugame[i][3:6])

for i in range(9):
    grid.append(sudokugame[i][6:9])

#set i = 0 
i=0



while(i<len(grid)):
    grid[i]=grid[i]+grid[i+1]+grid[i+2]
    grid.remove(grid[i+1])
    grid.remove(grid[i+1])
    i=i+1

#create the colums of the sudokugame
columns = [[],[],[],[],[],[],[],[],[]]


#add numbers to the grid (max 9)
for i in range(9):
    for j in range(9):
        columns[i].append(sudokugame[j][i])


#find all conditions where grid is NOT valid
for i in range(9):
    for j in range(9):
        if(grid[i].index(grid[i][j])!=j):
           check= False


for i in range(9):
    for j in range(9):
        if(columns[i].index(columns[i][j])!=j):
            check=False


for i in range(9):
    for j in range(9):
        if(sudokugame[i].index(sudokugame[i][j])!=j):
            check=False

#print statements relating to the "check" to see whether grid was valid or not
if(check):
    print("Sudoku grid is valid")


else:
    print("Sudoku grid is not valid")