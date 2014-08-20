'''Program for public Bulletin Board Systems (BBS)
Daniel M. Tamale
TMLDAN001
2014-04-15'''

def BBS():
    x=''
    message=''
    while x!='X':
        print ('Welcome to UCT BBS')
        print ('MENU')
        print('(E)nter a message')
        print('(V)iew message')
        print('(L)ist files')
        print('(D)isplay file')
        print('e(X)it')
    
        reply=input('Enter your selection:\n')
    
        '''To enter a message into BBS'''
        if reply.upper()=='E':
            message=input('Enter the message:\n')
        
        '''To view message entered in BBS'''
        if reply.upper()=='V':
            if message=='':
                print ('The message is: no message yet')
            else:
                print ('The message is:',message)
            
        '''To list files in BBS'''
        if reply.lower()=='l':
            print('List of files: 42.txt, 1015.txt')
            
        '''To display files in BBS'''
        if reply.lower()=='d':
            reply_2=input('Enter the filename:\n')
            if reply_2=='42.txt':
                print ('The meaning of life is blah blah blah ...')
            elif reply_2=='1015.txt':
                print ('Computer Science class notes ... simplified')
                print('Do all work')
                print('Pass course')
                print('Be happy')
            else:
                print ('File not found')

        '''To exit the BBS'''
        if reply.upper()=='X':
            print ('Goodbye!')
            break        
BBS()