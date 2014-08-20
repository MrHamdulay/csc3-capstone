'''sudoku checking for validity
Dudley Mutero
16/5/14'''

list1=[]
x=9
while x !=0:
    val=input()
    list1.append(val)
    x-=1
    
#vreating a 2d grid with height 9
grid=[]
for row in range (9):
    grid.append ([0]*9)

#reading input and inserting it into grid
templist1=[]
for i in list1:
    for j in range(9):
        templist1.append(eval(i[j]))
    del list1[0]    
    break
grid[0]=templist1
#reading input and inserting it into grid
templist1=[]
for i in list1:
    for j in range(9):
        templist1.append(eval(i[j]))
    del list1[0]    
    break
grid[1]=templist1
#reading input and inserting it into grid
templist1=[]
for i in list1:
    for j in range(9):
        templist1.append(eval(i[j]))
    del list1[0]    
    break
grid[2]=templist1
#reading input and inserting it into grid
templist1=[]
for i in list1:
    for j in range(9):
        templist1.append(eval(i[j]))
    del list1[0]    
    break
grid[3]=templist1

#reading input and inserting it into grid
templist1=[]
for i in list1:
    for j in range(9):
        templist1.append(eval(i[j]))
    del list1[0]    
    break
grid[4]=templist1

#reading input and inserting it into grid
templist1=[]
for i in list1:
    for j in range(9):
        templist1.append(eval(i[j]))
    del list1[0]    
    break
grid[5]=templist1

#reading input and inserting it into grid

templist1=[]
for i in list1:
    for j in range(9):
        templist1.append(eval(i[j]))
    del list1[0]    
    break
grid[6]=templist1

#reading input and inserting it into grid
templist1=[]
for i in list1:
    for j in range(9):
        templist1.append(eval(i[j]))
    del list1[0]    
    break
grid[7]=templist1


#reading input and inserting it into grid
templist1=[]
for i in list1:
    for j in range(9):
        templist1.append(eval(i[j]))
    del list1[0]    
    break
grid[8]=templist1

    
    
def row():
    """checking the rows whether the rows are valid or not"""
    valid = True
    x=0
    for i in grid:
        for y in range(x+1,9):
            if i[x]==i[y]:
                valid = False
                break
        x = x+1
    return valid
    
def column():
    """checking the columns whether the column are valid or not"""
    valid = True
    for x in range(9):
        column=[]
        x=0
        for y in grid:
            for w in range(9):
                column.append(y[w])
            for z in range(x+1,9):
                if column[x]==column[z]:
                    valid = False
                    break
            x = x+1
            break
    return valid             
        
def grid3():
    """checking in a 3*3 maner whether the grid is valid or not"""
    valid = True
    p = 0
    for i in range (9): 
        numbers = []
        b = 0
        if i==0 or i==1 or i==2:
            for x in grid[:3]:
                for y in range(3):
                    numbers.append(x[3*p + y])
            for k in range (8):
                for z in range(b+1,9):
                    if numbers[b]==numbers[z]:
                        valid = False
                b = b+1
        if i==3 or i==4 or i==5:
            for x in grid[3:6]:
                h=0
                for y in range(3):
                    numbers.append(x[3*p +y])
                    h= h+1
            for k in range(8):
                for z in range(b+1,9):
                    if numbers[b]==numbers[z]:
                        valid = False
                b = b+1                    
        if i==6 or i==7 or i==8:
            for x in grid[6:9]:
                h=0
                for y in range(3):
                    numbers.append(x[3*p + y])
                    h += 1
            for k in range (8):
                for z in range(b+1,9):
                    if numbers[b]==numbers[z]:
                        valid = False
                b = b+1                
        p+=1
        if p==3:
            p=0
    return valid
checking1 = row()
if checking1 == True:
    checking1 = column()
if checking1 == True:
    checking1 = grid3()
if checking1 == True:
    print ("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
















