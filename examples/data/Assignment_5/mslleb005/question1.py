i="m"

message="no message yet"
while i != "X" or i!="x":
                      print("Welcome to UCT BBS")
                      print("MENU")
                      E=print("(E)nter a message")
                      V=print("(V)iew message")
                      L=print("(L)ist files")
                      D=print("(D)isplay file")
                      X=print("e(X)it")
                      i=input("Enter your selection:\n")
                      if i == "E" or i=="e":
                                            message=input("Enter the message:\n")
                      if i=="V" or i=="v":
                                            print("The message is:",message)
                      if i=="L" or i=="l":
                                            print("List of files: 42.txt, 1015.txt")
                      if i=="d" or i=="D": 
                                            f=input("Enter the filename:\n")
                                            if f == "1015.txt":
                                                                  print("Computer Science class notes ... simplified")
                                                                  print("Do all work")
                                                                  print("Pass course")
                                                                  print("Be happy")
                                            elif f=="42.txt":
                                                                  print("The meaning of life is blah blah blah ...")
                                            else:
                                                                  print("File not found")
                      if i=="x" or i=="X":
                                            print("Goodbye!") 
                                            break
                      
            
        
    
    
        
    



    

