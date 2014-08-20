#Program to check if a complete Sudoku grid is valid or not.
#BRXCAI001
#16 May 2014

#Create an empty list.
sudoku=[]

#Add sudoku numbers to empty list.
num=input()
sudoku.append(num)
for i in range(8):
        num=input()
        sudoku.append(num)
        
#"Result" will be used as the ultimate varibale to show whether the sudoku grid is valid.

result=True
counter=0

#Check that no smaller 3 by 3 grid, in the 9 by 9 array, has the same value. 

#Variables.
smallgrid=[] 
rownum=0
num='' 
x=9

#Grids 1,2,3 refer to smaller 3x3 blocks in greater 9x9 grid. 
grid1='' 
grid2=''
grid3=''

#Go through each line and add 1st, 2nd and 3rd 3 numbers to repsective blocks. Then loop through so that the 1st three horizontal blocks form  one string in a list.
while x > 0:
        num = sudoku[rownum]
        grid1+=num[0:3]
        grid2+=num[3:6]
        grid3+=num[6:9]
        rownum+=1
        x-=3
smallgrid.append(grid1)
smallgrid.append(grid2)
smallgrid.append(grid3)
                
#Use same process but now for second three horizontal blocks.

rownum=3
num='' 
x=9
grid1=''
grid2=''
grid3=''
while x > 0:
        num = sudoku[rownum]
        grid1+=num[0:3]
        grid2+=num[3:6]
        grid3+=num[6:9]
        rownum+=1
        x-=3
smallgrid.append(grid1)
smallgrid.append(grid2)
smallgrid.append(grid3)
                
#Use same process but now for third three horizontal blocks.

rownum=6
num='' 
x=9
grid1=''
grid2=''
grid3=''
while x > 0:
        num = sudoku[rownum]
        grid1+=num[0:3]
        grid2+=num[3:6]
        grid3+=num[6:9]
        rownum+=1
        x-=3
smallgrid.append(grid1)
smallgrid.append(grid2)
smallgrid.append(grid3)       
                        
#Check for any duplicate values in smaller 3x3 grids. If there is duplicates, return that the sudoku is invalid. Use break loop because if one value is invalid then the whole sudoku is.

for j in smallgrid:
        for i in j:
                count = j.count(i)
                if count  > 1:
                        result = False
                        break
 
#Check no 2 blocks in the same row have the same value.
for i in sudoku:
        for num in i:
                counter=i.count(num) 
                if counter != 1:
                        result = False 
                        break 
                

#Check no 2 blocks in the same coloumn have the same value.
list1=[]
list2=[]
for num in sudoku:
        list1.append(num)
        
for i in range(len(list1)-1):
        for letter in sudoku:
                list2.append(letter[i])
        
for z in range(9):
        for y in range(8):
                if list1[z] == list2[y+1]:
                        result = False
                        break  
                
#Print respective statements if result is true or false.
if result == True:
        print("Sudoku grid is valid")
else:
        print("Sudoku grid is not valid")