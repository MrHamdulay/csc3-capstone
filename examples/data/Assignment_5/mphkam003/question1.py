"""simulate a BBS
Kamogelo Mphela
15 April 2014 """

m='no message yet' # defualt message
#get a message from the user
def msg():
    global m
    m=input("Enter the message:\n")
    return m
    

# define available lists     
def list():
    x = "42.txt"
    y =  "1015.txt"
    print("List of files: ", x,", ",y,sep="")

# display what is in the lists
def display():
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

# Interact with the user        
def main():
    
    while True:
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection = input("Enter your selection:\n")
        if selection == "x":
            print("Goodbye!")
            break
        elif selection == "e":
            msg()
        elif selection == "v":
            print("The message is:",m)
            
        
        elif selection == "l":
            list()
        elif selection == "d":
            display()
    
main()