# Creating a bulletin board system#
# Sohail Tulsi TLSSOH001    
# 15 April 2014

uselct=''
mes = 'no message yet'

while uselct != 'X':
    print('Welcome to UCT BBS\n','MENU\n','(E)nter a message\n','(V)iew message\n','(L)ist files\n','(D)isplay file\n','e(X)it', sep='')
    selct= input('Enter your selection:\n')        # user input selectioninput    
    uselct= selct.upper()              # capitilise all  
  
# specify actions for selection  
    if uselct == 'E':
        mes= input('Enter the message:\n')
    elif uselct == 'V':
        print('The message is:', mes)
    elif uselct == 'L':
        print('List of files: 42.txt, 1015.txt')
    elif uselct == 'D':
        file = input('Enter the filename:\n')
        if file == '1015.txt':
            print('Computer Science class notes ... simplified')
            print('Do all work')
            print('Pass course')
            print('Be happy')
        elif file == '42.txt':
            print('The meaning of life is blah blah blah ...')
        else:
            print('File not found')
        
print('Goodbye!')