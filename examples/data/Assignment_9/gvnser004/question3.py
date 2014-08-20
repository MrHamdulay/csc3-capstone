

s_arr = [ ]

check = True
for i in range(9):
    s_arr.append(input())
arr = [ ]

for i in range(9):
    
    arr.append(s_arr[i][0:3])
    
for i in range(9):
    
    arr.append(s_arr[i][3:6])
for i in range(9):
    
    arr.append(s_arr[i][6:9])
    
i=0
while(i<len(arr)):
    arr[i]=arr[i]+arr[i+1]+arr[i+2]
    arr.remove(arr[i+1])
    arr.remove(arr[i+1])
    i=i+1

arr_col = [[],[],[],[],[],[],[],[],[]]
for i in range(9):
    
    for j in range(9):
        
        arr_col[i].append(s_arr[j][i])
for i in range(9):
    
    for j in range(9):
    
        if(arr[i].index(arr[i][j])!=j):

            check=False
for i in range(9):
   
    for j in range(9):

        if(arr_col[i].index(arr_col[i][j])!=j):

            check=False
for i in range(9):
    
    
    for j in range(9):

        if(s_arr[i].index(s_arr[i][j])!=j):

            check=False
            
if(check):
    
    print("Sudoku grid is valid")
else:
    
    print("Sudoku grid is not valid")