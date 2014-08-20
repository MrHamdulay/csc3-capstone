# Write a program to check if a complete Sudoku grid is valid or not.
# mashau zwivhuya
# 12 may 2014
# getting input from user and file
list1=[]
file=input("")
list1.append(file)
count=0
while count<8:
    file=input("")
    list1.append(file)
    count+=1
#--------------------------------------------------------------------------------------------------------
k=0
n=0
#checking  wheather numbers are equal on 3x3 grid
def grid1():
    k=True
    checklist=[]
    list3=[]
    for i in range(0,3):
        for j in range(0,3):
            x=list1[j][i]
            checklist.append(x)
    for i in range(9):
        for j in checklist:
            if checklist[i]==j:
                list3.append(j)
        if len(list3)>=2:
            k=False
            return k
        list3=[]
    return k
#checking  wheather numbers are equal on 3x3 grid
def grid2():
    k=True
    checklist=[]
    list3=[]
    for i in range(3,6):
        for j in range(0,3):
            x=list1[j][i]
            checklist.append(x)
    for i in range(9):
        for j in checklist:
            if checklist[i]==j:
                list3.append(j)
        if len(list3)>=2:
            k=False
            return k
        list3=[]
    return k
#checking  wheather numbers are equal on 3x3 grid
def grid3():
    k=True
    checklist=[]
    list3=[]
    for i in range(6,9):
        for j in range(0,3):
            x=list1[j][i]
            checklist.append(x)
    for i in range(9):
        for j in checklist:
            if checklist[i]==j:
                list3.append(j)
        if len(list3)>=2:
            k=False
            return k
        list3=[]
    return k
#checking  wheather numbers are equal on 3x3 grid
def grid4():
    k=True
    checklist=[]
    list3=[]
    for i in range(0,3):
        for j in range(3,6):
            x=list1[j][i]
            checklist.append(x)
    for i in range(9):
        for j in checklist:
            if checklist[i]==j:
                list3.append(j)
        if len(list3)>=2:
            k=False
            return k
        list3=[]
    return k
#checking  wheather numbers are equal on 3x3 grid
def grid5():
    k=True
    checklist=[]
    list3=[]
    for i in range(3,6):
        for j in range(3,6):
            x=list1[j][i]
            checklist.append(x)
    for i in range(9):
        for j in checklist:
            if checklist[i]==j:
                list3.append(j)
        if len(list3)>=2:
            k=False
            return k
        list3=[]
    return k
#checking  wheather numbers are equal on 3x3 grid
def grid6():
    k=True
    checklist=[]
    list3=[]
    for i in range(6,9):
        for j in range(3,6):
            x=list1[j][i]
            checklist.append(x)
    for i in range(9):
        for j in checklist:
            if checklist[i]==j:
                list3.append(j)
        if len(list3)>=2:
            k=False
            return k
        list3=[]
    return k
#checking  wheather numbers are equal on 3x3 grid
def grid7():
    k=True
    checklist=[]
    list3=[]
    for i in range(0,3):
        for j in range(6,9):
            x=list1[j][i]
            checklist.append(x)
    for i in range(9):
        for j in checklist:
            if checklist[i]==j:
                list3.append(j)
        if len(list3)>=2:
            k=False
            return k
        list3=[]
    return k
#checking  wheather numbers are equal on 3x3 grid
def grid8():
    k=True
    checklist=[]
    list3=[]
    for i in range(3,6):
        for j in range(6,9):
            x=list1[j][i]
            checklist.append(x)
    for i in range(9):
        for j in checklist:
            if checklist[i]==j:
                list3.append(j)
        if len(list3)>=2:
            k=False
            return k
        list3=[]
    return k
#checking  wheather numbers are equal on 3x3 grid
def grid9():
    k=True
    checklist=[]
    list3=[]
    for i in range(6,9):
        for j in range(6,9):
            x=list1[j][i]
            checklist.append(x)
    for i in range(9):
        for j in checklist:
            if checklist[i]==j:
                list3.append(j)
        if len(list3)>=2:
            k=False
            return k
        list3=[]
    return k
#checking  wheather numbers are equal on the vertical lines
def func_verti(n):
    if n==9:
        k=True
        return k

    checklist=[]
    list3=[]
    for i in range(9):
        x=list1[i][n]
        checklist.append(x)
    
    for i in range(9):
        for j in checklist:
            if checklist[i]==j:
                list3.append(j)
        if len(list3)>=2:
            k=False
            return k
        list3=[]
            
    return func_verti(n+1)
#checking  wheather numbers are equal on the horizontal line
def func_hori(n):
    if n==9:
        return True

    checklist=[]
    list3=[]
    for i in range(9):
        x=list1[n][i]
        checklist.append(x)
    
    for i in range(9):
        for j in checklist:
            if checklist[i]==j:
                list3.append(j)
        if len(list3)>=2:
            k=False
            return k
        
        list3=[]
  
    return func_hori(n+1)
# a function joining all functions and printing out the results
def combining():
    if grid1() and grid2() and grid3() and grid4() and grid5() and grid6() and grid7() and grid8() and grid9() and func_hori(0) and func_verti(0):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
        
combining()
    