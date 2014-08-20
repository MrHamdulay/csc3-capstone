# program to check files and enter data
# by Jacob Mwanza
# 16/04/2014

# default message
w = 'The message is: no message yet'

# view menu
def view_message():
    
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

# selection choices
def choice(a):
    if a == 'V' or a == 'v':
        print(w)
        menu()
        
    # enter message
    elif a == 'E' or a == 'e':
        b = input('Enter the message:\n')
        view_message()
        c = input("Enter your selection:\n")
        if c == 'V' or c == 'v':
            print('The message is:',b)
            menu()
        else:
            choice(c)
    elif a == 'L' or a == 'l':
        print('List of files: 42.txt, 1015.txt')
        menu()
        
     # display file   
    elif a == 'D' or a == 'd':
        g = input('Enter the filename:\n')
        if g == '42.txt':
            print('The meaning of life is blah blah blah ...')
            menu()
        elif g == '1015.txt':
            print('Computer Science class notes ... simplified')
            print('Do all work')
            print('Pass course')
            print('Be happy')
            menu()
        else:
            print('File not found')
            menu()
            
# input selection        
def menu():
    view_message()
    option = input("Enter your selection:\n")

    if option == 'X' or option == 'x':
        print('Goodbye!') 
        
    else:
        choice(option)   
    
menu()