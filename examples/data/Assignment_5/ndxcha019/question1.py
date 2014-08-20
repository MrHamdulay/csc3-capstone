'''Luke Naude
16 April'''

def main():
    message='no message yet'
    menu()

def menu():
    print('Welcome to UCT BBS')
    print('MENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')
    user_choice=input('Enter your selection:\n')
    
    if user_choice=='E' or user_choice== 'e': 
        global message
        message=input('Enter the message:\n')
        main()
        
    if user_choice=='V' or user_choice=='v':
        global message
        print('The message is: ',message,sep='')
        main()
    
    if user_choice=='L'or user_choice=='l':
        print('List of files: 42.txt, 1015.txt')
        main()
        
    if user_choice=='D' or user_choice=='d':
        file_choice=input('Enter the file name: \n')
        if file_choice == '42.txt':
            print('The meaning of life is blah blah blah ...')
            menu()
        if file_choice=='1015.txt':
            print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
            menu()
        else:
            print('File not found')
            menu()
        
    if user_choice=='X' or user_choice == 'x':
        print('Goodbye!')
    
        

  

    


main()
