file1 = open("42.txt","r")
file2 = open("1015.txt", "r")
carryon = "eEvVlLdD"
finish = "xX"
def getmessage():
   m = input("Enter the message:\n")
   return m
choice = input("Welcome to UCT BBS \nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
message = "no message yet"
if choice == "x" or choice=="X":
   print("Goodbye!")
while choice in carryon:
   if choice == "E" or choice == "e":
      message = getmessage()
      choice = input("Welcome to UCT BBS \nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
      if choice in finish:
         print("Goodbye!")
   elif choice =="V" or choice =="v":
      print("The message is: " + message)
      choice = input("Welcome to UCT BBS \nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
      if choice in finish:
         print("Goodbye!")   
   elif choice =="L" or choice =="l":
      print("List of files: 42.txt, 1015.txt")
      choice = input("Welcome to UCT BBS \nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
      if choice in finish:
         print("Goodbye!") 
   elif choice == "D" or choice =="d":
      name = input("Enter the filename: \n")
      if name == "42.txt":
         print(file1.read())
      elif name == "1015.txt":
         print(file2.read())
      elif name != "42.txt" or name != "1015.txt":
         print("File not found")
      choice = input("Welcome to UCT BBS \nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
      if choice in finish:
         print("Goodbye!")       
      
      


     
   
  