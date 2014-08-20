#Ikhlaas Pohplnker
#16 May 2014
#a program to check if a complete Sudoku grid is valid or not
list_of_nums=[]#empty list
p=0#initialise p to zero
while p<9:#ask for input for as long as p is less than zerpo
    x=input()#asks for input
    list2=[]#empty temporary list
    for i in range(9):
        y=x[i]
        list2.append(y)#adds a number to a list
    list_of_nums.append(list2)#adds list2 to list_of_nums
    p=p+1 
t=True#intialise t to true
for row in range(9):
    for col in range(9):
        z=1#initialise z to 1
        while col+z<9 and t==True:#keeps on checking the condition below until the conditions are not met
            if list_of_nums[row][col]==list_of_nums[row][col+z]:
                    t=False#if the same number is found in the same row more than once then the sudoku is not valid
            z=z+1
q=True#initialise q to true
for col in range(9):
    for row in range(9):
        z=1#initialise z to 1
        while row+z<9 and q==True:#keeps on checking the condition below until the conditions are not met
            if list_of_nums[row][col]==list_of_nums[row+z][col]:
                    q=False#if the same number is found in the same column more than once then the sudoku is not valid
            z=z+1 
for a in range(0,7,3):
    for b in range(0,7,3):
        temporary_list=[]#empty temporary list
        for c in range(3):
            for d in range(3):
                if not list_of_nums[a+c][b+d] in temporary_list:
                    temporary_list.append(list_of_nums[a+c][b+d])#if the number is not in the temporary list then add it to the temporary list
        if len(temporary_list)<9:
            t=False#if the same number is found in the 3x3 subgrid more than once then the sudoku is not valid
if t==True and q==True:
    print("Sudoku grid is valid")#if t is true and q is true then the sudoku grid is valid
else:
    print("Sudoku grid is not valid")#if t is false and q is false then the sudoku grid is not valid
