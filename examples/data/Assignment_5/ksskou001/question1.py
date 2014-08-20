'''This program simulate a simple BBS with one stored message and 2 fixed files
Kouame KOUASSI
12 april 2014'''

#definition of global variable 
message = 'no message yet'

#function to get message
def enter_m():
    global message    
    message = input('Enter the message:\n')
    return message

#function to print message
def view_m(): 
    global message
    if message == 'no message yet':
        print('The message is: no message yet')
    else:
        print('The message is:',message)
    
#function to print menu
def menu():
    print('Welcome to UCT BBS','MENU','(E)nter a message','(V)iew message','(L)ist files','(D)isplay file','e(X)it',sep='\n')
#function to print the list of file
def list_f():
    print('List of files: 42.txt, 1015.txt')

#function to display the file
def display_f():
    file = input('Enter the filename:\n')
    if file == '42.txt':
        print('The meaning of life is blah blah blah ...')
    elif file == '1015.txt':
        print('Computer Science class notes ... simplified','Do all work','Pass course','Be happy',sep='\n')
    else:
        print('File not found')
 
 #main function
def main():
    condition = True
    while condition:
        menu()
        selection = input('Enter your selection:\n')
        selection = selection.upper()
        if selection == 'E':
            enter_m()
        elif selection == 'V':
            view_m()
        elif selection == 'L':
            list_f()
        elif selection == 'D':
            display_f()
        elif selection == 'X':
            print('Goodbye!')
            condition = False
if __name__ == "__main__":
   main()
   
