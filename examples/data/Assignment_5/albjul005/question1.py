""" UCT BBS program
Julian Albert
ALBJUL005
15-04-2014"""
#loop paramaters to end at exit
end = False
menu = "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n"
menu += "(L)ist files\n(D)isplay file\ne(X)it"
message = "no message yet"
#defines .txt file choices
def display_file(filename):
    if filename == '42.txt':
        filecontents = 'The meaning of life is blah blah blah ...'
    elif filename == '1015.txt':
        filecontents = 'Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy'
    else: filecontents = 'File not found'
    return filecontents
#main program of menu with options
while not end:
    print(menu)
    choice = input('Enter your selection:\n').lower() #.lower to run for all cases
    if choice == 'e':
        message = input('Enter the message:\n')
    elif choice == 'v':
        print('The message is:',message)
    elif choice == 'l':
        print('List of files: 42.txt, 1015.txt')
    elif choice == 'd':
        print(display_file(input('Enter the filename:\n'))) #runs display_file
    elif choice == 'x':
        end = True #ends the loop if input = 'x'
        print('Goodbye!') 
