"""Text-based program to allow user to select options 
continuously until a specific task has been chosen
Ringo Shima
14/4/14"""
def main():
    menu = print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it", sep="\n")
    ans = " "
    list = "List of files: 42.txt, 1015.txt"
    ans = input("Enter your selection:\n")
    f1 = "42.txt"
    f2 = "1015.txt"
    message = "no message yet"
    while ans != "stop":
       
        if ans == 'e' or ans == 'E':
            message = input("Enter the message:\n")
            
            
            print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it", sep="\n")
            ans = input("Enter your selection:\n")
            
        elif ans == "v" or ans == "V":
            
            print ("The message is:", message)
            print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it", sep="\n")
            ans = input("Enter your selection:\n")
        elif ans == "l"or ans== "L":
            print(list)
            print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it", sep="\n")
            ans = input("Enter your selection:\n")
        elif ans == "d" or ans == "D":
            file = input("Enter the filename:")
            
            
            if file == "42.txt":
                print("\n" + "The meaning of life is blah blah blah ...")
                
                
            elif file  == "1015.txt":
                print ("\n" + "Computer Science class notes ... simplified", "Do all work", "Pass course", "Be happy", sep="\n")
                
        
            elif file != "42.txt" or file != "1015.txt":
                print("\n" + "File not found")
                
                
            print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it", sep="\n")
            ans = input("Enter your selection:\n")
        
        elif ans== "x" or ans == "X":
            print("Goodbye!")
            break
                
                
            
main()
