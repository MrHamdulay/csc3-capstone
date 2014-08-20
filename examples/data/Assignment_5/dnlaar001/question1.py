# programe that graphically illustrates functions 
# Aaron Daniels
# 15 April 2014

print('Welcome to UCT BBS')
print('MENU')
print('(E)nter a message')
print('(V)iew message')
print('(L)ist files')
print('(D)isplay file')
print('e(X)it')
k=input('Enter your selection:\n')
t="no message yet"

while k=='e' or k=='E' or k=='V' or k=='v' or k=='L' or k=='l' or k=='D' or k=='d' or k=='x' or k=='X':
    y='no message yet'
    if k=='E' or k=='e':
        t=input('Enter the message:\n')
    elif k=='V' or k=='v':        
            print('The message is:',t)        
        
    elif k=='L' or k=='l':
        print('List of files: 42.txt, 1015.txt')
        
    elif k=='D' or k=='d':
        fname=input('Enter the filename:\n')
        if fname=='1015.txt' or fname=='42.txt':
            cc=fname
            infile=open(cc,"r")
            data=infile.read()
            print(data)
        else:
            print('File not found')
    elif k=='x' or k=='X':
        print('Goodbye!')
        break
    print('Welcome to UCT BBS')
    print('MENU')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')
    k=input('Enter your selection:\n')    