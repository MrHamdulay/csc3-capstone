"""UCT BBS prompts
Telisha Ramlall
11/04/2014"""


prompt = "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it"
y = ""
print(prompt)

terminate = 0

while terminate == 0:
    selection = input("Enter your selection:\n").upper()
    
    if selection == "X":
        print("Goodbye!")
        break
    
    else:
        while selection != "X":
            if selection == "E":
                y = input("Enter the message:\n")
                print(prompt)
                break
            
            elif selection == "V":
                if y == "":
                    print("The message is: no message yet")
                    print(prompt)
                    break
                
                else:
                    print("The message is:", y)
                    print(prompt)
                    break
                
            elif selection == "L":
                print("List of files: 42.txt, 1015.txt")
                print(prompt)
                break
            
            elif selection== "D":
                filename = input("Enter the filename:\n")
                if filename == "42.txt":
                    print("The meaning of life is blah blah blah ...")
                    print(prompt)
                    break
                
                elif filename == "1015.txt":
                    print("Computer Science class notes ... simplified")
                    print("Do all work")
                    print("Pass course")
                    print("Be happy")
                    print(prompt)
                    break
               
                else:
                    print("File not found")
                    print(prompt)
                    
                    break
            elif selection == "X" or selection == "x":
                terminate == -1
    

            
        