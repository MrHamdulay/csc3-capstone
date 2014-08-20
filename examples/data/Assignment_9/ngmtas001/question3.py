#NGMTAS001
#Question3
#Tase Ngambi


def FindDuplicates(in_list):
    unique = set(in_list)
    if len(unique) == len(in_list):
        return False
    else:
        return True     
             
      
grid = []

#initialise the grid
for i in range (9):
     grid.append ([0] * 9)

#stroing into a 2D     
for x in range(9):
     line = input()
     for k in range(9):
          grid[x][k] = line[k]
          
isValid = True


#find duplicates in rows
for k in range(9):
    if FindDuplicates(grid[k]) == True:
        isValid = False

column = []                
#find duplicates in columns    

for k in range(9):
    tmp = ""
    for x in range(9):
        tmp = tmp + grid[x][k]
    column.append(tmp)

for k in range(9):
    if FindDuplicates(column[k]) == True:
        isValid = False
        
#No 2 cells in 3x3 grid
grid3by3 = []

#1
tmp = ""
for x in range(3):
    for k in range(3):
        tmp = tmp+grid[x][k]
grid3by3.append(tmp)


#2
tmp = ""
for x in range(3,6):
    for k in range(3):
        tmp = tmp+grid[x][k]
grid3by3.append(tmp)

#3
tmp = ""
for x in range(6,9):
    for k in range(3):
        tmp = tmp+grid[x][k]
grid3by3.append(tmp)

#4
tmp = ""
for x in range(3):
    for k in range(3,6):
        tmp = tmp+grid[x][k]
grid3by3.append(tmp)

#5
tmp = ""
for x in range(3):
    for k in range(6,9):
        tmp = tmp+grid[x][k]
grid3by3.append(tmp)

#6
tmp = ""
for x in range(3,6):
    for k in range(3,6):
        tmp = tmp+grid[x][k]
grid3by3.append(tmp)

#7
tmp = ""
for x in range(6,9):
    for k in range(3,6):
        tmp = tmp+grid[x][k]
grid3by3.append(tmp)


#8
tmp = ""
for x in range(6,9):
    for k in range(6,9):
        tmp = tmp+grid[x][k]
grid3by3.append(tmp)


#9
tmp = ""
for x in range(3,6):
    for k in range(6,9):
        tmp = tmp+grid[x][k]
grid3by3.append(tmp)

for k in range(9):
    if FindDuplicates(grid3by3[k]) == True:
        isValid = False


if isValid ==True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
          
          
    
    
    
    