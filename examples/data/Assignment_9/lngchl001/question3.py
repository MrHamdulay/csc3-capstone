#prgram to check if sudoku soloution is correct
#By Chloe Longmore
#16 May 2014

#take in input
numbers=[]
for i in range(9):
    nos=str(input(""))
    numbers.append([nos])
    
numbers1=[]
numbers2=[]
numbers3=[]
numbers4=[]
numbers5=[]
numbers6=[]
numbers7=[]
numbers8=[]
numbers9=[]
#split each line into separate lists
for i in numbers[0][0]:
    numbers1.append(int(i))


for i in numbers[1][0]:
    numbers2.append(int(i))


for i in numbers[2][0]:
    numbers3.append(int(i))
    

for i in numbers[3][0]:
    numbers4.append(int(i))
    
for i in numbers[4][0]:
    numbers5.append(int(i))

for i in numbers[5][0]:
    numbers6.append(int(i))

    
for i in numbers[6][0]:
    numbers7.append(int(i))

    
for i in numbers[7][0]:
    numbers8.append(int(i))

        
for i in numbers[8][0]:
    numbers9.append(int(i))
#put all the lists into a list, i.e. 2d array
sum_numbers=[numbers1,numbers2,numbers3,numbers4,numbers5,numbers6,numbers7,numbers8,numbers9]

#check if the sudoku grid is correct
def check_sudoku(sum_numbers):
    n = len(sum_numbers)
    for i in range(0, n):
        horizontal = []
        vertical = []
        for k in range(0, n):
            #vertical check
            if sum_numbers[k][i] in vertical:
                return False
            vertical.append(sum_numbers[k][i])
            #horizontal check
            if sum_numbers[i][k] in horizontal:
                return False
            horizontal.append(sum_numbers[i][k])
    return True

#prints out vaild/invalid
def true_or_false():
    if check_sudoku(sum_numbers)==True:
        print("Sudoku grid is valid")
    elif check_sudoku(sum_numbers)==False:
        print("Sudoku grid is not valid")

check_sudoku(sum_numbers)
true_or_false()