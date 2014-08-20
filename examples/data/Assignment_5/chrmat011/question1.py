import os

sel = ''

message = 'no message yet'

while sel != 'x':
    print('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:')
    sel = input('')
          
    if sel in 'eE':
        message = input('Enter the message:\n')

    elif sel in 'vV':
        print('The message is:', message)

    elif sel in 'lL':
        text_files = []
        for i in os.listdir():
            if i[len(i)-3:len(i)] == 'txt':
              text_files.append(i)
        text_files = text_files[::-1]
        print('List of files:',', '.join(text_files))

    elif sel in 'dD':
        file_name = input('Enter the filename:\n')
        try:
            file = open(file_name, 'r')
            print(file.read())
        except:
            print('File not found')

    elif sel in 'xX':
        print('Goodbye!')

          
