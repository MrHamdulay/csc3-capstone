
lines = []
placeholder = ''
proceed1 = 'no'
proceed2 = 'yes'
ph = 0
while len(lines) < 9:
    lines.append(input())

for i in range(9):
    if str(i+1) in lines[i]:
        proceed1 = 'yes'

for j in range(9):
    if proceed2 == 'yes':
        for k in range(9):
            placeholder += lines[k][j]

        for p in range(1,10):
            if str(p) in placeholder:
                proceed2 = 'yes'
            else:
                proceed2 = 'no'
                break
    placeholder = ''
    
    if proceed2 == 'no':
        break

if (proceed1 == 'yes' and proceed2 == 'yes'):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")






   
    










