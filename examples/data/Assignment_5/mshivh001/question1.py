#A function that a simple BBS with one stored message and 2 fixed files
#Maisha Ivha
#15 April 2014

#the welcoming message
def BBS():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
x="EVLDX" #creating a new string which can be easily sliced

#a function of getiing input from user
def file():   
    z="no message yet" # default message
    b="file not found"
    
    #use an infinity loop
    while True:
        BBS()        
        y=input("Enter your selection: \n")
        if y==x[0] or y==x[0].lower():
            z=input("Enter the message: \n")
        if y==x[1] or y==x[1].lower():
            print("The message is:",z)
        if y==x[2] or y==x[2].lower():
            print("List of files: 42.txt, 1015.txt" )
        if y==x[3] or y==x[3].lower():
            h=input("Enter the filename: \n")
            if h=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif h=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")

            else:
                print("File not found")
        if y==x[4] or y==x[4].lower():
            print("Goodbye!")
            break # stop the loop from iterating
            
        
        
file()