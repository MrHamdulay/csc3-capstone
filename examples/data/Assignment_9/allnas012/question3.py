'''from random import sample


random_list = sample([1,2,3,4,5,6,7,8,9],9)
random_list = random_list + random_list[:9]
for i in range(3):
    for j in range(3):
        print(random_list[i+j*3:i+j*3+9])'''
    
'''def sudoku(p):
    n=len(p)
    dig=1
    while dig<=n:
        i=0
        while i<n:
            row=0
            col=0
            j=0
            while j<n:
                if p[i][j]==dig:
                    row+=1
                if p[j][i]==dig:
                    col+=1
                j+=1
            if row!=1 or col!=1:
                return "Sudoku grid is not valid"
            i+=1
        dig+=1
    return "Sudoku grid is valid"'''


def isValid(grid):
    grid=input()
    for x in range(0,9):   # check rows
        temp_list = []
        for i in grid[x]:
            if i != 0:
                if i in temp_list:
                    return 2
                temp_list.append(i)
    for y in range(0,9):  # check columns
        temp_list = []
        for x in range(0,9):
            i = grid[x][y]
            if i != 0:
                if i in temp_list:
                    return 2
                temp_list.append(i)                             
    return 1