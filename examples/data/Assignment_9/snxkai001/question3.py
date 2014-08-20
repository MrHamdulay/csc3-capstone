#Kairav soni
#15/5/14
#Q3 ASS 9

import sys
sys.setrecursionlimit(30000)
list1=[]
list2=[[],[],[],[],[],[],[],[],[]]
block=[[],[],[],[],[],[],[],[],[]]
num=0
num1=0
num2=0
c=0
i=0
y=0

for i in range(0,9,1):
    line=input()
    row=[]
    for l in range(0,9,1):
        row.append(line[l])
    list1.append(row)

for j in range(0,9,1):
    for k in range(0,9,1):
        list2[j].append(list1[k][j])

def blocks(grid):
    global num
    global num1
    global num2
            
    for i in range(num1,num1+3,1):
        for j in range(num2,num2+3,1):
            block[num].append(list1[i][j])
                    
    num2=num2+3
    num=num+1
            
    if num==(9):
            return block 
                
    if num2==(9):
        num2=0 
        num1=num1+3 
                
    return blocks(list1)
        
        
def search_column(column):
    global c 
    global list2

    if len(column)==(1):
        c+=1
        if c<9:
            return search_column(list2[c])
        else:
            return True
        
    else:
        for j in range(1,len(column),1):
            if column[0]==column[j]:
                return False
        
        return search_column(column[1:])
    
    return True
   
def search_row(row):
    global list1
    global i 

    if len(row)==1:
        i=i+1
        if i<(9):
            return search_row(list1[i])
        else:
            return True 
        
    else:
        for j in range(1,len(row),1):
            if row[0]==row[j]:
                return False
        
        return search_row(row[1:])
    return True


blockrow=blocks(list1)
def search_blocks(block):
    global y 
    global blockrow

    if len(block)==(1):
        y=y+1
        if y<(9):
            return search_blocks(blockrow[y])
        else:
            return True
        
    else:
        for j in range(1,len(block),1):
            if block[0]==block[j]:
                return False
        
        return search_blocks(block[1:])
    
    return True

truecolumn=search_column(list2[c])
trueblock=search_blocks(blockrow[y])
truerow=search_row(list1[i])

if truerow==True and truecolumn==True and trueblock==True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")