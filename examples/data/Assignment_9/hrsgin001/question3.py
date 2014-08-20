#Question 3, Assignment 9
#Gina Horscroft
#10.05.2014

total = 0
for a in range(9):
    for i in range(1, 10):
        total += ord(str(i))

totalNine = 0
for a in range(1, 10):
    totalNine +=ord(str(a))

sudoku = True 

grid = []
for i in range(9):
    st1 = input()
    grid.append(st1)

sudokutotal = 0    
#calculate ord of sudoku
for a in range(9):
    temp = grid[a]
    for b in range(9):
        sudokutotal+= ord(temp[b])
        
if total != sudokutotal:
    sudoku = False
  
for a in range (9):
    temp = grid[a]
    for b in range(1, 9):
        #checks in row for duplicates
        if temp[0] == temp[b]:
            sudoku = False
        
#checks columns for duplicates 
column = grid[0]
for a in range (9):
    for b in range(1, 9):
        tempg = grid[b]
        if column[a] == tempg[a]:
            sudoku == False
            
#could be much more elegant solution but in a hurry because I have 6 test to study for
g2 = []
st = ""
for a in range(3):
    temp = grid[a]
    st += temp[0:3]
g2.append(st)
st = ""
for a in range(3,6):
    temp = grid[a]
    st += temp[0:3]
g2.append(st)
st = ""
for a in range(6,9):
    temp = grid[a]
    st += temp[0:3]
g2.append(st)
st = ""
for a in range(3):
    temp = grid[a]
    st += temp[3:6]
g2.append(st)
st = ""
for a in range(3,6):
    temp = grid[a]
    st += temp[3:6]
g2.append(st)
st = ""
for a in range(6,9):
    temp = grid[a]
    st += temp[3:6]
g2.append(st)
st = ""
for a in range(3):
    temp = grid[a]
    st += temp[6:9]
g2.append(st)
st = ""
for a in range(3,6):
    temp = grid[a]
    st += temp[6:9]
g2.append(st)
st = ""
for a in range(6,9):
    temp = grid[a]
    st += temp[6:9]
g2.append(st)

#check to see if duplicates in block
for i in range(len(g2)):
    temp = g2[i]
    tottemp = 0
    for a in range(len(temp)):
        tottemp+=ord(temp[a])
    if tottemp != totalNine:#must be a duplicate value
        sudoku = False
        break
        
if sudoku == True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
        
"""SIMPLE WAY TO CHECK FOR DUPLICATES:
in sudoku there should be 9 sets of 9 different numbers.
The ord() value of every TRUE sudoku is the same, therefore if the ord value is too high or too low, there is a duplicate skewing the data"""