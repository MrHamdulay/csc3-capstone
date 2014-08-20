# Maisha Ivha
# Program that checks if a sudoku square is valid or NOT
#26 May 2014


# Create empty list
lst = []
# Get input
for i in range(9):
    string = input()
    lst.append(string)

# Checked first(top left) grid1

string1 =''
for i in range(3):
    string1 = string1 + (lst[i][0:3])
    myset1 = set(string1)
if len(myset1) == 9:
    grid1 = 1
else:
    grid1 = 0

# middle top grid2

string2 =''
for i in range(3):
    string2 = string2 + (lst[i][3:6])
    myset2 = set(string2)
if len(myset2) == 9:
    grid2 = 1
else:
    grid2 = 0
    
# right top grid3

string3 =''
for i in range(3):
    string3 = string3 + (lst[i][6:9])
    myset3 = set(string3)
if len(myset3) == 9:
    grid3 = 1
else:
    grid3 = 0

# left middle grid4

string4 =''
k=3
for i in range(3):
    string4 = string4 + (lst[k][0:3])
    myset4 = set(string4)
    k+=1
if len(myset4) == 9:
    grid4 = 1
else:
    grid4 = 0

# middle middle grid5

string5 =''
k=3
for i in range(3):
    string5 = string5 + (lst[k][3:6])
    myset5 = set(string5)
    k+=1
if len(myset5) == 9:
    grid5 = 1
else:
    grid5 = 0
# right middle grid6

string6 =''
k=3
for i in range(3):
    string6 = string6 + (lst[k][6:9])
    myset6 = set(string6)
    k+=1
if len(myset6) == 9:
    grid6 = 1
else:
    grid6 = 0

# left bottom grid7

string7 =''
k=6
for i in range(3):
    string7 = string7 + (lst[k][0:3])
    myset7 = set(string7)
    k+=1
if len(myset7) == 9:
    grid7 = 1
else:
    grid7 = 0

# left bottom grid8
string8 =''
k=6
for i in range(3):
    string8 = string8 + (lst[k][0:3])
    myset8 = set(string8)
    k+=1
if len(myset8) == 9:
    grid8 = 1
else:
    grid8 = 0

# left bottom grid9
string9 =''
k=6
for i in range(3):
    string9 = string9 + (lst[k][0:3])
    myset9 = set(string9)
    k+=1
if len(myset9) == 9:
    grid9 = 1
else:
    grid9 = 0

#Get total of grids when true, gridnum = 1, therefore truegrids = 9
gridsum = (grid1 + grid2 + grid3 + grid4 + grid5 + grid6 + grid7 + grid8 + grid9)


# Testing Verticals:
# vertical 1
vert_string1 = ''

for i in range(9):
    vert_string1 = vert_string1 + ((lst[i][0]))
       
myvertset1 = set(vert_string1)
if len(myvertset1) == 9:
    v1 = 1
else:
    v1 = 0

# vertical 2
vert_string2 = ''

for i in range(9):
    vert_string2 = vert_string2 + ((lst[i][1]))
       
myvertset2 = set(vert_string2)
if len(myvertset2) == 9:
    v2 = 1
else:
    v2 = 0
    
# vertical 3
vert_string3 = ''

for i in range(9):
    vert_string3 = vert_string3 + ((lst[i][2]))
       
myvertset3 = set(vert_string3)
if len(myvertset3) == 9:
    v3 = 1
else:
    v3 = 0
    
# vertical 4
vert_string4 = ''

for i in range(9):
    vert_string4 = vert_string4 + ((lst[i][3]))
       
myvertset4 = set(vert_string4)
if len(myvertset4) == 9:
    v4 = 1
else:
    v4 = 0

# vertical 5
vert_string5 = ''

for i in range(9):
    vert_string5 = vert_string5 + ((lst[i][4]))
       
myvertset5 = set(vert_string5)
if len(myvertset5) == 9:
    v5 = 1
else:
    v5 = 0
    
# vertical 6
vert_string6 = ''

for i in range(9):
    vert_string6 = vert_string6 + ((lst[i][5]))
       
myvertset6 = set(vert_string6)
if len(myvertset6) == 9:
    v6 = 1
else:
    v6 = 0

# vertical 7
vert_string7 = ''

for i in range(9):
    vert_string7 = vert_string7 + ((lst[i][6]))
       
myvertset7 = set(vert_string7)
if len(myvertset7) == 9:
    v7 = 1
else:
    v7 = 0

# vertical 8
vert_string8 = ''

for i in range(9):
    vert_string8 = vert_string8 + ((lst[i][7]))
       
myvertset8 = set(vert_string8)
if len(myvertset8) == 9:
    v8 = 1
else:
    v8 = 0

# vertical 9
vert_string9 = ''

for i in range(9):
    vert_string9 = vert_string9 + ((lst[i][8]))
       
myvertset9 = set(vert_string9)
if len(myvertset9) == 9:
    v9 = 1
else:
    v9 = 0

# Find total of v, where vtotal for true v = 9
vtotal = (v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9)

    
# horizontal 1
hset1 = set(lst[0])
if len(hset1) == 9:
    h1 = 1
else:
    h1 = 0

# horizontal 2
hset2 = set(lst[1])
if len(hset2) == 9:
    h2 = 1
else:
    h2 = 0
    
# horizontal 3
hset3= set(lst[2])
if len(hset3) == 9:
    h3 = 1
else:
    h3 = 0
    
# horizontal 4
hset4= set(lst[3])
if len(hset4) == 9:
    h4 = 1
else:
    h4 = 0

# horizontal 5
hset5= set(lst[4])
if len(hset5) == 9:
    h5 = 1
else:
    h5 = 0

# horizontal 6
hset6= set(lst[5])
if len(hset6) == 9:
    h6 = 1
else:
    h6 = 0

# horizontal 7
hset7= set(lst[6])
if len(hset7) == 9:
    h7 = 1
else:
    h7 = 0

# horizontal 8
hset8= set(lst[7])
if len(hset8) == 9:
    h8 = 1
else:
    h8 = 0
    
# horizontal 9
hset9= set(lst[8])
if len(hset9) == 9:
    h9 = 1
else:
    h9 = 0
    
# Find htotal where htotal = 9 if true   
htotal = (h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9)

finaltotal = gridsum + vtotal + htotal

if finaltotal == 27:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
    
'''259716483
867345912
413928675
398574126
546281739
172639548
984163257
621857394
735492861'''