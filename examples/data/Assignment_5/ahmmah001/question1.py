a="42.txt"
b="1015.txt"

menu="Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it"
print(menu)
selection=input("Enter your selection:\n")
selection=selection.upper()
while selection != "X":
    
    if selection=="E":
        msg=input("Enter the message:\n")
        print(menu)
        selection=input("Enter your selection:\n")
        selection=selection.upper()
        
        if selection=="V":
            print("The message is:",msg)
            print(menu)
            selection=input("Enter your selection:\n")   
            selection=selection.upper()
            
    elif selection=="V":
        print("The message is: no message yet")
        print(menu)
        selection=input("Enter your selection:\n")   
        selection=selection.upper()        
            
    elif selection=="L":
        print("List of files: ",a,", ",b,sep="")
        print(menu)
        selection=input("Enter your selection:\n")      
        selection=selection.upper()
        
        if selection=="D":
            while selection=="D":
                file=input("Enter the filename:\n")
                if file==a:
                    print("The meaning of life is blah blah blah ...")
                    print(menu)
                    selection=input("Enter your selection:\n") 
                    selection=selection.upper()
                    
                elif file==b:
                    print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                    print(menu)
                    selection=input("Enter your selection:\n")    
                    selection=selection.upper()
                    
                else:
                    print("File not found")
                    print(menu)
                    selection=input("Enter your selection:\n")          
                    selection=selection.upper()
        
    
else:
    print("Goodbye!")
        

