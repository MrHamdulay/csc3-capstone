def votes():
    print('Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):')
    LIST = []    
    x = input()
    while x != 'DONE':
        LIST.append(x)
        x = input()
   
    LIST1 = []
    LIST2 = []
    for i in LIST:
        if i in LIST1:
            continue
        LIST1.append(i)
        c = LIST.count(i)
        LIST2.append(c)
    print()
    print('Vote counts:')
    k = 0   
    S = ' '
   # time = "{:>10}"
    LIST3 = []
    for i in LIST2:
        i = '- ' + str(i)
        LIST3.append(i)
    LIST4 = []
    e = 0
    for i in LIST1:
        i = str(i).ljust(11)+ str(LIST3[e])
        e+=1
        LIST4.append(i)
    LIST4 = sorted(LIST4)
    for i in LIST4:
        #print(LIST1[k],(LIST3[k]).ljust(21))
        print(i)

votes()