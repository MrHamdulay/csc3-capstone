#GVNMER006
#2014-04-16
def display():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    x=input("Enter your selection:\n")
    x=x.upper()
    return x

def main():
    choice=""
    message="no message yet"
    file="File not found"    
    while choice!="X":
        choice=display()
        if(choice=="E"):
            message=input("Enter the message:\n")
        elif(choice=="V"):
            print("The message is:",message)
        elif(choice=="L"):
            print("List of files: 42.txt, 1015.txt")
        elif(choice=="D"):
            fName=input("Enter the filename:\n")
            if(fName=="42.txt"):
                print("The meaning of life is blah blah blah ...")
            elif(fName=="1015.txt"):
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else:
                print(file)
                 
    else:
        print("Goodbye!")
                     
main()
            
        
        
    
    
