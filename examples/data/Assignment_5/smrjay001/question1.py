"""
Assignment 5 - Question 1
A simple user interface.
Jayan Smart
April 2014
"""

#Starting values and lists:
message = "no message yet"
filelist = ["42.txt", "1015.txt"]

#Loop untill exit prompt is given:
X = False
while X == False:
    print("""Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it""")
    #Recieve user input:
    imp=input("Enter your selection:\n")
    imp=imp.upper()
    
    #Check for valid input:
    if imp not in ["E", 'V', 'L', 'D', 'X']:
        continue
    else:
        if imp == 'E':
            message = input("Enter the message:\n")
        elif imp == 'V':
            print("The message is:", message)
        elif imp == "L":
            print("List of files: "+filelist[0]+ ", "+filelist[1])
        elif imp == "D":
            file = input("Enter the filename:\n")
            if file not in filelist:
                print("File not found")
            else:
                if file == "42.txt":
                    print("The meaning of life is blah blah blah ...")
                else:
                    print("""Computer Science class notes ... simplified
Do all work
Pass course
Be happy""")
        elif imp == "X":
            X = True
            print("Goodbye!")
