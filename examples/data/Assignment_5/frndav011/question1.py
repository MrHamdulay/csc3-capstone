"""David Fransch
Assignment 5- Q1
14-04-2014"""
#Interface and input
print("Welcome to UCT BBS\nMENU")
select = str(input("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n"))
lists = ['42.txt','1015.txt']
msg = ""
#For exit function
while select.upper()!="X":
   
   #Determines which statement to execute from user input
   if select.upper() =='E':
      msg= input("Enter the message:\n")
   elif select.upper() =='V':
      if msg == "":
         print("The message is: no message yet")
      else:
         print("The message is:", msg)
              
   elif select.upper() == 'L':
      print("List of files:", lists[0]+",", lists[1])
   elif select.upper() == 'D':
      filename = input("Enter the filename:\n")
      if filename in lists:
         if filename == lists[0]:
            print("The meaning of life is blah blah blah ...")
         elif filename == lists[1]:
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
      else:
         print("File not found")
   print("Welcome to UCT BBS\nMENU")   
   select = str(input("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n"))

#End of while returns when x/X is selected
print("Goodbye!")
   
   
    