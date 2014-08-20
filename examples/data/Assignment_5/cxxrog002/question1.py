""" UCT BBS
Roger m Cox
16/04/2014"""


selection=""

mesg ="no message yet"

while selection.upper() !="X":
    #always prints this
    print("Welcome to UCT BBS")
    print("MENU")
    print ("(E)nter a message")
    print ("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection= input("Enter your selection:\n")
    if selection.upper()=="E" :
        mesg=input("Enter the message:\n")
    
        # renames mesg veriable
    if selection.upper()=="V" :
        print("The message is:",mesg)
    
    if selection.upper()=="L" :
        print("List of files: 42.txt, 1015.txt")
        
      #if it has to do with "d"  
    if selection.upper()=="D" :
        filename =input("Enter the filename:\n")
    
        if filename=="42.txt":
            print ("The meaning of life is blah blah blah ...")
            
        elif filename=="1015.txt" :
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
            
    if ( selection ==""):
        print ("no data")
print("Goodbye!")    