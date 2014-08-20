'''program for BBS
nicole henning
due 17 april'''

#make intro
def intro ():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
  

intro()

#ask for selction
selection = input("Enter your selection:\n")
message = "no message yet" 
selection=selection.lower()

#continue asking until x
while selection != "x":
     
    #for message   
    if selection =="e":
        message = input("Enter the message:\n")
    
    if selection =="v":
        if message =="no message yet":
            print("The message is:", message)
        else:
            print("The message is:", message)
    
    #for files
    elif selection == "l":
        print("List of files: 42.txt, 1015.txt")
        
    elif selection == "d":
        filename = input ("Enter the filename:\n")
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    
    #continue asking   
    intro()
    selection = input("Enter your selection:\n")
    
#end
if selection =="x":
    print("Goodbye!")
