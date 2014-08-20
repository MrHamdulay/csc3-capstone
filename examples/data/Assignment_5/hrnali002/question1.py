# A program that simulates a BBS
# Alison Hoernle
# HRNALI002
# 12 April 2014

def BSS():
   
   select = ''
   message = ''
   
   while select != 'X':

      # beginning statements
      print("Welcome to UCT BBS")
      print("MENU")
      print("(E)nter a message")
      print("(V)iew message")
      print("(L)ist files")
      print("(D)isplay file")
      print("e(X)it")
    
      #their decisions:
      select = input("Enter your selection:\n")
      select = select.upper()
    
      if select == 'E':
         message = input("Enter the message:\n")     
      
      if select == 'V':
         if message != '':
            print("The message is:", message)
         else:
            print("The message is: no message yet")
         
      elif select == 'L':
         print("List of files: 42.txt, 1015.txt")
         
      elif select == 'D':
         file = input("Enter the filename:\n")
         if file == '42.txt':
            print("The meaning of life is blah blah blah ...")
         elif file == '1015.txt':
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
         else:
            print("File not found")
    
      elif select == 'X':
         print("Goodbye!")
   
      # make select whatever option they chose for the next iteration of the while loop   
      select == select
      # if they put in a mesage, record it so that if they choose v it will display their message
      message = message
BSS()