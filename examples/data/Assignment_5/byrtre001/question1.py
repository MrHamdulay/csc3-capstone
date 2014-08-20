"""program to simulate a simple BBS with one stored message and 2 fixed file
Trevor Byaruhanga
15 april 2014"""
# stored message.
a=('Welcome to UCT BBS'+'\n'+
'MENU'+'\n'+
'(E)nter a message'+'\n'+
'(V)iew message'+'\n'+
'(L)ist files'+'\n'+
'(D)isplay file'+'\n'+
'e(X)it')


print(a)
# input question prompting the user to chose one of the options
#in the menu
command=input('Enter your selection:'+'\n')
#function to work out which item was chosen and present output to the user.
def function(command):
    command=command.upper()
    
    
    if command == 'E':
        message=input('Enter the message:'+'\n')
        print(a)
        command=input('Enter your selection:'+'\n')
        command=command.upper()
        if command == 'X':
            print('Goodbye!')        
        if command == 'V':
            if message:
                print ('The message is:', message)
                print(a)
                command=input('Enter your selection:'+'\n') 
                if command == 'X':
                    print('Goodbye!')
                                       
    
    elif command == 'V':
        print ('The message is: no message yet')
        print(a)
        command=input('Enter your selection:'+'\n')
    elif command == 'X':
        print('Goodbye!')    
    if command == 'L':
        print('List of files: 42.txt, 1015.txt')
        print(a)
        command=input('Enter your selection:'+'\n')
    
    if command == 'D':
        filename=input('Enter the filename:'+'\n')
        if filename=='42.txt':
            print('The meaning of life is blah blah blah ...')
            print(a)
            command=input('Enter your selection:'+'\n')
        elif filename=='1015.txt':
            print('Computer Science class notes ... simplified'+'\n'+
        'Do all work'+'\n'+
        'Pass course'+'\n'+
        'Be happy') 
            print(a)
            command=input('Enter your selection:'+'\n')
            
        else:
            print('File not found')
            print(a)
            command=input('Enter your selection:'+'\n')
            
    
               


function(command)
