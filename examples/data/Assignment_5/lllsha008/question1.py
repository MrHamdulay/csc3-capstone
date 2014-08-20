import glob

cango = 'Y'
message = 'no message yet'

while cango != 'X': #sentinel
    #input messages
    print('Welcome to UCT BBS')
    print('MENU')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')
    print('Enter your selection:')
    cango = input()
    if (cango in 'Xx'):
        print('Goodbye!')
        #just breaks loop. Could have just done nothing
        break
    elif cango in 'Ee':
        #checks for message to change by
        message = input('Enter the message:\n')
    elif (cango in 'Vv'):
        #output stored message
        print('The message is:', message)
    elif cango in 'Ll':
        #look for files in current directory
        print('List of files:', ', '.join(glob.glob("*.txt")[::-1]))
    elif cango in 'Dd':
        #gets filename
        myfile = input('Enter the filename:\n')
        try:
            #tries to open and read
            myfile = open(myfile, 'r')
            for x in myfile:
                print(x, end = '')
        except:
            #otherwise gives failure message
            print('File not found')
            continue
