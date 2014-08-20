print('Enter strings (end with DONE):')
x = []
enter = ' '
max = 0
count = 0
while enter!='DONE':
    enter = input()
    if enter!='DONE':
        x.append(enter)
        if max < len(enter):
            max = len(enter)
        count+=1
print()
print('Right-aligned list:')
test = 0
while test<count:
    print((max-len(x[test]))*' '+x[test])
    test+=1