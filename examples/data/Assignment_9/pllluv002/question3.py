"""Sudoko checker
BY:Luveshen Pillay
5/11/2014"""


#Sudoku checker

# Appending of and processing of lists
list0=[]
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]
biglist=[]
in0=input("")
list0=list(str(in0))
biglist.append(list0)

in1=input("")
list1=list(str(in1))
biglist.append(list1)

in2=input("")
list2=list(str(in2))
biglist.append(list2)

in3=input("")
list3=list(str(in3))
biglist.append(list3)

in4=input("")
list4=list(str(in4))
biglist.append(list4)

in5=input("")
list5=list(str(in5))
biglist.append(list5)

in6=input("")
list6=list(str(in6))
biglist.append(list6)

in7=input("")
list7=list(str(in7))
biglist.append(list7)

in8=input("")
list8=list(str(in8))
biglist.append(list8)
#Checker
check=""
#Check rows
for i in range(9):
    for j in range(9):
        a=biglist[i].count(str(j))
        if a>1:
            check="no"
        
        
        
#Check colums
if check=="":
    for j in range(8):
        for i in range(len(biglist)-1):
            if biglist[i][j]==biglist[i+1][j]:
                check="no"
            
    
#Check 3x3 grid
e=0
r=3
t=0
y=3
templist=[]
if r<=9:
    for i in range(6,9):
        for j in range(6,9):
            templist.append(biglist[i][j])
        
        for k in range(0,9):
            a=biglist[i].count(str(k))
            if a>1:
                check="no"
                
            else:
                templist=[]
                t+=3
                y+=3
                
    e+=3
    r+=3
        
        
            
        
        
        

               

            
if check !="":
    print("Sudoku grid is not valid")
    
if check =="":
    print("Sudoku grid is valid")
