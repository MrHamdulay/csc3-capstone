#Azhar Aboobaker
#ABBAZH001
#13/05/2014

lines = []
space = ""
no = "no"
yes = "yes"
a = 0
while len(lines) < 9:
    lines.append(input())

for i in range(9):
    if str(i+1) in lines[i]:
        no = "yes"

for j in range(9):
    if yes == "yes":
        for x in range(9):
            space += lines[x][j]

        for y in range(1,10):
            if str(y) in space:
                yes = "yes"
            else:
                yes = "no"
                break
    space = ""
    
    if yes == "no":
        break

if (no == "yes" and yes == "yes"):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")






   
    










