'''BBS message board
Nic Findlay 13/04/2014'''
import time
count = 0
message = 0
while count == 0:
    print("Welcome to UCT BBS \nMENU")
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')
    
    question = input('Enter your selection:\n').upper()
    
    if question == 'E':
        message += 1
        message_save = input('Enter the message:\n')
        continue
        
    if question == 'V':
        if message == 0:
            print('The message is: no message yet')
        else:
            print('The message is:', message_save)
    if question == 'L':
        print('List of files: 42.txt, 1015.txt')
    if question == 'D':
        selection = input('Enter the filename:\n')
        if selection == '42.txt':
            print('The meaning of life is blah blah blah ...')
        elif selection == '1015.txt':
            print('Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy')
        else: print('File not found')
    if question == 'X': 
        print('Goodbye!')
        break
    else: continue
    
   
    


    
    
    
    
