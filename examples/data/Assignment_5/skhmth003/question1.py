#Bulletin Board
#Author: Gordon Skhosana
#Date: 12/04/2014


def UCT_BBS_Default_message():
     print("Welcome to UCT BBS\n","MENU\n","(E)nter a message\n","(V)iew message\n","(L)ist files\n","(D)isplay file\n","e(X)it",sep="")
def UCT_BBS():
     UCT_BBS_Default_message()
     Selection=input("Enter your selection:\n")
     if Selection == "E" or Selection=="e":
          Message=input("Enter the message:\n")
          UCT_BBS_Default_message()
          Selection=input("Enter your selection:\n")
          if Selection == "V" or Selection=="v":
               print("The message is:",Message)
               UCT_BBS_Default_message()
               Selection=input("Enter your selection:\n")
               if Selection == "X" or Selection=="x":
                    print("Goodbye!")               
          else:
               UCT_BBS()
     elif Selection == "V" or Selection=="v":
          print("The message is: no message yet")
          UCT_BBS()
     elif Selection  == "L" or Selection=="l":
          print("List of files: 42.txt, 1015.txt")
          UCT_BBS_Default_message()
          Selection=input("Enter your selection:\n")
          if Selection == "D" or Selection =="d":
               FileName=input("Enter the filename:\n")
               if FileName == "42.txt":
                    print("The meaning of life is blah blah blah ...")
               elif FileName == "1015.txt":
                    print("Computer Science class notes ... simplified\n","Do all work\n","Pass course\n","Be happy",sep="")
               else:
                    print("File not found")               
               UCT_BBS()
          else:
               UCT_BBS()          
     elif Selection == "D" or Selection=="d":
          FileName=input("Enter the filename:\n")
          if FileName == "42.txt":
               print("The meaning of life is blah blah blah ...")
          elif FileName == "1015.txt":
               print("Computer Science class notes ... simplified\n","Do all work\n","Pass course\n","Be happy",sep="")
          else:
               print("File not found")
          UCT_BBS()
     elif Selection == "X" or Selection=="x": 
          print("Goodbye!")
     else:
          UCT_BBS() 
UCT_BBS()