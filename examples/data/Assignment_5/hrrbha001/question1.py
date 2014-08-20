# bbs simulator
# hs
# 23 march 2011

choice = ""
message = "no message yet"

while choice != "X":
   print ("Welcome to UCT BBS")
   print ("MENU")
   print ("(E)nter a message")
   print ("(V)iew message")
   print ("(L)ist files")
   print ("(D)isplay file")
   print ("e(X)it")
   print ("Enter your selection:")
   
   choice = input ("").upper ()
   if choice == "E":
      message = input ("Enter the message:\n")
   elif choice == "V":
      print ("The message is:", message)
   elif choice == "L":
      print ("List of files: 42.txt, 1015.txt")
   elif choice == "D":
      filename = input ("Enter the filename:\n")
      if filename == "42.txt":
         print ("The meaning of life is blah blah blah ...")
      elif filename == "1015.txt":
         print ("Computer Science class notes ... simplified")
         print ("Do all work")
         print ("Pass course")
         print ("Be happy")
      else:
         print ("File not found")

print ("Goodbye!") 
   