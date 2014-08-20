OneDim = []
TwoDim = []

for i in range (9):
    sudoku = input()
    for number in sudoku:
        OneDim.append(number)
for i in range (9):
    TwoDim.append(OneDim[(i*9):((i+1)*9)])

Row = ""

for i in range (9):
    Total = 0
    for item in TwoDim[i]:
        Total = Total + eval(item)
    if Total == 45 and Row != "-":
        Row = "+"
    else:
        Row = "-"

Column = ""

for i in range (9):
    Total2 = 0
    for a in range (9):
        Total2 = Total2 + eval(TwoDim[a][i])
    if Total2 == 45 and Column != "-":
        Column = "+"
    else:
        Column = "-"

Box = ""

for z in range (3):
    Total3 = 0
    for y in range (3):
        for x in range (3):
            Total3 = Total3 + eval(TwoDim[y+(z*3)][x])
    if Total3 == 45 and Box != "-":
        Box = "+"
    else:
        Box = "-"     
        
for z in range (3):
    Total3 = 0
    for y in range (3):
        for x in range (3):
            Total3 = Total3 + eval(TwoDim[y+(z*3)][x+3])
    if Total3 == 45 and Box != "-":
        Box = "+"
    else:
        Box = "-"
                
for z in range (3):
    Total3 = 0
    for y in range (3):
        for x in range (3):
            Total3 = Total3 + eval(TwoDim[y+(z*3)][x])
    if Total3 == 45 and Box != "-":
        Box = "+"
    else:
        Box = "-"        
            
if Row == "+" and Column == "+" and Box == "+" and TwoDim[0][0] != TwoDim[0][1]: 
    print ("Sudoku grid is valid")
            
else:
    print ("Sudoku grid is not valid")