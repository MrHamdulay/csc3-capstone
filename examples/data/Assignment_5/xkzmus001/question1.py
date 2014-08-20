"""question1.py Bulletin Board System
Author : Musa Xakaza
Student# : XKZMUS001
Date : 12/04/2014"""

option = ''
msg = ''
file42 = 'The meaning of life is blah blah blah ...'
file1015 = 'Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy'
exist = False

while option != 'X':
        print('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message')
        print('(L)ist files\n(D)isplay file')
        print('e(X)it')
        option = input('Enter your selection:\n').upper()
        
        if option == 'E': 
                msg = input('Enter the message:\n')
        elif option == 'V':
                if msg: print('The message is:',msg)
                else: print('The message is: no message yet')
        elif option == 'L':
                print('List of files:','42.txt,','1015.txt')
        elif option == 'D':
                filename = input('Enter the filename:\n')
                if filename == '42.txt': print(file42)
                elif filename == '1015.txt': print(file1015)
                else : print('File not found')
print('Goodbye!')