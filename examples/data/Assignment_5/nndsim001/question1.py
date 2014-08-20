# This program simulates a simple Bulletin Board Systems (BBS) 
# with one stored message and 2 fixed files as indicated in the output
# A default message of "no message yet"; 
# and if a file cannot be located, output "File not found".

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 15 April 2014

# Display the Menu
def DisplayMenu():    
    menu = "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it"    
    
    return menu

# Ask user to enter something
def Selection():
    selected = input("Enter your selection:\n")
    selected = str(selected).lower()
    
    return selected


# The default message
message = "no message yet"

files = ["42.txt","1015.txt"]


# Asks user to choose item on the menu
print(DisplayMenu())
select = Selection()

# Exits the BBS
if select == "x":
    print("Goodbye!")
        
while select != "x":
    # Asks user to enter a new message
    if select == "e":
        message = input("Enter the message:\n")
        print(DisplayMenu())
        select = Selection()        
    
    # Displays the current message
    if select == "v":
        print("The message is:",message)
        print(DisplayMenu())
        select = Selection()        
       
    # Displays the current files stored
    if select == "l":
        print("List of files:",", ".join(files))
        print(DisplayMenu())
        select = Selection()      
    
    # Asks user to enter one file to display its content
    if select == "d":
        filename = input("Enter the filename:\n")
        
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
        print(DisplayMenu())
        select = Selection() 
    
    # Exit the BBS 
    if select == "x":
        print("Goodbye!")
        break
    


#Sample I/O:

# Welcome to UCT BBS
# MENU
# (E)nter a message
# (V)iew message
# (L)ist files
# (D)isplay file
# e(X)it
# Enter your selection:
# E
# Enter the message:
# test message
# Welcome to UCT BBS
# MENU
# (E)nter a message
# (V)iew message
# (L)ist files
# (D)isplay file
# e(X)it
# Enter your selection:
# V
# The message is: test message
# Welcome to UCT BBS
# MENU
# (E)nter a message
# (V)iew message
# (L)ist files
# (D)isplay file
# e(X)it
# Enter your selection:
# X
# Goodbye!


#Sample I/O:

# Welcome to UCT BBS
# MENU
# (E)nter a message
# (V)iew message
# (L)ist files
# (D)isplay file
# e(X)it
# Enter your selection:
# l
# List of files: 42.txt, 1015.txt
# Welcome to UCT BBS
# MENU
# (E)nter a message
# (V)iew message
# (L)ist files
# (D)isplay file
# e(X)it
# Enter your selection:
# d
# Enter the filename:
# 42.txt
# The meaning of life is blah blah blah ...
# Welcome to UCT BBS
# MENU
# (E)nter a message
# (V)iew message
# (L)ist files
# (D)isplay file
# e(X)it
# Enter your selection:
# d
# Enter the filename:
# 1015.txt
# Computer Science class notes ... simplified
# Do all work
# Pass course
# Be happy
# Welcome to UCT BBS
# MENU
# (E)nter a message
# (V)iew message
# (L)ist files
# (D)isplay file
# e(X)it
# Enter your selection:
# d
# Enter the filename:
# 1016.txt
# File not found
# Welcome to UCT BBS
# MENU
# (E)nter a message
# (V)iew message
# (L)ist files
# (D)isplay file
# e(X)it
# Enter your selection:
# x
# Goodbye!