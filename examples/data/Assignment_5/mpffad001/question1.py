#a program to simulate a simple BBS
#fadzai mupfunya
#13 April 2014

def disp_list(): #displays the main menu
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")

def fourtyTwo_txt(): #for the 42.txt file
    print("The meaning of life is blah blah blah ...")

def tenFifteen_txt(): #for the 1015.txt file
    print("Computer Science class notes ... simplified")
    print("Do all work")
    print("Pass course")
    print("Be happy")

def selection(): #allows the user to selcet from the different files
    mess=''
    while True:
        disp_list()
        S=input("Enter your selection:""\n")
        if S=="E" or S=='e':
            mess=input("Enter the message:" "\n")
        elif S=="V" or S=="v":
            if mess=="":
                print("The message is: no message yet") #when there hasnt been a message that has been typed
            else:
                print("The message is:",mess)
        elif S=="X" or S=="x":
            print("Goodbye!")
            break
        elif S=="L" or S=="l":
            print("List of files: 42.txt, 1015.txt")
        elif S=="d" or S=="d": 
            file=input("Enter the filename:" '\n')
            if file=="42.txt":
                fourtyTwo_txt()
            elif file=="1015.txt":
                tenFifteen_txt()
            else:
                print("File not found")
                
selection()