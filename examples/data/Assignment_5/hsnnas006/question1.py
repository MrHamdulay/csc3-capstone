#UCT BBS Program
#by nasreen

#assign variables
menu = 'Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it'
options = ['E', 'V', 'L', 'D', 'X']
s = 'Enter your selection:\n'
message = 'no message yet'
files = ['42.txt', '1015.txt']
#initial selection
print(menu)
selection = input(s)
selection = selection.upper() #converts selection to uppercase

while not selection == 'X': #loop while user does not want to exit
    if selection == 'E':
        message = input('Enter the message:\n')
    if selection == 'V':
        print('The message is:', message, sep=' ')
    if selection == 'L':
        print('List of files: ', files[0], ', ', files[1], sep='')
    if selection == 'D':
        filename = input('Enter the filename:\n')
        if filename == files[0]:
            print('The meaning of life is blah blah blah ...')
        elif filename == files[1]:
            print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
        else:
            print('File not found')
    print(menu)   
    selection = input(s) #next selection from user
    selection = selection.upper()

#exits program    
print('Goodbye!')
