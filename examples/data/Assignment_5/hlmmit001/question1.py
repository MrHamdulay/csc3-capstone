"""Question 1, Assignment 5
UCT BBS
Mitchell Holmes
13 April 2014"""

selection=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
message=0
#keep repeating options while input is valid
while selection=="E" or selection=="e" or selection=="V" or selection=="v" or selection=="L" or selection=="l" or selection=="D" or selection=="d":    
   
   if selection=="E" or selection=="e":
      message=input("Enter the message:\n")
   if selection=="V" or selection=="v":
      if message:
         print("The message is:",message)
      else:
         print("The message is: no message yet")
   if selection=="L" or selection=="l":
      print("List of files: 42.txt, 1015.txt")
   if selection=="D" or selection=="d":
      file_name=input("Enter the filename:\n")
      if file_name=="42.txt":
         print("The meaning of life is blah blah blah ...")
      if file_name=="1015.txt":
         print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
      if file_name=="1016.txt":
         print("File not found")
  
   selection=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
# if input not e, v, l or d
print("Goodbye!")
      
             