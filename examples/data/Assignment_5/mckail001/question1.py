#Ailsa Mackay: MCKAIL001
#Assignment 5 
#Question 1: Program to simulate BBF
#2014-04-15

end = False
menu="Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n"
menu+="(L)ist files\n(D)isplay file\ne(X)it"
message="no message yet"

def display_file(filename):
    if filename=='42.txt':
        filecont='The meaning of life is blah blah blah ...'
    elif filename=='1015.txt':
        filecont='Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy'
    else: filecont='File not found'
    return filecont

while not end:
    print(menu)
    choice = input('Enter your selection:\n').lower() 
    if choice == 'e':
        message = input('Enter the message:\n')
    elif choice == 'v':
        print('The message is:',message)
    elif choice == 'l':
        print('List of files: 42.txt, 1015.txt')
    elif choice == 'd':
        print(display_file(input('Enter the filename:\n'))) 
    elif choice == 'x':
        end = True 
        print('Goodbye!') 
