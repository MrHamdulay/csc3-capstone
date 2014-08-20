"""emile mclennan
11/5/14
q2 A9"""

def check_dups(s): #check for duplicates
    tot=0
    for let in s:
        tot = tot+ s.count(let)
    if tot > len(s):
        return True
    else:
        return False
        

flag = False
#io = [359716482,867345912,413928675,398574126,546281739,172639548,984163257,621857394,735492861]
#io=['259716483','867345912','413928675','398574126','546281739','172639548','984163257','621857394','735492861']
strIO=[]
rows=[]
digits=[]
count=0
letters=[]

#create a list with the sudoku lines
io=[]
numbers=input()
io.append(numbers)
for i in range(8):
        numbers=input()
        io.append(numbers)

        
#check if 2 cells have same value in row

for i in io: #make nums strings for easy comparison later on
    strIO.append(str(i))
    
for i in io:
    currNum = i
    currNum = str(currNum)
    for number in currNum:
        count = currNum.count(number)
        if count !=1:
            flag = True
            break #if true,no need to continue testing
                        
#check if 2 cells have same value in column
for num in strIO:
    digits.append(num)

for i in range(len(digits)-1): #strip letters from word
    for word in strIO:
        letters.append(word[i])

for i in range(9):
    for i2 in range(8): #test if columns are equal
        if digits[i] ==letters[i2+1]: #ignore its own column
            flag = True
            break #if true,no need to continue testing
        
#check 3x3 grid

grid =[] #populate top 3 grids
current=''
counter=9
whileCount=0
smallerWord=''
smallerWord1=''
smallerWord2=''
while counter > 0:
    current = strIO[whileCount]
    smallerWord= smallerWord+current[0:3]
    smallerWord1= smallerWord1+current[3:6]
    smallerWord2=smallerWord2+current[6:9]
    counter=counter-3
    whileCount+=1
grid.append(smallerWord)
grid.append(smallerWord1)
grid.append(smallerWord2)
#end populate top 3 grids

    
#begin populate middle 3 grids    
current='' 
counter=9
whileCount=3
smallerWord=''
smallerWord1=''
smallerWord2=''
while counter > 0:
    current = strIO[whileCount]
    smallerWord= smallerWord+current[0:3]
    smallerWord1= smallerWord1+current[3:6]
    smallerWord2=smallerWord2+current[6:9]
    counter=counter-3
    whileCount+=1
grid.append(smallerWord)
grid.append(smallerWord1)
grid.append(smallerWord2)         
#end populate middle 3 grids

#begin populate bottom 3 grids
current='' 
counter=9
whileCount=6
smallerWord=''
smallerWord1=''
smallerWord2=''
while counter > 0:
    current = strIO[whileCount]
    smallerWord= smallerWord+current[0:3]
    smallerWord1= smallerWord1+current[3:6]
    smallerWord2=smallerWord2+current[6:9]
    counter=counter-3
    whileCount+=1
grid.append(smallerWord)
grid.append(smallerWord1)
grid.append(smallerWord2)
#end populate bottom 3 grids       

#now we check for duplicates
for cells in grid:
    if check_dups(str(cells)) == True:
        flag = True
        break
# 1 more final check to see if all the tests were true
if flag == False:
    print('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')
    
