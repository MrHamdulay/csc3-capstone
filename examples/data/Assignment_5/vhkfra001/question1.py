# Assignment 5
# Program to simulate a BSS user interface
# Frans van Hoek
# 14 April 2014

message = "no message yet"

selection = (input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")).lower()

while selection != 'x':
    
    if selection == 'e':
        message = input("Enter the message:\n")
        
        
    elif selection == 'v':
        print('The message is:', message)
        
    
    elif selection == 'l':
        print("List of files: 42.txt, 1015.txt")
        
        
    elif selection == 'd':
        file = (input("Enter the filename:\n")).lower()
    
        if file == '42.txt':
            print("The meaning of life is blah blah blah ...")
    
        
        elif file == '1015.txt':
            print("""Computer Science class notes ... simplified
Do all work
Pass course
Be happy""")
            
        else:
            print("File not found")    
        
        
    selection = (input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")).lower()
        

print("Goodbye!")

    