#Program to simulate a Bulletin Board System
#Kiran Desraj - DSRKIR001
#12 April 2014

#content of text files
text_file_1 = "The meaning of life is blah blah blah ..."
text_file_2 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"

selection ='' #makes selection a string
mes ='' #makes mes a string
#prints menu if not asked to exit
while selection !='X' and selection !='x':
    while selection!='X' and selection !='x':#Stops program when 'x' is entered
        #if exit option isn't chosen, menu is printed
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection=input("Enter your selection:\n")#User enters option
        #executes selection
        if selection=='e'or selection =='E':
            mes = input("Enter the message:\n")    
        if selection=='v'or selection =='V':
            if(mes != ""):
                print("The message is:",mes)
            else:
                print("The message is: no message yet")
        if selection=='l'or selection =='L':
            print("List of files: 42.txt, 1015.txt")
        if selection=='d'or selection =='D':
            filename=input("Enter the filename:\n")
            if(filename=="42.txt"):
                print(text_file_1)
            elif(filename=="1015.txt"):
                print(text_file_2)
            else:
                print("File not found")
    print("Goodbye!")
    

