
import glob

print('Welcome to UCT BBS')
print('MENU')
print('(E)nter a message')
print('(V)iew message')
print('(L)ist files')
print('(D)isplay file')
print('e(X)it')
#above:printing menu
thein = input('Enter your selection:\n')#input
stored = 'no message yet'#default value

while thein != 'X' and thein != 'x':
    if thein == 'E' or thein == 'e':
        stored = input('Enter the message:\n')
    elif thein == 'V' or thein == 'v':
        print('The message is:', stored)
    elif thein == 'L' or thein == 'l':
        print('List of files:', ', '.join(glob.glob('*.txt')[::-1]))
    elif thein == 'D' or thein == 'd':
        mname = input('Enter the filename:\n')
        if mname in glob.glob('*.txt'):
            mname = open(mname, 'r')
            for line in mname:
                print(line, end = '')
        else:
            print('File not found')
            #evalauting the selection/input agaisnt the menu
    print('Welcome to UCT BBS')
    print('MENU')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')
    thein = input('Enter your selection:\n')

print('Goodbye!')
