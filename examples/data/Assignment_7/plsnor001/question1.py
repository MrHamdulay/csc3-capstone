def unique():
    new=[]
    old=[]
    print('Enter strings (end with DONE):')
    while True: #collect list from user
        data=input()
        if data=='DONE':
            break
        old.append(data)
    for i in old: #create new list without word repetions
        if i not in new:
            new.append(i)
 
    print('\nUnique list:')#prints out new list
    for t in new:
        print(t)
unique()        