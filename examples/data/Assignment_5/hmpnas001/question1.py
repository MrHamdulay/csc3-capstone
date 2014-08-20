def main():
   
    message="no message yet"
    selection=""
    while selection!="X":
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection = input("Enter your selection:\n") 
        
        if selection =="E" or selection=="e":
                message=input("Enter the message:\n")
                
        elif selection == "V" or selection=="v":
                print("The message is:",message)
        elif selection=="l" or selection=="L":
                print("List of files: 42.txt, 1015.txt")
        elif selection=="d" or selection=="D":
                filename=input("Enter the filename:\n")
                if filename=="42.txt":
                        print("The meaning of life is blah blah blah ...")
                elif filename=="1015.txt":
                        print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                else:
                        print("File not found")
        if selection=="x" or selection=="X":
                print("Goodbye!")
                break
main()                 
        
        
        
    
    
    