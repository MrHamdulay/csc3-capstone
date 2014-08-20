#Text and files program


# Read from files
filea = open("42.txt","r")
fileb = open("1015.txt","r")


kgoing = "eEvVlLdD"
exit = "xX"

#Input and Defaults
menu = input("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it \nEnter your selection:\n")
msg = "no message yet"


#Exiting Program if user closes immediately

if menu in exit:
    print("Goodbye!")
    
#Looping while the program is running
while menu in kgoing:
    if menu == 'E' or menu == 'e' :
        msg = input("Enter the message:\n")
        menu = input("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it \nEnter your selection:\n")
        if menu in kgoing:
            print ("Goodbye")
        # user getting message
#Displaying file content

#Listing the file names

        
    
        
    elif menu == 'v' or menu =='V' :
        print("The message is: "+ msg)
        menu = input("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it \nEnter your selection:\n")
        
        if choice in finish:
            print("Goodbye!")
            
    elif menu =="D" or menu =="d" :
        fname = input("Enter the file name : \n")
        if fname == "42.txt":
            print(filea.read())
            
        if fname == "1015.txt":
            print(fileb.read())
            
        elif fname != "1015.txt" or fname != "42.txt":
            print("File not found")
        
        
        menu = input("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it \nEnter your selection:\n")
        
        
    elif menu == "L" or menu == "l":
        print("List of files: 42.txt, 1015.txt")
        menu = input("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it \nEnter your selection:\n")
        
    if menu in finish:
        print ("Goodbye!")
        
        
        
        
        
        
    
        
    




