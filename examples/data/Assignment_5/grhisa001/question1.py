""" Bella gorham
question1
message function
14/04/2014"""

def main():
    
        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        choice= input("Enter your selection:\n")
        message = ""
                 
    
        while choice != "X" or choice == "x":
                if choice == "V" or choice == "v":
                        if message:
                                print("The message is:",message)
                                                
                                print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                                choice= input("Enter your selection:\n"   )         
                        else:
                                print("The message is: no message yet")
                                print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                                choice= input("Enter your selection:\n"  )                       
                if choice == "E" or choice == "e":
                        
                        message = input("Enter the message:\n")
                        
                        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                        choice = input("Enter your selection:\n")
                        
                   
                if choice == "L" or choice == "l":
                        print("List of files: 42.txt, 1015.txt")
                        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                        choice= input("Enter your selection:\n" )           
                if choice == "D" or choice == "d":
                        file = input("Enter the filename:\n")
                        if file == "1015.txt":
                                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                                print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                                choice= input("Enter your selection:\n"   )             
                        elif file == "42.txt":
                                print("The meaning of life is blah blah blah ...")
                                print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                                choice= input("Enter your selection:\n"  )              
                        else:
                                print("File not found")
                                print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                                choice= input("Enter your selection:\n"    ) 
                if choice == "X" or choice == "x":
                        break
        print( "Goodbye!")                
        
        
           
main()
    
    
        
