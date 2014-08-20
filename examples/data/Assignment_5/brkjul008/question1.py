"""UCT BBS
Julia Breakey
15 April 2014"""

#menu and selection
ans = ""
msg = ""
list1 = ["42.txt", "1015.txt"]
while ans!="x":
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")        
        ans=input("Enter your selection:\n")
        #choosing a function 
        if ans =="E" or ans == "e": 
                msg=input("Enter the message:\n")
        elif ans =="V" or ans == "v":
                if msg == "":
                        print("The message is: no message yet")
                else: print("The message is:", msg)
        elif ans == "L" or ans == "l":
                print("List of files: 42.txt, 1015.txt")
        elif ans == "D" or ans =="d":
                file=input("Enter the filename: \n")
                if file == "42.txt":
                        print("The meaning of life is blah blah blah ...")
                elif file == "1015.txt":
                        print("Computer Science class notes ... simplified")
                        print("Do all work")
                        print("Pass course")
                        print("Be happy")
                else: print("File not found")
                
#when X is chosen and loop cuts
print("Goodbye!")