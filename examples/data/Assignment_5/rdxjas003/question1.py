import sys

m = 'no message yet';

def run(a):
    if a == 'e':
        global m
        m = input('Enter the message:\n')
        main()
    if a == 'v':
        print('The message is: '+m)
        main()
    if a == 'l':
        print('List of files: 42.txt, 1015.txt')
        main()
    if a == 'd':
        f = input('Enter the filename:\n')
        if f == '1015.txt':
            print('Computer Science class notes ... simplified')
            print('Do all work')
            print('Pass course')
            print('Be happy')
        else:
            if f == '42.txt':
                print('The meaning of life is blah blah blah ...')
            else:
                if f == '1016.txt':
                    print('File not found')
        main()
    if a == 'x':
        print('Goodbye!')
        sys.exit(0)
                
def main():
    print('Welcome to UCT BBS')
    print('MENU')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')
    x = input('Enter your selection:\n')
    run(x)    

main()


