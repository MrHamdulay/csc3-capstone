"""Internet ,public Bulletin Board Systems (BBS)  to exchange information (messages/files) in a community of users
katlego gaveni
15th April 2014"""


#text line
def BBS():
    

    print("Welcome to UCT BBS \nMENU") #first display of message
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")        
    user_info=input("Enter your selection:\n").upper() #selection from the user
    msg="" #creation of emty string to store the message
    while user_info != "X": #while the user has not selected x this will loop continuously asking the user for input
        files=["1015.txt","42.txt"]#stored files
        text=["Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy","The meaning of life is blah blah blah ..."]#corresponding text to stored files        
        
        if user_info == "E": #creating a stored message
                    
                    msg=input("Enter the message:\n")        
        
     
        elif user_info== "V": #viewing of stored message
            if len(msg)>0:
                print("The message is:",msg)
            elif len(msg) == 0:
                print("The message is: no message yet")
       
        
        elif user_info == "D": #display of files
            choice=input("Enter the filename:\n")
            if choice == files[0]:
                print(text[0])
            elif choice==files[1]:
                print(text[1])
            else:
                print("File not found")
        
        elif user_info== "L":
            print("List of files:"," ",files[1],","," ",files[0],sep="")#listing of files
        
        
        
        print("Welcome to UCT BBS \nMENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        
       
        user_info=input("Enter your selection:\n").upper()
        
 
    print("Goodbye!")#exit from loop if option "X" is selected
    

BBS()