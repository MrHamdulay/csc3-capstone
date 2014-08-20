# program to create and stored text in files
#romelon chetty(chtrom001)
#13 april 2014
#question.py

nut= 'Z'
message= 'no message yet' #default message

while nut !='X': #if use wants to exit they can type in x or X
    print('Welcome to UCT BBS')
    print('MENU')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')              
    nut=input('Enter your selection:\n') #selection input required for user
    if nut=='X' or nut=='x':
        print('Goodbye!')
        break                           #program will stop here if users wants to exit
    elif nut=='E' or nut=='e':
        message=input('Enter the message:\n') #this will allow the uers to enter a message
    elif nut=='V' or nut=='v':     
        print('The message is:', message)    #allow to view saved message
    elif nut=='L' or nut=='l':
        print('List of files:', '42.txt,','1015.txt')  # this will display list of files stored
    elif nut=='D' or nut=='d':          
        mefile=input('Enter the filename:\n')        # allows users to slect a file they want to display
        if mefile!='1015.txt' and mefile!='42.txt':
            print('File not found')             # only to files exist here
            continue
        elif mefile=='1015.txt':
            print('Computer Science class notes ... simplified')
            print('Do all work')
            print('Pass course')
            print('Be happy') # text in file selected
        elif mefile=='42.txt':
            print('The meaning of life is blah blah blah ...') # text in file selected
            
        
    
    
        