
def main():
    end="true"
    message="no message yet"
    while end=="true":
        print ("Welcome to UCT BBS")
        print ("MENU") 
        print ("(E)nter a message")
        print ("(V)iew message")
        print ("(L)ist files")
        print ("(D)isplay file")
        print ("e(X)it")
        
        selection=(input("Enter your selection:\n")).lower()
        
        if selection=="e":
            message=input("Enter the message:\n")  
        
        elif selection=="v":
            print ("The message is:", message)    
        
        elif selection == "l":
            print ("List of files: 42.txt, 1015.txt") 
            
        elif selection == "d":
            filename=input("Enter the filename:\n")
            if filename=="42.txt":
                print("The meaning of life is blah blah blah ...") 
            elif filename=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            elif filename!="42.txt" and "1015.txt":
                print("File not found")       
        
        elif selection == "x":
            end="false"
    print("Goodbye!")

main()

        
        

