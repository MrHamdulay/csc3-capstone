#a program that simulate a BBS
#Jenny Luo
#15 april 2014

a=""
message="no message yet"
file=""

#determine the selection of options from the user and bahave accordingly
while a!="X" or a!="x":
   print("Welcome to UCT BBS")
   print("MENU")
   print("(E)nter a message")
   print("(V)iew message")
   print("(L)ist files")   
   print("(D)isplay file")
   print("e(X)it")
   selection=input("Enter your selection:\n")  # get the input from the user
   if selection=="E"or selection=="e":
      message=input("Enter the message:\n")
   elif selection=="V" or selection=="v":  # view the stored message 
      print("The message is:", message)
   elif selection=="l" or selection=="L": 
      print("List of files: 42.txt, 1015.txt")
   elif selection=="D" or selection=="d":  
      file=input("Enter the filename:\n") #get the input from the user
      if file=="42.txt":
         print("The meaning of life is blah blah blah ...")
      elif file=="1015.txt":
         print("Computer Science class notes ... simplified")
         print("Do all work")
         print("Pass course")
         print("Be happy")
      else:
         print("File not found")
   else:
      print("Goodbye!") 
      break   # break out the entire function when user enters "x" or "X"
