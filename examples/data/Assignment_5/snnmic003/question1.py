'''BBS Simulator
Michael Sanne
2014/04/15'''

#Initialise variables to allow use before assignment
option = "a"
message = ""
file1015 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
file42 = "The meaning of life is blah blah blah ..."
#Loop to repeat options until the user ends by X
while option[0].upper() != 'X':
    print ("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    option = input ("Enter your selection:\n")    
    if option[0].upper() == 'E':
        message = input ("Enter the message:\n")
    if option[0].upper() == 'V':
        if message == "":
            print ("The message is: no message yet")
        else: print ("The message is: " + message)
    if option[0].upper() == 'L':
        print ("List of files: 42.txt, 1015.txt")
    if option[0].upper() == 'D':
        fileSelection = input("Enter the filename:\n")
        if (fileSelection == "42.txt"):
            print (file42)
        elif (fileSelection == "1015.txt"):
            print (file1015)
        else: print ("File not found")
        
print ("Goodbye!")