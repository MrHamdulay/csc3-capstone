"""Program to simulate Bulletin Board System
Author: Pankaj Munbodh
16 April 2014"""

#Create an indefinitely repeating loop except when 'x' or 'X' is entered.
message_stored="no message yet"
x=1
while x==True:
          print("Welcome to UCT BBS")
          print("MENU")
          print("(E)nter a message")
          print("(V)iew message")
          print("(L)ist files")
          print("(D)isplay file")
          print("e(X)it")
          selection = input("Enter your selection:\n")
          
          #if-else statements that represent different courses of action
          if selection=='x' or selection =='X':
               print("Goodbye!")
               x=0 #to stop loop from re-executing once x is entered
               continue
          elif selection == "E" or selection == "e":
                message_stored=input("Enter the message:\n")
          elif selection == 'v' or selection == 'V':
              print("The message is:",message_stored)
          elif selection =='l' or selection == 'L':
              print("List of files: 42.txt, 1015.txt")
          elif selection == 'd' or selection == 'D':
              get_file = input("Enter the filename:\n")
              if get_file=='42.txt':
                  print('The meaning of life is blah blah blah ...')
              elif get_file == '1015.txt':
                  print("""Computer Science class notes ... simplified
Do all work
Pass course
Be happy""")
              else:
                  print("File not found")




              


