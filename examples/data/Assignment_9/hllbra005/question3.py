# program checking accuracy of sudoku grid
# Brandon Hall (HLLBRA005)
# 16/05/2014



sudoku=[] #creates grid 

for i in range(9):
    sudoku.append(input(""))
for i in range(9):
    sudoku[i]= " ".join(sudoku[i])
    sudoku[i] = list(sudoku[i].split(" "))
    
k=0
#Checks vertical direction if equal across whole grid
for row in range(9):
    compare=[] 
    for col in range(9):
        if not((sudoku[row][col])in compare):

            compare.append(sudoku[row][col])
        else:
            k = k+1

            break

#Checks horizontal direction if equal across grid
for row in range(9):
    compare=[] 
    for col in range(9):
        if not((sudoku[col][row])in compare):

            compare.append(sudoku[col][row])
        else:
            k = k+1
            break
#If 'small' 3x3 blocks are equal:
for i in range(3):
    for j in range(3):
        for a in range(i,i+3):
            compare=[]
            for b in range(j,j+3):
                if not((sudoku[a][b])in compare):
                    compare.append(sudoku[a][b])
                else:
                    k = k+1
                    break
      #If K is zero, then none of the 'else' clauses have been accessed.
      #Therefore grid should be valid
if k==0:
    print("Sudoku grid is valid")
    #if k is not = 0. then grid cannot be valid as an earlier 'else' caluse was accessed. 
else:
    print("Sudoku grid is not valid")