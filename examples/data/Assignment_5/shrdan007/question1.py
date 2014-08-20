file1 = "42.txt"
file2 = "1015.txt"

print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")
a = input("Enter your selection:\n")
if a == "E" or a == "e":
     b = input("Enter the message:\n")
     a = input("Enter your selection:\n")
     if a == "V" or a == "v":
          print("The message is:", b)
          print("Welcome to UCT BBS")
          print("MENU")
          print("(E)nter a message")
          print("(V)iew message")
          print("(L)ist files")
          print("(D)isplay file")
          print("e(X)it")
          a = input("Enter your selection:\n")        
       
            
elif a == "V" or a == "v":
     print("The message is: no message yet")
     print("Welcome to UCT BBS")
     print("MENU")
     print("(E)nter a message")
     print("(V)iew message")
     print("(L)ist files")
     print("(D)isplay file")
     print("e(X)it")
     a = input("Enter your selection:\n")
     if a == "E" or a =="e":
          b = input("Enter the message:\n")
          print("Welcome to UCT BBS")
          print("MENU")
          print("(E)nter a message")
          print("(V)iew message")
          print("(L)ist files")
          print("(D)isplay file")
          print("e(X)it")          
          a = input("Enter your selection:\n")
          if a == "V" or a == "v":
               print("The message is:", b)
               print("Welcome to UCT BBS")
               print("MENU")
               print("(E)nter a message")
               print("(V)iew message")
               print("(L)ist files")
               print("(D)isplay file")
               print("e(X)it")
               a = input("Enter your selection:\n")
               if a == "X" or a == "x":
                    print("Goodbye!")
               
          
      
        
       
          

elif a == "X" or a == "x":
     print("Goodbye!")

if a == "L" or a == "l":
     print("List of files:", file1 + ","+" " + file2)
     print("Welcome to UCT BBS")
     print("MENU")
     print("(E)nter a message")
     print("(V)iew message")
     print("(L)ist files")
     print("(D)isplay file")
     print("e(X)it")
     a = input("Enter your selection:\n")
     if a == "D" or a == "d":
          c = input("Enter the filename:\n")
          if c == file1:
                    print("The meaning of life is blah blah blah ...")
          elif c == file2:
                    print("Computer Science class notes ... simplified")
                    print("Do all work")
                    print("Pass course")
                    print("Be happy")
          else:
               print("File not found")
               print("Welcome to UCT BBS")
               print("MENU")
               print("(E)nter a message")
               print("(V)iew message")
               print("(L)ist files")
               print("(D)isplay file")
               print("e(X)it")
               a = input("Enter your selection:\n")
               if a == "D" or a == "d":
                    c = input("Enter the filename:\n")
                    if c == file1:
                         print("The meaning of life is blah blah blah ...")
                    elif c == file2:
                         print("Computer Science class notes ... simplified")
                         print("Do all work")
                         print("Pass course")
                         print("Be happy")
                         print("Welcome to UCT BBS")
                         print("MENU")
                         print("(E)nter a message")
                         print("(V)iew message")
                         print("(L)ist files")
                         print("(D)isplay file")
                         print("e(X)it")
                         a = input("Enter your selection:\n")
                         if a == "D" or a == "d":
                              c = input("Enter the filename:\n")
                              if c == file1:
                                   print("The meaning of life is blah blah blah ...")
                                   print("Welcome to UCT BBS")
                                   print("MENU")
                                   print("(E)nter a message")
                                   print("(V)iew message")
                                   print("(L)ist files")
                                   print("(D)isplay file")
                                   print("e(X)it")
                                   a = input("Enter your selection:\n")
                                   if a == "X" or a == "x":
                                        print("Goodbye!")
                              
                              
          
      
       
if a == "D" or a == "d":
     c = input("Enter the filename:\n")
     if c == file1:
               print("The meaning of life is blah blah blah ...")
     elif c == file2:
               print("Computer Science class notes ... simplified")
               print("Do all work")
               print("Pass course")
               print("Be happy")
     else:
          print("File not found")