welcome = ('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')

files = ('List of files: 42.txt, 1015.txt')

f42 = ('The meaning of life is blah blah blah ...')
f1015 = ('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
mess = ''

k = 0

print(welcome)

while k != 1:
    
    option = input('Enter your selection:\n')
    option = option.upper()    

    if option == 'X':
        print('Goodbye!')
        k = 1

    elif option == 'E':
        mess = input('Enter the message:\n')
        print(welcome)        
    
    elif option == 'V':
        if mess == '':
            print('The message is: no message yet')
        else:
            print('The message is:', mess)
        print(welcome)
    
    elif option == 'L':
        print(files)
        print(welcome)
    
    elif option == 'D':
        tf = input('Enter the filename:\n')
        
        if tf == '42.txt':
            print(f42)
        elif tf == '1015.txt':
            print(f1015)
        else:
            print('File not found')
        
        print(welcome)