#question 1: UCT BBS
#Galya Wolov
#16 April 2014

#smart variable statements outside of loop:
message= ("no message yet")
userinput=""

#start the menu of the bbs:
while True:
    #ask user for input:
    menu= ("Welcome to UCT BBS\nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file\ne(X)it")
    print(menu)
    userinput= input("Enter your selection:\n")
    #go through the menu and give specific outputs
    if userinput == "E" or userinput == "e":
        #specific to e or E
        message= input("Enter the message:\n")
    
    elif userinput == "V" or userinput == "v":
        #specific to v or V only after e
        print("The message is:", message)
    
    elif userinput == "l" or userinput == 'L':
        print("List of files: 42.txt, 1015.txt")
        #provides the neccessary steps after l or L is chosen
    elif userinput == 'd' or userinput == 'D':
        #provides all the options if d or D is chosen. They are a bit more complicated and supply three different decisions. 
        filechoice = input("Enter the filename:\n")
        if filechoice == '42.txt':
            print("The meaning of life is blah blah blah ...")
        elif filechoice == '1015.txt':
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
        
    #exits out of the loop and ends program
    elif userinput == "x" or userinput == "X":
        print("Goodbye!")
        break
    
    