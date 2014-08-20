#Mbongeni Mazibuko
#MZBMBO002
#Assignment 5

files = ['The meaning of life is blah blah blah ...','''Computer Science class notes ... simplified
Do all work
Pass course
Be happy''']
msg= 'no message yet'
sel='Users selection'

while sel!='X':
    print('''Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it''')
    sel= (input('Enter your selection:\n')).upper()
    if sel=='E':
        msg= input('Enter the message:\n')
    elif sel=='V':
        print('The message is:',msg)
    elif sel=='L':
        print('List of files:','42.txt,','1015.txt')
    elif sel=='X':
        print('Goodbye!')
    elif sel=='D':
        filename= input('Enter the filename:\n')
        if filename=='42.txt':
            print(files[0])
        elif filename=='1015.txt':
            print(files[1])
        else: print('File not found')