#UCT BBS
#Ruchaan Schmidt
#April 2014

def BBS():
    
    message = ('')
    while True:
        print ('Welcome to UCT BBS')
        
        print ('MENU')
        
        print (' (E)nter a message\n (V)iew message\n (L)ist files\n (D)isplay file\n e(X)it')
        
        sel = input('Enter your selection: \n')

        if sel == ('E') or sel == ('e'):
            message = input('Enter the message:\n')
            
        if sel == ('V') or sel == ('v'):
            if message != (''):
                print('The message is:', message)
            else:
                print('The message is: no message yet')

        if sel == ('L') or sel == ('l'):
            print('List of files: 42.txt, 1015.txt')
    
        if sel == ('D') or sel == ('d'):
            fn = input('Enter the filename:\n')
            
            if fn == ('42.txt'):
                print ('The meaning of life is blah blah blah ...')
            
            if fn == ('1015.txt'):
                print('Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy')
                
            if fn != ('42.txt') or fn != ('1015.tx'):
                print('File not found')
                
        if sel == ('X') or sel == ('x'):
            print("Goodbye!")
            break
BBS()