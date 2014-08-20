#Sandisha Budhal
#16/05/2014
#Program to check if a complete Sudoku grid is valid or not.

new_lis = [ ] #creating an empty list
F = True #setting the flag to be true
for a in range(9):
    new_lis.append(input())
grd = [ ]  #creating an empty list for the grid

for a in range(9):   #appending the grid
    grd.append(new_lis[a][0:3])
for a in range(9):
    grd.append(new_lis[a][3:6])
for a in range(9):
    grd.append(new_lis[a][6:9])
a=0  #setting the value of a to be 0
while(a<len(grd)):
    grd[a]=grd[a]+grd[a+1]+grd[a+2]
    grd.remove(grd[a+1])
    grd.remove(grd[a+1])
    a=a+1

column = [[],[],[],[],[],[],[],[],[]] #creating a new list
for a in range(9):
    for b in range(9):
        column[a].append(new_lis[b][a]) #appending the new list names column
for a in range(9):
    for b in range(9):
        if(grd[a].index(grd[a][b])!=b):
          F=False #the flag is false if the above condition is met
for a in range(9):
    for b in range(9):
        if(column[a].index(column[a][b])!=b):
            F=False #if the above condition is met the flag will be false
for a in range(9):
    for b in range(9):
        if(new_lis[a].index(new_lis[a][b])!=b):
            F=False #the flag is false if the above condition is met
if(F):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")