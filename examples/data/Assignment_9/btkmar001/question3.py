rowstrings=[[],[],[],[],[],[],[],[],[]] # List template
control = 0
while True: # Gather 9 lines of input from user
    a = input("")
    control+=1 # Counts the iterations
    for number in range(len(a)):
        rowstrings[control-1].append(a[number]) # Store input in a 2D list, sorted in horizontal rows
    if control ==9:
        break        

columnstrings = [[],[],[],[],[],[],[],[],[]] # Sorts input into columns 
for column in range(len(rowstrings[0])):
    for row in range(len(rowstrings)):
        columnstrings[column].append(rowstrings[row][column])

gridstrings = [[],[],[],[],[],[],[],[],[]]
for row in range(len(rowstrings)): # Sorts input into respective 3x3 grids
    if row <= 2:
        for column in range(len(rowstrings[row])):
            if column <=2:
                gridstrings[0].append(rowstrings[row][column])
            elif 2 < column <= 5:
                gridstrings[1].append(rowstrings[row][column])
            elif 5 < column <= 8:
                gridstrings[2].append(rowstrings[row][column])
    elif 2 < row <= 5:
        for column in range(len(rowstrings[row])):
            if column <=2:
                gridstrings[3].append(rowstrings[row][column])
            elif 2 < column <= 5:
                gridstrings[4].append(rowstrings[row][column])
            elif 5 < column <= 8:
                gridstrings[5].append(rowstrings[row][column])
    elif 5 < row <= 8:
        for column in range(len(rowstrings[row])):
            if column <=2:
                gridstrings[6].append(rowstrings[row][column])
            elif 2 < column <= 5:
                gridstrings[7].append(rowstrings[row][column])
            elif 5 < column <= 8:
                gridstrings[8].append(rowstrings[row][column])        
     
def check(s,l):
    """A funtion that checks for recurrences in lists or strings using recursion"""
    if len(s)==1:
        if s[0] in l:
            return False
        else:
            return True
    else:
        if s[0] in l:
            return False
        else:
            l.append(s[0])
            return check(s[1:],l)

for row in range(9): # Check for recurences in every row column and grid
    if not check(rowstrings[row],[]) or not check(columnstrings[row],[]) or not check(gridstrings[row],[]):
        x = False
        break
    else:
        x = True

if x:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
    
    