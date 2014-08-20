"""Naveet Baitchu
com sci menu programme
17 April 2014"""



def main():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    message = ""

    y =input("Enter your selection: \n")
    while y!="x":

        if y == "e":
            message = input("Enter the message: \n")
            
        elif y == "v":
            print("The message is: ",message,sep="")
            
        elif y == "l":
            print("List of files: 42.txt, 1015.txt")
            
        elif y == "d":
            z = input("Enter the filename: \n")
            if z == "42.txt":
                print("The meaning of life is blah blah blah ...")
                
            elif z == "1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass Course")
                print("Be happy")
                
            else:
                print("File not found")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")  
        print("(D)isplay file")
        print("e(X)it")        
        y =input("Enter your selection: \n")                  
    
    if y == "x":
            print("Goodbye!")
      
        
        
        
        
main()