"""Sphiwe Muthembi
Std no: MTHSPH007
Question 1 - Assignment 5"""

def welc():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")    
    
    
def main():
    welc()
    
    message= ""
    cnt = True
    
    
    while cnt:
        selection= input("Enter your selection:\n")
        
        if selection == "e" or selection == "E":
            message = input("Enter the message:\n")
            welc()
            
        elif selection == "v" or selection == "V":
            if message== "":
                print("The message is: no message yet")
                
            else:
                print("The message is:",message)
            welc()
                
        elif selection == "l" or selection == "L":
            print("List of files: 42.txt, 1015.txt")
            welc()
            
        elif selection == "d" or selection == "D":
            name= input("Enter the filename:\n")
                
            if name == "42.txt":
                print("The meaning of life is blah blah blah ...")
            
            elif name == "1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work\nPass course\nBe happy")
                
            else:
                print("File not found")   
            welc()
            
        elif selection == "x" or selection == "X":
            print("Goodbye!")
            cnt = False
        
main()