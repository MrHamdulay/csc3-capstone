"""programme to check sudoku
Paul Truter
16 May 2014"""

#convert input into array
array = []
for i in range(9):
    array.append([]*9)
for i in range(9):
    userInput=str(input())
    Input = list(userInput)
    for j in range(9):
        array[i].append(Input[j])
        
#convert array of strings into integers
grid=[]
for i in range(9):
    grid.append([]*9)
for i in range(9):
    for j in array[i]:
        grid[i].append(int(j))
        
def check_sudoku(array):
    #checks if numbers in rows range from 1-9
    x = len(array)
    for i in array:
        counter = 1
        while counter <= x:
            if counter not in i:
                return False
            counter+=1
    
    #splits up array for easier check
    counter2 = 0
    col = []
    row = []
    while counter2 < x:
        for i in array:
            row.append(i[counter2])
        col.append(row)
        row=[]
        counter2+=1
    #checks columns
    for j in col:
        counter3=1
        while counter3 <= x:
            if counter3 not in j:
                return False
            counter3 +=1
    return True


#check if grid is valid or not
if check_sudoku(grid):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")