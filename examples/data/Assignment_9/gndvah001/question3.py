"""sodoku checker
Vahin Gounden
14/05/14"""

#create lists
lst = []
lst2 = []
lst3 = []

#loop over input and add items to lst
lst = []
for i in range (9):
    x = input()
    lst.append (x)

#split items into the individual lists, ie create 2d array    
for i in range (len(lst)):
    x = lst[i].split ()
    lst2.append (x)
    
#break lines into individual characters    
for w in range (len(lst2)):
    q = lst2[w][0]
    e = list(q)
    lst3.append (e)
    
#check rows
smr1 = 0
smr2 = 0
smr3 = 0
smr4 = 0
smr5 = 0
smr6 = 0
smr7 = 0
smr8 = 0
smr9 = 0
for l in range (len(lst3)):
    row1 = eval(lst3[0][l])
    smr1 = smr1 + row1
    row2 = eval(lst3[1][l])
    smr2 = smr2 + row2
    row3 = eval(lst3[2][l])
    smr3 = smr3 + row3
    row4 = eval(lst3[3][l])
    smr4 = smr4 + row4
    row5 = eval(lst3[4][l])
    smr5 = smr5 + row5
    row6 = eval(lst3[5][l])
    smr6 = smr6 + row6
    row7 = eval(lst3[6][l])
    smr7 = smr7 + row7
    row8 = eval(lst3[7][l])
    smr8 = smr8 + row8
    row9 = eval(lst3[8][l])
    smr9 = smr9 + row9

if smr1 != 45 or smr2 != 45 or smr3 != 45 or smr4 != 45 or smr5 != 45 or smr6 != 45 or smr7 != 45 or smr8 != 45 or smr9 != 45:
    validrow = "false"
elif smr1 == 45 and smr2 == 45 and smr3 == 45 and smr4 == 45 and smr5 == 45 and smr6 == 45 and smr7 == 45 and smr8 == 45 and smr9 == 45:
    validrow = "true"
    
#check columns for duplicates
smc1 = 0
smc2 = 0
smc3 = 0
smc4 = 0
smc5 = 0
smc6 = 0
smc7 = 0
smc8 = 0
smc9 = 0
for p in range (len(lst3)):
    col1 = eval(lst3[p][0])
    smc1 = smc1 + col1
    col2 = eval(lst3[p][1])
    smc2 = smc2 + col2
    col3 = eval(lst3[p][2])
    smc3 = smc3 + col3
    col4 = eval(lst3[p][3])
    smc4 = smc4 + col4
    col5 = eval(lst3[p][4])
    smc5 = smc5 + col5
    col6 = eval(lst3[p][5])
    smc6 = smc6 + col6
    col7 = eval(lst3[p][6])
    smc7 = smc7 + col7
    col8 = eval(lst3[p][7])
    smc8 = smc8 + col8
    col9 = eval(lst3[p][8])
    smc9 = smc9 + col9

if smc1 != 45 or smc2 != 45 or smc3 != 45 or smc4 != 45 or smc5 != 45 or smc6 != 45 or smc7 != 45 or smc8 != 45 or smc9 != 45:
    validcol = "false"
elif smc1 == 45 and smc2 == 45 and smc3 == 45 and smc4 == 45 and smc5 == 45 and smc6 == 45 and smc7 == 45 and smc8 == 45 and smc9 == 45:
    validcol = "true"
    
#check 3x3 box
#box 1
smb1 = 0
for o in range (3):
    for p in range (3):
        box1 = eval(lst3[o][p])
        smb1 = smb1 + box1
#box 2
smb2 = 0
for o1 in range (3):
    for p1 in range (3,6):
        box2 = eval(lst3[o1][p1])
        smb2 = smb2 + box2
#box 3  
smb3 = 0
for o2 in range (3):
    for p2 in range (6,9):
        box3 = eval(lst3[o2][p2])
        smb3 = smb3 + box3
#box 4
smb4 = 0
for o3 in range (3):
    for p3 in range (3):
        box4 = eval(lst3[o3][p3])
        smb4 = smb4 + box4
#box 5
smb5 = 0
for o4 in range (3):
    for p4 in range (3,6):
        box5 = eval(lst3[o4][p4])
        smb5 = smb5 + box5
#box 6        
smb6 = 0
for o5 in range (3):
    for p5 in range (6,9):
        box6 = eval(lst3[o5][p5])
        smb6 = smb6 + box6
#box 7        
smb7 = 0
for o6 in range (3):
    for p6 in range (3):
        box7 = eval(lst3[o6][p6])
        smb7 = smb7 + box7
#box 8
smb8 = 0
for o7 in range (3):
    for p7 in range (3,6):
        box8 = eval(lst3[o7][p7])
        smb8 = smb8 + box8
#box 9  
smb9 = 0
for o8 in range (3):
    for p8 in range (6,9):
        box9 = eval(lst3[o8][p8])
        smb9 = smb9 + box9
        
if smb1 != 45 or smb2 != 45 or smb3 != 45 or smb4 != 45 or smb5 != 45 or smb6 != 45 or smb7 != 45 or smb8 != 45 or smb9 != 45:
    validbox = "false"
elif smb1 == 45 and smb2 == 45 and smb3 == 45 and smb4 == 45 and smb5 == 45 and smb6 == 45 and smb7 == 45 and smb8 == 45 and smb9 == 45:
    validbox = "true"

#decide if grid is valid or not    
if validrow == "true" and validcol == "true" and validbox == "true":
    print("Sudoku grid is valid")
elif validrow == "false" or validcol == "false" or validbox == "false":
    print("Sudoku grid is not valid")