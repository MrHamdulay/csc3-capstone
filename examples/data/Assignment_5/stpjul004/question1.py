""" UCT BBS program
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-04-14 """

exit = False
options = "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n"
options += "(L)ist files\n(D)isplay file\ne(X)it"

#set default message
message = "no message yet"

def displayfile(filename):
    """ Function that returns the contents of a chosen file """
    if filename == '42.txt':
        filecontents = 'The meaning of life is blah blah blah ...'
    elif filename == '1015.txt':
        filecontents = 'Computer Science class notes ... simplified\n'
        filecontents += 'Do all work\nPass course\nBe happy'
    else: filecontents = 'File not found'
    return filecontents

# Loop to keep running the program unless told to exit
while not exit:
    print(options)
    choice = input('Enter your selection:\n').lower()
    if choice == 'e':
        message = input('Enter the message:\n')
    elif choice == 'v':
        print('The message is:',message)
    elif choice == 'l':
        print('List of files: 42.txt, 1015.txt')
    elif choice == 'd':
        print(displayfile(input('Enter the filename:\n')))
    elif choice == 'x':
        exit = True
        print('Goodbye!')
