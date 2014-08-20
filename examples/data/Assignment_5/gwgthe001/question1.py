#a program to simulate a simple BBS 
#Thembekani Gwegwana
#April 2014


def BBS():
    ans='a'
    message='no message yet'
    while ans!='r':
        print('Welcome to UCT BBS')
        print('MENU')
        print('(E)nter a message')
        print('(V)iew message')
        print('(L)ist files')
        print('(D)isplay file')
        print('e(X)it')
        ans=input('Enter your selection:\n') #ask the user for input
        #check the user's input against the statement
        if ans=='E' or ans=='e':
            message=input('Enter the message:\n')
        elif ans=='V' or ans=='v':
            print('The message is:',message)
        elif ans=='L' or ans=='l':
            print('List of files:','42.txt,','1015.txt')
        elif ans=='D' or ans=='d':
            filename=input('Enter the filename:\n')
            if filename=='42.txt' :
                print('The meaning of life is blah blah blah ...')
            elif filename=='1015.txt':
                print('Computer Science class notes ... simplified')
                print('Do all work')
                print('Pass course')
                print('Be happy')
            else:
                print('File not found')
        elif ans=='X' or ans=='x':
            print('Goodbye!')
            break
                


            
    
BBS()
    
             
    
    
    
