#Kovlin Perumal

#Print Menu
print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")

message = "no message yet"
#initialize selection variable
sel = input("Enter your selection:\n") 

#Close if sel = X
if sel == 'X' or sel == 'x':
    print("Goodbye!")
        
while(sel!='X' and sel!='x') :
    if sel == 'E' or sel == 'e':
        message = input("Enter the message:\n")#Enter message
    
    if sel == 'V' or sel == 'v':
        print("The message is:", message)#View message
    
    if sel == 'L' or sel == 'l' :
        print("List of files: 42.txt, 1015.txt")

    if sel == 'D' or sel == 'd': #Display contents of text files
        fName = input("Enter the filename:\n")
        
        if fName == '42.txt':
            myfile = open("42.txt", 'r')
            for line in myfile: print(line,end = '')
            print()
        elif fName == '1015.txt':
            myfile = open("1015.txt", 'r')
            for line in myfile: print(line,end = '')
            print()
        else:
            print("File not found")
            
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")             
            
    sel = input("Enter your selection:\n") 
    
    if sel == 'X' or sel == 'x':
        print("Goodbye!")
        