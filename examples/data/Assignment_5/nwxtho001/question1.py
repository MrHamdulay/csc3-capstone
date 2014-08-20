'''A simple BBS'''

message = 'no message yet'
import glob
files = glob.glob ('*.txt')

while True:
    print ('''Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:''')
    inp = input ('').upper()
    if inp == 'E':
        message = input ('Enter the message:\n')
    elif inp == 'V':
        print ('The message is:', message)
    elif inp == 'L':
        print ('List of files:', end = ' ')
        for file in range (len (files), 0, -1):
            if file == 1:
                print (files [file - 1])
            else:
                print (files [file - 1], end = ', ')
    elif inp == 'D':
        filename = input ('Enter the filename:\n')
        if filename in files:
            file = open (filename)
            print (file.read ())
        else:
            print ('File not found')
    elif inp == 'X':
            print ('Goodbye!')
            break    