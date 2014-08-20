# a program to simulate a simple BBS with one stored message and 2 fixed files
# joshua gullan
# 16 April 2014

def main():
    selection=""
    message=""
    while selection!="X" or "x":
        print("Welcome to UCT BBS\nMENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection= input("Enter your selection:\n")
        
        
        if selection == "E" or selection == "e":
            message=input("Enter the message:\n") 
            
        elif selection == "V" or selection == "v":
            if message=="":
                print("The message is: no message yet")
            else:
                print("The message is:", message)
            
        elif selection == "L" or selection == "l":
            print("List of files: 42.txt, 1015.txt")
            
        elif selection == "D" or selection == "d":
            file_selection=input("Enter the filename:\n")
            
            if file_selection == "42.txt":
                print("The meaning of life is blah blah blah ...")
                
            elif file_selection == "1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            
            else:
                print("File not found")
                
            
        elif selection=="X" or selection=="x":
            break
    print("Goodbye!")
            

main()
