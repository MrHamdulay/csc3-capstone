# program to simulate a simple Bulletin Board System
# Gadija Moollagie
# 14 April 2014

def displayName(): # defines the menu that will be displayed every time 
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
def main():
    while True: # continues through the loop body as long as expression remains true
        displayName() # displays this through every iteration
        selection = input("Enter your selection:\n") # displays this through every iteration
        selection = selection.upper()
        if selection == 'E':
            message = input("Enter the message:\n")
            
        elif selection == 'V':
            try:
                print("The message is:", message)
            except(NameError): 
                print("The message is: no message yet") 
                # exception raised if there is a NameError and variable cannot be found
                
        elif selection == 'L':
                print("List of files: 42.txt, 1015.txt")
                    
        elif selection == 'D':
            fileName = input("Enter the filename:\n")
            if fileName == '42.txt':
                print("The meaning of life is blah blah blah ...")   
            elif fileName == '1015.txt':
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else: # if fileName is not in list
                print("File not found")
                
        elif selection == 'X':
            print("Goodbye!")
            break # breaks out of loop
main()