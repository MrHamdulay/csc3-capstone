def align():
    LIST = []
    LISTLENGTH = []
    name = input("Enter strings (end with DONE):\n")
    length = len(name)
    while name != 'DONE':
        LIST.append(name)
        LISTLENGTH.append(length)
        name = input()
        length = len(name)
    LISTLENGTH.sort(key=int)
    #print(LISTLENGTH)
    print()
    print('Right-aligned list:')
    for i in LIST:
        print(i.rjust(LISTLENGTH[-1]))
        
align()