"""Assignment 9-Question 3: Checking a sudoku grid
Duncan Saffy
May 12 2014"""


rows_list=[]
count=0
for row in range(9):
    x=input("")
    rows_list.append(x)
    
s_list=[]
for no in rows_list:
    list1=[]
    for i in no:
        list1.append(i)
    s_list.append(list1)

sudoku=1
#checking rows
for q in range(9):
    for a in range(9):
        if s_list[q][a] in s_list[q][a+1:]:
            sudoku=-1
            break
            
#checking columns

index=0
while index<9:
    count=0
    while count<8:
        if s_list[count][index]==s_list[count+1][index]:
            sudoku=-1
            break
        else:
            count+=1
    index+=1

grid_1=[]
grid_2=[]
grid_3=[]
grid_4=[]
grid_5=[]
grid_6=[]
grid_7=[]
grid_8=[]
grid_9=[]

#checking for code in 3x3 area      
for p in range(3):
    for o in range(3):
        grid_1.append(s_list[p][o])
        
for p in range(3):
    for o in range(3,6):
        grid_2.append(s_list[p][o])
        
for p in range(3):
    for o in range(6,9):
        grid_3.append(s_list[p][o])
        
for p in range(3,6):
    for o in range(3):
        grid_4.append(s_list[p][o])
            
for p in range(3,6):
    for o in range(3,6):
        grid_5.append(s_list[p][o])
            
for p in range(3,6):
    for o in range(6,9):
        grid_6.append(s_list[p][o])
        
for p in range(6,9):
    for o in range(3):
        grid_7.append(s_list[p][o])
                
for p in range(6,9):
    for o in range(3,6):
        grid_8.append(s_list[p][o])
                
for p in range(6,9):
    for o in range(6,9):
        grid_9.append(s_list[p][o])
        
grid_main=[]
grid_main.append(grid_1)
grid_main.append(grid_2)
grid_main.append(grid_3)
grid_main.append(grid_4)
grid_main.append(grid_5)
grid_main.append(grid_6)
grid_main.append(grid_7)
grid_main.append(grid_8)
grid_main.append(grid_9)
        
for q in range(9):
    for a in range(8):
        if a==7:
            if grid_main[q][a] == grid_main[q][a+1]:
                sudoku=-1
        elif grid_main[q][a] in grid_main[q][a+1:]:
            sudoku=-1
            break
#checking made grids

if sudoku == 1:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")


            



    