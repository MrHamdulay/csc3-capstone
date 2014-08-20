option=""#Initialise option
message=""
txt1="The meaning of life is blah blah blah ..."#Store 42.txt as a string
txt2="Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"#Store 1015.txt as a string
while(option!='X' and option !='x'):#Stops program when 'x' is entered
    #Print menu
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    option=input("Enter your selection:\n")#User enters option
    #Perform actions according to user's selection
    if(option=='e'):
        message=input("Enter the message:\n")    
    if(option=='v'):
        if(message!=""):
            print("The message is:",message)
        else:
            print("The message is: no message yet")
    if(option=='l'):
        print("List of files: 42.txt, 1015.txt")
    if(option=='d'):
        filename=input("Enter the filename:\n")
        if(filename=="42.txt"):
            print(txt1)
        elif(filename=="1015.txt"):
            print(txt2)
        else:
            print("File not found")
print("Goodbye!")


