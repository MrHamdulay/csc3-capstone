def main():
    xinput = ''
    smessage = 'no message yet'
    while not xinput.upper() == 'X':
        print('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')
        xinput = input('Enter your selection:\n')
        if xinput.upper() == 'E':
            smessage = input('Enter the message:\n')
        if xinput.upper() == 'V':
           print('The message is:', smessage)
        if xinput.upper() == 'L':
            print('List of files: 42.txt, 1015.txt')
        if xinput.upper() == 'D':
            filename = input('Enter the filename:\n')
            if filename == '42.txt':
                print('The meaning of life is blah blah blah ...')
            elif filename == '1015.txt':
                print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
            else: print('File not found')
    else: 
        print('Goodbye!')
main()