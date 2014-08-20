'''Dumisani Ngwenza
NGWDUM005
11/05/2014
Assignment 9 Question 3'''

#create a 9x9 2-D array 
sudoku = []
for i in range(9):
    sudoku.append([0]*9)

#populating the 1st row
line = input()
increment = 0
pos = 0
while increment < 9:
    sudoku[0][increment] = int((line[pos]))
    pos += 1
    increment += 1

#populating 2nd row
line = input()
increment = 0
pos = 0
while increment < 9:
    sudoku[1][increment] = int(line[pos])
    pos += 1
    increment += 1

#populating the 3rd row
line = input()
increment = 0
pos = 0
while increment < 9:
    sudoku[2][increment] = int(line[pos])
    pos += 1
    increment += 1

#populating the 4th row
line = input()
increment = 0
pos = 0
while increment < 9:
    sudoku[3][increment] = int(line[pos])
    pos += 1
    increment += 1

#populating the 5th row
line = input()
increment = 0
pos = 0
while increment < 9:
    sudoku[4][increment] = int(line[pos])
    pos += 1
    increment += 1

#populating the 6th row
line = input()
increment = 0
pos = 0
while increment < 9:
    sudoku[5][increment] = int(line[pos])
    pos += 1
    increment += 1

#populating the 7th row
line = input()
increment = 0
pos = 0
while increment < 9:
    sudoku[6][increment] = int(line[pos])
    pos += 1
    increment += 1

#populating the 8th row
line = input()
increment = 0
pos = 0
while increment < 9:
    sudoku[7][increment] = int(line[pos])
    pos += 1
    increment += 1

#populating the 9th row
line = input()
increment = 0
pos = 0
while increment < 9:
    sudoku[8][increment] = int(line[pos])
    pos += 1
    increment += 1

#checks if there is any number in same row is the same
def row_valid():
    global sudoku
    
    for i in range(9):
        for col in range(9):
            counter = sudoku[i].count(sudoku[i][col])
            if counter > 1:
                return False
        else:
            return True
            
#checks if same column has same value
def col_valid():
    global sudoku
    line = ""
    for row in range(9):
        for col in range(9):
            line += str(sudoku[col][row])
    
    for i in range(0,81,9):
        number = line[i]
        string = line[i:i+9]
        if string.count(number)>1:
            return False
        else:
            return True    

#checks whether the blocks are valid
def block_valid():
    global sudoku
    block=""    
    for i in range(0,9,3):
        for j in range(i,i+3):
            for k in range(3):
                block+=str(sudoku[j][k])
        
        for j in range(i,i+3):
            for k in range(3,6):
                block+=str(sudoku[j][k])
       
        for j in range(i,i+3):
            for k in range(6,9):
                block+= str(sudoku[j][k])
    
    for i in range(0,27,9):
        number = block[i]
        string = block[i:i+9]
        if string.count(number)>1:
            return False 
        else:
            return True
      
if col_valid() is True and row_valid() is True and block_valid() is True:
    print ('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')
#print (row_valid())