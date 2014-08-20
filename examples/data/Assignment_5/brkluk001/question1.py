""" BBS Program
Luke BArker
15 April 2014"""
def menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

message = 'no message yet'   
answer=""
    
while answer != 'X' and answer != 'x':
    menu()
    answer = input("Enter your selection: \n")
    if answer == 'e' or answer == "E":
        message = input('Enter the message: \n')
    if answer == 'v' or answer == 'V':
        print('The message is:', message)
    if answer == 'l' or answer == "L":
        print('List of files: 42.txt, 1015.txt')
    if answer == 'd' or answer == 'D':
        selection = input('Enter the filename: \n')
        if selection == '42.txt':
            print('The meaning of life is blah blah blah ...')
        elif selection == '1015.txt':
            print('''Computer Science class notes ... simplified
Do all work
Pass course
Be happy''')
        else: print('File not found')
print('Goodbye!')
    