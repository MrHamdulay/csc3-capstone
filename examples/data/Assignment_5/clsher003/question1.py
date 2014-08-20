"""Program to simulate a simple BBS
herman claassens
13 april 2014"""

message2='no message yet'
z=1 # sentinel , if z=1 the loop will end
while z !=0:
    # print options
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
 # prompt user for selection
    selection=input("Enter your selection:\n")
 # depending on selection , perform certain task  
    if selection=='E' or selection=='e':
        message1=input("Enter the message:\n")
        message2=''
        message2+=message1
        z+=1 # add number to z to continue loop
    elif selection=='V' or selection=='v':
        print("The message is:",message2)
        z+=1
    elif selection=='L' or selection=='l':
        print("List of files: 42.txt, 1015.txt")
        z+=1
    elif selection=='D' or selection=='d':
        file_names=input("Enter the filename:\n")
        if file_names== '42.txt':
            print("The meaning of life is blah blah blah ...")
        elif file_names== '1015.txt':
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else: print("File not found")
        z+=1
    elif selection=='x' or selection=='X':
        print("Goodbye!")
        z=0 # end loop 
        
        
    
    
           
        
    
    
    