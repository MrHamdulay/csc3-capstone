"""Check if sudoku grid is valid
Emmnauel Conradie
16 May 2014"""

#Sudoku grid input
s1 = input()
s2 = input()
s3 = input()
s4 = input()
s5 = input()
s6 = input()
s7 = input()
s8 = input()
s9 = input()

#Temp grid
grid = []

#New grid
s = []

#Append input to grid
grid.append(s1)
grid.append(s2)
grid.append(s3)
grid.append(s4)
grid.append(s5)
grid.append(s6)
grid.append(s7)
grid.append(s8)
grid.append(s9)

#Create new grid
for i in range(9):
    s.append([]*9)

#Import numbers to new grid
for i in str(grid[0]):
    s[0].append(i)
    
for i in str(grid[1]):
    s[1].append(i)

for i in str(grid[2]):
    s[2].append(i)
    
for i in str(grid[3]):
    s[3].append(i)    
    
for i in str(grid[4]):
    s[4].append(i)    

for i in str(grid[5]):
    s[5].append(i)
    
for i in str(grid[6]):
    s[6].append(i) 
    
for i in str(grid[7]):
    s[7].append(i)    
    
for i in str(grid[8]):
    s[8].append(i)    
    
#Check for repitition in rows
for i in s:
    row = i
    for j in row:
        y = row.count(j)
        z = 0 
        if y > 1:
            z += 1   
        else:
            x = 1       

#Check for repitition in columns
t = zip(*s)
for i in t:
    col = i
    for j in col:
        w = col.count(j)
        m = 0 
        if w > 1:
            m += 1   
        else:
            v = 1                  

#Print validity
    if z == 0 and m == 0:
        #print (s1)
        #print (s2)
        #print (s3)
        #print (s4)
        #print (s5)
        #print (s6)
        #print (s7)
        #print (s8)
        #print (s9)
        print ("Sudoku grid is valid")
        break
    else:
        #print (s1)
        #print (s2)
        #print (s3)
        #print (s4)
        #print (s5)
        #print (s6)
        #print (s7)
        #print (s8)
        #print (s9)        
        print ("Sudoku grid is not valid")
        break