'''program to check whether a suduko grip (completed) is valid
Luke Naude
13-May-2014'''

#get grid input
grid=[]
for i in range(9):
    grid.append(input())

#assume that the suduko puzzle is true
validity = True

def print_val():
    '''if the validity remains true after testing the hamming weight, print validity'''
    if validity is False:
        print('Sudoku grid is not valid')
    if validity is True:
        print('Sudoku grid is valid')

def squares(x,y):
    global validity
    '''check hammingweight of squares'''
    ham_weight=0
    for i in range(3):
        for j in range(3):
            ham_weight+=2**(eval(grid[x+i][y+j])-1)
    if ham_weight != 511:
        validity= False

def check_Hammingweight():
    global validity
    '''function to check the Hamming weight of each row and columb square of 3*3'''
    for i in range(9):  
        temp_list=0
        for j in range(9):
            temp_list+=(2**(eval(grid[i][j])-1))
        if temp_list != 511:
            validity = False
        
    for i in range(9):
        temp_list=0
        for j in range(9):
            temp_list+=(2**(eval(grid[j][i])-1))
        if temp_list != 511:
            validity = False
    squares(0,0)
    squares(0,3)
    squares(0,6)
    squares(3,0)
    squares(3,3)
    squares(3,6)
    squares(6,0)
    squares(6,3)
    squares(6,6)
check_Hammingweight()
print_val()
##tell user if valid
#check_vertical()
#check_horizontal()

