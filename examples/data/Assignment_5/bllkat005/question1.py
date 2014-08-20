# Kate Bell
# BLLKAT005
# 16 April 2014 

# Initiate variables 
message= "no message yet"
file42 = "The meaning of life is blah blah blah ..."
file1015 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"

# Print options and ask user to choose
choice = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")[0]

#loop until user enters "X"
while True: 
    if choice == 'E' or choice == 'e' :
        message = input("Enter the message:\n")
        
    elif choice == 'V' or choice == 'v':
        print("The message is:",message)
        
    elif choice == 'L' or choice == 'l':
        print("List of files: 42.txt, 1015.txt")
        
    elif choice == 'D' or choice == 'd':
        filename = input("Enter the filename:\n")
        if filename == '42.txt':
            print(file42)
        elif filename == '1015.txt':
            print(file1015)
        else: print("File not found")
            
    elif choice == 'X' or choice == 'x':
        print("Goodbye!")
        break
    
    choice = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")[0]


    



