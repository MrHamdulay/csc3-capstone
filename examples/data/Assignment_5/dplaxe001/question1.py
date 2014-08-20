#Axel du Plessis 14/04/2014
#BBS system using text files

while True:
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    
    choice = input("Enter your selection:\n") 
    
    if choice in "Ee":
        fileWrite = open("Message.txt","w")
        message = input("Enter the message:\n")
        fileWrite.write(message)
        fileWrite.close()
        
    elif choice in "Vv":
        fileRead = open("Message.txt","r")
        print("The message is: "+fileRead.read())
        
    elif choice in "Ll":
        print("List of files: 42.txt, 1015.txt")
            
    elif choice in "Dd":
        filename = input("Enter the filename:\n")
        try:
            fileRead = open(filename,"r")
            print(fileRead.read())  
        except IOError or FileNotFoundError:
            print("File not found")
        
    elif choice in "Xx":
        print("Goodbye!")
        break