'''Daniel Feinstein FNSDAN001
Assignment 9
Check for valid soduko grid
'''
#initialisation
lines = [[],[],[],[],[],[],[],[],[]]
col = [[],[],[],[],[],[],[],[],[]]
tgrid = [[],[],[],[],[],[],[],[],[]]
#populate
for i in range(9):
    line = input()
    for j in range(9):
        lines[i].append(line[j])

#set cnt = 0
cnt = 0

#check rows
for line in lines:
    if sorted(line) != ['1','2','3','4','5','6','7','8','9']:
        cnt +=1
        break

        
#check columns
for i in range(9):
    
    for j in range(9):
        col[i].append(lines[j][i])
for line in col:
    if sorted(line) != ['1','2','3','4','5','6','7','8','9']:
        cnt +=1
        break
    
#check 3x3 grids
for i in range(3):
    for j in range(9):
        if j<=2:  
            tgrid[0].append(lines[i][j])
        elif  j>2 and j<6:
            tgrid[1].append(lines[i][j])
        elif 5<j:
            tgrid[2].append(lines[i][j])
for i in range(3,6):
    for j in range(9):
        if j<=2:  
            tgrid[3].append(lines[i][j])
        elif  j>2 and j<6:
            tgrid[4].append(lines[i][j])
        elif 5<j:
            tgrid[5].append(lines[i][j])
for i in range(6,9):
    for j in range(9):
        if j<=2:  
            tgrid[6].append(lines[i][j])
        elif  j>2 and j<6:
            tgrid[7].append(lines[i][j])
        elif 5<j:
            tgrid[8].append(lines[i][j])


for i in tgrid:
    if sorted(i) !=['1','2','3','4','5','6','7','8','9']:
        cnt+=1
        break



if cnt==0:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
        





