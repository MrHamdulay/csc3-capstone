
#Shahrain Coovadia #CVDSHA002
def strings():
    start=input("Enter strings (end with DONE):\n")             #asks for input of strings
    var=0
    list=[]
    while start!="DONE":                    #loop start with boolean expression                 
        if start not in list:
            list.append(start)          #append strings to list
            var+=1
            start=input()
        else: start =input()
    print(" ")    
    print('Unique list:')               
    c='\n'.join(list)                         #formatting 
    for k in range (var):
        print(list[k])
strings()            