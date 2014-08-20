#Thea Sitek, STKTHE002
#16.05.2014
#Sudoku

#turn input string to array
array = []
for i in range(9):
    #always 9 * 9 formation
    array.append([]*9)
    #for each row, insert numbers
for i in range(9):
    userInput = str(input())
    info = list(userInput)
    for j in range(9):
        array[i].append(info[j])
        
#strings into integers
a=[]
#create new grid
for i in range(9):
    a.append([]*9)
#...but with numerical values
for i in range(9):
    for j in array[i]:
        a[i].append(int(j)) 
               
        

#check if valid sudoku
# values 1 to 9 in both directions
def check_sudoku(array):
    x = len(array)
    for i in array:
        countR = 1
        #check if all numbers 1 to 9 in each row
        while countR <= x:
            if countR not in i:
                return 0
            countR += 1
    
    #split up array
    counter = 0
    col = []
    row = []
    while counter < x:
        for i in array:
            row.append(i[counter])
        col.append(row)
        row = []
        counter += 1
        
    #checks columns
    for j in col:
        countC = 1
        while countC <= x:
            if countC not in j:
                return 0
            countC +=1
    return 1



    
#if all requirements true
if check_sudoku(a): #and check_pieces(a):
    print("Sudoku grid is valid")
#if not
else:
    print("Sudoku grid is not valid")