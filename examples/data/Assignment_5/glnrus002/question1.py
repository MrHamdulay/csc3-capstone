#glnrus002
#question 1
#16 April
def Options():#displays menu
    choice=""
    msg="no message yet"
    while choice !="X":#if user enters x, program terminates
#Displays list        
        print("Welcome to UCT BBS")
        print("MENU")   
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        choice=input("Enter your selection:\n").upper()

#operates on user input
        if choice =="E":
            msg=enter()
            
        elif choice=="V":
            view(msg)
            
        elif choice=="L":
            list()
            
        elif choice== "D":
            ope()
            
    print("Goodbye!")
        
def enter():#enter new msg
    msg=input("Enter the message:\n")
    return msg
    
def view(msg):#print msg
    print("The message is:",msg)
    
def list():
        print("List of files: 42.txt, 1015.txt")
    
def ope(): #open file
        fname=input("Enter the filename:\n")
        if fname!="1016.txt":
            infile = open(fname, "r")
            print(infile.read())       
            infile.close
        else:
            print("File not found")
        
if __name__== "__main__":

    Options()