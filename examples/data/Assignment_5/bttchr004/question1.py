#Program for a UCT BBS
#Chris Betteridge
#14 April 2014

print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it",sep="\n")
selection = input("Enter your selection:\n")
u_selection = selection.upper()
while u_selection == "E" or u_selection == "V" or u_selection == "L" or u_selection == "D":
   if u_selection == "E":
      message = input("Enter the message:\n")
      print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it",sep="\n")
      selection = input("Enter your selection:\n")
      u_selection = selection.upper()
      if u_selection == "V":
         print("The message is:",message)
         print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it",sep="\n")
         selection = input("Enter your selection:\n")
         u_selection = selection.upper()
   if u_selection == "V":
      print("The message is: no message yet")
      print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it",sep="\n")
      selection = input("Enter your selection:\n")
      u_selection = selection.upper()
   if u_selection == 'L':
      print("List of files: 42.txt, 1015.txt")
      print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it",sep="\n")
      selection = input("Enter your selection:\n")
      u_selection = selection.upper()
   if u_selection == "D":
      filename = input("Enter the filename:\n")
      if filename == "42.txt":
         print("The meaning of life is blah blah blah ...")
      if filename == "1015.txt":
         print("Computer Science class notes ... simplified")
         print("Do all work")
         print("Pass course")
         print("Be happy")
      if filename != "1015.txt" and filename != "42.txt":
         print("File not found")               
      print("Welcome to UCT BBS","MENU","(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it",sep="\n")
      selection = input("Enter your selection:\n")
      u_selection = selection.upper()         
         
if selection == "X" or selection == "x":
   print("Goodbye!")