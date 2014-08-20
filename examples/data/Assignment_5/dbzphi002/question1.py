#Thembekile Dubazana
#Assignment 5:Q1
#dbzphi002
#April 2014

message=""
while True:
    print('Welcome to UCT BBS')
    print('MENU')    
    Input=input('(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n')
    if Input =="X" or Input=="x":
        print('Goodbye!')
        break
    elif Input == "E" or Input == "e":
        message=input('Enter the message:\n')
    elif Input == "V" or Input == "v":
        if message=="":
            print('The message is: no message yet')
        else:
            print('The message is: ',message,sep="")
    elif Input == "L" or Input == "l":
        print('List of files: 42.txt, 1015.txt')
    elif Input == "D" or Input == "d":
        file=input('Enter the filename:\n')
        if file == "42.txt":
            print('The meaning of life is blah blah blah ...')
        elif file == "1015.txt":
            print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
        else:
            print('File not found')
            