'''right margin program
Frans Ledwaba
25 April 2014'''

#create list
strings = []

#create input for the list
x = input('Enter strings (end with DONE):\n')
strings.append(x)

#set parameters
if x == 'DONE':
    print(' ')
    print('Right-aligned list:')

else:
    print(' ')
    
    #craete empty string and loop input
    x = ''
    while x != 'DONE':
        x = input('')
        strings.append(x)
    
    #remove last loop
    strings.remove('DONE')
    
    #count length of the longest word
    a = len(strings[0])
    for i in range(len(strings)):
        if a < len(strings[i]):
            a = len(strings[i])
            
    #right allignment
    print('Right-aligned list:')
    for i in range(len(strings)):
        print(' '*(a - len(strings[i])), strings[i], sep='')