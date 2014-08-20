'''Program to simulate a simple BBS with one stored message and 2 fixed files
Sinead Urisohn
15 April 2014'''

#Print menu options
print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
#Get choice input
choice= input("Enter your selection:\n")
#change input to lowercase
choice=choice.lower()
#set default message
message="no message yet"
#set filename as empty variable
filename=""
#creat the 2 files
file1="The meaning of life is blah blah blah ..."
file2=["Computer Science class notes ... simplified","Do all work","Pass course","Be happy"]
#loop until user exits/enters 'x'
while choice !='x':
    #if user enters e
    if choice=='e':
        #get message
        message=input('Enter the message:\n')
        #if message empty tell user
        if message=="":message="no message yet"
    #if user enters v
    elif choice=='v':
        #print message
        print("The message is: "+message)
    #if user enters l
    elif choice=='l':
        #print list of files
        print("List of files: 42.txt, 1015.txt")
    #if user enters d
    elif choice=='d':
        #get filename input
        filename=input("Enter the filename:\n")
        #determine which file to print based on filename inut
        if filename=='42.txt':
            print(file1)
        elif filename=='1015.txt':
            for n in file2:
                print(n)
        #if user enters incorrect file
        else: print("File not found")
    #get choice input again for user to repeat BBS
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    choice= input("Enter your selection:\n")
    choice=choice.lower()    
#If user exits
print("Goodbye!")
        