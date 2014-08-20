#Joy Arendse-Gorvalla

print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message") #print statements
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")
A = input("Enter your selection:\n") #asking for input

while A != "X" and A != "x": #creating a loop
   if A == "E" or A == "e": #if statement - creating condition
      M = input("Enter the message:\n") #asking for input
      print("Welcome to UCT BBS")
      print("MENU")
      print("(E)nter a message")
      print("(V)iew message")
      print("(L)ist files")
      print("(D)isplay file")
      print("e(X)it") 
      A = input("Enter your selection:\n") #asking user to enter a selection

   elif A == "V" or A == "v": #another condition
      try:
         print("The message is:", M)   #prints the message M
      except NameError:
         print("The message is: no message yet") 

      print("Welcome to UCT BBS")
      print("MENU")
      print("(E)nter a message")
      print("(V)iew message")
      print("(L)ist files")
      print("(D)isplay file")
      print("e(X)it") 
      A = input("Enter your selection:\n")       

   elif A == "L" or A == "l": #another condition
      print("List of files: 42.txt, 1015.txt")
      print("Welcome to UCT BBS")
      print("MENU")
      print("(E)nter a message")
      print("(V)iew message")
      print("(L)ist files")
      print("(D)isplay file")
      print("e(X)it") 
      A = input("Enter your selection:\n") 


   elif A == "D" or A == "d": #another codition
      file = input("Enter the filename:\n") 
      if file == "42.txt": 
         print("The meaning of life is blah blah blah ...")
         print("Welcome to UCT BBS")
         print("MENU")
         print("(E)nter a message")
         print("(V)iew message")
         print("(L)ist files")
         print("(D)isplay file")
         print("e(X)it") 
         A = input("Enter your selection:\n")             

      elif file == "1015.txt": #another condition
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
         A = input("Enter your selection:\n")             

      else: #another condition
         print("File not found")
         print("Welcome to UCT BBS")
         print("MENU")
         print("(E)nter a message")
         print("(V)iew message")
         print("(L)ist files")
         print("(D)isplay file")
         print("e(X)it") 
         A = input("Enter your selection:\n")         

if A == "X" or A == "x": 
   print("Goodbye!") #end of loop