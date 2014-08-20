names = []
enter = ' '
count = 0
print('Enter strings (end with DONE):')
while enter!='DONE':
    enter = input()
    if enter!='DONE':
        uneek = 1
        test1 = 0
        while test1<count:
            if names[test1]==enter:
                uneek = 0
            test1+=1
        if uneek==1:
            names.append(enter)
            count+=1        
print('\nUnique list:')
test = 0
while test<count:
    print(names[test])
    test+=1