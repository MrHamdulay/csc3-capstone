def good():
    LIST = []
    LIST1 = []
    x = input('Enter strings (end with DONE):\n')
    while x != 'DONE':
        LIST.append(x)
        x = input()
    
    for i in LIST:
        if i not in LIST1:
            LIST1.append(i)
    print()        
    #print(LIST1)
    print('Unique list:')
    for i in LIST1:
        print(i)
good()