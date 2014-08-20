# Dalise Steynfaard
# STYDAL001
# Assignment 5, question 1
# 12-04-2014

def BBS():
    m = 'no message yet'
    s = ''
    files = {'42.txt':'The meaning of life is blah blah blah ...',
             '1015.txt':'Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy'}
    while not(s == 'X'):
        print('Welcome to UCT BBS\nMENU')
        print('(E)nter a message\n'+'(V)iew message\n'+'(L)ist files\n'+
              '(D)isplay file\n'+'e(X)it')
        s = input('Enter your selection:\n')
        s = s.upper()
        if s == 'E':
            m = input('Enter the message:\n')
        elif s == 'V':
            print('The message is:', m)
        elif s =='L':
            print('List of files: 42.txt, 1015.txt')
        elif s == 'D':
            f = input('Enter the filename:\n')
            if f in files:
                print(files[f])
            else:
                print('File not found')
        elif s == 'X':
            print('Goodbye!')

BBS()