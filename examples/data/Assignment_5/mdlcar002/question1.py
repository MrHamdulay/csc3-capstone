#Assignment5 Question1
#MDLCAR002


def display():
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
   
    x=input("Enter your selection:\n")
    x=x.upper()
    return x

def main():
    choice=""
    message="no message yet"
    file="File not found"    
#while the user does not exit    
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
            
        
        
    
    