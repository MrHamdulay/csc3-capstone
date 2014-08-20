#BTCNAV001
#Ass9
#Q3

lst = []
lst0 = []
lst1 = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []
lst6 = []
lst7 = []
lst8 = []


for i in range(9):
    line = input("")
    lst.append(line)

    
lst0.append(lst[0])
lst1.append(lst[1])
lst2.append(lst[2])
lst3.append(lst[3])
lst4.append(lst[4])
lst5.append(lst[5])
lst6.append(lst[6])
lst7.append(lst[7])
lst8.append(lst[8])


lst00 = []
lst01 = []
lst02 = []
lst03 = []
lst04 = []
lst05 = [] 
lst06 = [] 
lst07 = []
lst08 = []


for i in range(len(lst0[0])):
    lst00.append(lst0[0][i])
    lst01.append(lst1[0][i])
    lst02.append(lst2[0][i])
    lst03.append(lst3[0][i])
    lst04.append(lst4[0][i])
    lst05.append(lst5[0][i])
    lst06.append(lst6[0][i])
    lst07.append(lst7[0][i])
    lst08.append(lst8[0][i])
    
valid = 0

for i in lst00:
    l = lst00.count(i)
    if l > 1:
        valid = 1

for i in lst01:
    l = lst01.count(i)
    if l > 1:
        valid = 1
        
for i in lst02:
    l = lst02.count(i)
    if l > 1:
        valid = 1  
        
for i in lst03:
    l = lst03.count(i)
    if l > 1:
        valid = 1
        
for i in lst04:
    l = lst04.count(i)
    if l > 1:
        valid = 1 
        
for i in lst05:
    l = lst05.count(i)
    if l > 1:
        valid = 1
        
for i in lst06:
    l = lst06.count(i)
    if l > 1:
        valid = 1    
        
for i in lst07:
    l = lst07.count(i)
    if l > 1:
        valid = 1

for i in lst08:
    l = lst08.count(i)
    if l > 1:
        valid = 1        


for j in range(9):
    y=[]
    for k in range(9):
        y.append(lst[k][j])
    for i in y:
        t = y.count(i)
        if t>1:
            valid = 1
            
p = []
for i in range(3):
    p.append(lst00[i])
    p.append(lst01[i])
    p.append(lst02[i])

for i in p:
    w = p.count(i)
    if w>1:
        valid = 1

                 
if valid == 0:
    print("Sudoku grid is valid")
    
else:
    print("Sudoku grid is not valid")
    