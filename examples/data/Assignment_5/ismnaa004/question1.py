
def menu():
    print('Welcome to UCT BBS \nMENU')
    print('(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay files \ne(X)it')

    
def main():
    menu()
    
    selection=input('Enter your selection:')
    selection=str.upper(selection)       
   
    if (selection=='E'):
        global message
        message=input('Enter the message:')
        menu()
        selection=input('Enter your selection:')
        selection=str.upper(selection)           
    elif (selection=='V'):
        return message
    if not message:
        print('no message yet')
        
    elif (selection=='X'):
        print ('Goodbye!')
    elif (selection=='L'):
        print('List of files: 42.txt, 1015.txt')
        menu()
        selection=input('Enter your selection:')
        selection=str.upper(selection)           
    elif (selection=='D'):
        filename=input('Enter the filename:\n')
        filename=str.lower(filename)
        if (filename=='42.txt'):
            print('The meaning of life is blah blah blah ...')
            menu()
            selection=input('Enter your selection:')
            selection=str.upper(selection)               
        elif (filename=='1015.txt'):
            print('Computer Science class notes ... simplified')
            menu()
            selection=input('Enter your selection:')
            selection=str.upper(selection)               
            
        else:
            print('File not found')
            menu()
            selection=input('Enter your selection:')
            selection=str.upper(selection)               
if __name__== '__main__':
    main()
        
    