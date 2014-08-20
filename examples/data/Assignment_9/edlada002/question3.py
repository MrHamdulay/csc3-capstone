"""Assignment 9 Question3 
Adam Edelberg"""


sudoku = []
valid = 0

for i in range (9):
    sudoku.append([0])
    sudoku[i]=[0]*9
    s=input('')
    for j in range (9):
        sudoku[i][j]=s[j:j+1]

for i in range(3):
    for j in range(3):
        for a in range(i,i+3):
            temp=[]
            for b in range(j,j+3):
                if not((sudoku[a][b])in temp):
                    temp.append(sudoku[a][b])
                else:
                    valid += 1
                    break
           
for row in range(9):
    temp=[] 
    for col in range(9):
        if not((sudoku[row][col])in temp):
            
            temp.append(sudoku[row][col])
        else:
            valid += 1
            break
            
for row in range(9):
    temp=[] 
    for col in range(9):
        if not((sudoku[col][row])in temp):
            
            temp.append(sudoku[col][row])
        else:
            valid += 1

            break
        
        
        

    

if valid>1:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")
