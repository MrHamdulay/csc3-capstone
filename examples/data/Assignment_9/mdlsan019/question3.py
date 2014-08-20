"""Sanele Mdlalose
   Sudoku Grid Validity
   Question 3, Assignment 9
   16 May 2014"""

lst=[]

for i in range(9):
    
    lst_acq=input()
    lst.append(list(lst_acq))
    
lst1=[]
lst2=[]
lst3=[]
lst4=[]
lst5=[]
lst6=[]
lst7=[]
lst8=[]
lst9=[]
q = []
for a in range(9):
    for b in range(3):
        if a <= 2:
            if b == 0:
                q = lst1
            elif b == 1:
                q = lst2
            elif b == 2:
                q = lst3
        elif a <= 5:
            if b == 0:
                q = lst4
            elif b == 1:
                q = lst5
            elif b == 2:
                q = lst6
        elif a <= 8:
            if b == 0:
                q = lst7
            elif b == 1:
                q = lst8
            elif b == 2:
                q = lst9           
        
        q.append(list(lst[a][:3]))
        del lst[a][:3]
     
same=False
for i in range(9):
    if same == True:
        break
    if i==0:
        var=lst1
    elif i==1:
        var=lst2
    elif i==2:
        var=lst3
    elif i==3:
        var=lst4
    elif i==4:
        var==lst5
    elif i==5:
        var=lst6
    elif i==6:
        var=lst7
    elif i==7:
        var=lst8
    else:
        var=lst9
        
    for row in range(1,2):
        if same == True:
            break
        for col in range(3):
            if var[row][col]!=var[row-1][col]:
                if var[row][col]!=var[row+1][col]:
                    if var[col][row]!=var[col][row-1]:
                        if var[col][row]!=var[col][row+1]:
                            for i in range(1, 2):
                                for j in range(3):
                                    if var[i][j] not in var[0] and var[i][j] not in var[2]:
                                        same = False
                                    else:
                                        same = True
                                        break
                     
                        else:
                            same=True
                    else:
                        same=True
                else:
                    same=True    
            else:
                same=True
                
            if same == True:
                break

if same == True:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")