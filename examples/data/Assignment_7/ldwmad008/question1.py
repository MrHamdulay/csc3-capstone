'''Unique list presenter
Frans Ledwaba
05 May 2014'''

#create a list
x = []

#fill the list
y = input('Enter strings (end with DONE):\n')
if y == 'DONE':
    print(' ')
    print('Unique list:')

#create unique list
else:
    x.append(y)
    y = ''
    while y != 'DONE':
        y = input('')
        x.append(y)
    x.remove('DONE')

    #create unique list
    u = []
    for i in range(len(x)):
        if u.count(x[i]) == 0:
            u.append(x[i])
    #unique list
    print(' ')
    print('Unique list:')
    for i in range(len(u)):
        print(u[i])