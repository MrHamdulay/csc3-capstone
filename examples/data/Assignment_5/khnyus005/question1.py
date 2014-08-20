"""Bulletin Board System
Yusuf Khan
17 April 2014"""

#declaration of variables
chorus = """Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:\n"""
message = 'no message yet'
files = ['42.txt','1015.txt']
exit = False

#initialization of loop
while exit == False:
    choice = input(chorus)
    if choice =='e':
        message = input("Enter the message:\n")
    elif choice == 'v':
        print("The message is: "+message)
    elif choice == 'l':
        print('List of files: '+files[0]+', '+files[1])
    elif choice == 'd':
            file = input("Enter the filename:\n")
            if file not in files:
                print("File not found")
            else:
                if file == files[0]: 
                    print('The meaning of life is blah blah blah ...')
                else:
                    print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
    else:
        exit = True
        print("Goodbye!")
        #statement to break loop and exit
    