# Question3 
# 14 May 2014
# Richard van Gysen

# get list input
lis=[]
for i in range(9):
    lis.append(input())

# assume true
check = True
# check grid for 3x3 blocks
def grid(x,y):
    global check
    weight=0
    for i in range(3):
        for j in range(3):
            weight+=2**(eval(lis[x+i][y+j])-1)
    if weight != 511:
        check= False
# use hammingway to check row by row and collumn by collumn
def Hammingweight():
    global check
    for i in range(9):  
        temp=0
        for j in range(9):
            temp+=(2**(eval(lis[i][j])-1))
        if temp != 511:
            check = False
        
    for i in range(9):
        temp=0
        for j in range(9):
            temp+=(2**(eval(lis[j][i])-1))
        if temp != 511:
            check = False
# do for every 3x3 grid
    grid(0,0)
    grid(0,3)
    grid(0,6)
    grid(3,0)
    grid(3,3)
    grid(3,6)
    grid(6,0)
    grid(6,3)
    grid(6,6)
# check if true or false
def check_it():
    if check is False:
        print('Sudoku grid is not valid')
    if check is True:
        print('Sudoku grid is valid')

Hammingweight()
check_it()
