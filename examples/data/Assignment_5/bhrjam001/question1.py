def menu():
    options = ['E', 'V', 'L', 'D', 'X']
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    select = input("Enter your selection:\n")
    if select.upper() not in options:
        return -1
    else:
        return options.index(select.upper())
    
def main():
    message = 'no message yet'
    while True:
        select = menu()
        if select == 0:
            message = input('Enter the message:\n')
        elif select == 1:
            print('The message is:', message)
        elif select == 2:
            print('List of files: 42.txt, 1015.txt')
        elif select == 3:
            file = input('Enter the filename:\n')
            if file == '42.txt':
                print('The meaning of life is blah blah blah ...')
            elif file == '1015.txt':
                print('Computer Science class notes ... simplified')
                print('Do all work')
                print('Pass course')
                print('Be happy')     
            else:
                print('File not found')
        elif select == 4:
            print('Goodbye!')
            break
        
if __name__ == '__main__':
    main()
    

