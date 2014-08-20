def sudoku(x): 
    
    length = len(x)  
    number = 1
    while number <= length:
        a = 0
        while a < length:
            count1 = 0
            count2 = 0
            b = 0
            while b < length:
                if x[a][b] == number:
                    count1 += 1
                if x[b][a] == number:
                    count2 = count2 + 1
                b += 1
            if count1 != 1 or count2 != 1:
                return print("Sudoku grid is not valid")
            a = a +1
        number += 1
    return print("Sudoku grid is valid")


list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []


listmain = []


list1n = eval(input()) 
list1s = str(list1n)  
for i in list1s:  
    list1.append(int(i)) 

list2n = eval(input())
list2s = str(list2n)
for i in list2s:
    list2.append(int(i))
    
list3n = eval(input())
list3s = str(list3n)
for i in list3s:
    list3.append(int(i))

list4n = eval(input())
list4s = str(list4n)
for i in list4s:
    list4.append(int(i))
    
list5n = eval(input())
list5s = str(list5n)
for i in list5s:
    list5.append(int(i))

list6n = eval(input())
list6s = str(list6n)
for i in list6s:
    list6.append(int(i))

list7n = eval(input())
list7s = str(list7n)
for i in list7s:
    list7.append(int(i))

list8n = eval(input())
list8s = str(list8n)
for i in list8s:
    list8.append(int(i))

list9n = eval(input())
list9s = str(list9n)
for i in list9s:
    list9.append(int(i))



listmain.append(list1)
listmain.append(list2)
listmain.append(list3)
listmain.append(list4)
listmain.append(list5)
listmain.append(list6)
listmain.append(list7)
listmain.append(list8)
listmain.append(list9)

sudoku(listmain)

