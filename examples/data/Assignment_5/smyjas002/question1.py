#I origionally thought this question asked for acctual *.txt files to be used within the folder, thus the commenting out of certain parts of this code

import os

message = """Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:
"""
impMessage = "no message yet"
choice = "bla bla"


def giveChoice():
   choice = input (message)
   action = choice[:1].upper()
   return action

def choiceAction(action):
   if action == 'a':
      boxes.print_square ()
   elif action == 'E':
      enterMessage()
      
      #print ("Repeat to make sure:", impMessage)
   elif action == 'V':
      print ("The message is:", impMessage)
   elif action == 'L':
      listFiles() 
      #print("List of files: 42.txt, 1015.txt") # as my implementation of this prints "1015.txt, 42.txt" GAH!! this is just much easier than changing things...
   elif action == 'D':
      name = input("Enter the filename:\n")
      openFile(name)
   elif action == 'X':
      print("Goodbye!")

def enterMessage():
   global impMessage
   impMessage  = input ("Enter the message:\n")
   #print(impMessage)

def listFiles():
   files = [f for f in os.listdir('.') if os.path.isfile(f)]
   fileList = ""
   for f in files:
      if f.endswith(".txt"):
         fileList = f + fileList
         fileList = ", " + fileList
   fileList = "List of files: " + fileList[2:]
   print(fileList)



def openFile(name):
   files = os.listdir('.')  
   if os.path.isfile(name):
      with open (name, "r") as myfile:
          data=myfile.read()
      print(data)
   else:
      print("File not found")
   
while (choice != "X"):
   choice = giveChoice()
   choiceAction(choice)
   
   
   
   

'''
Welcome to UCT BBS
MENU
##(E)nter a message##
##(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:
E
Enter the message:
test message
Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:
V
The message is: test message
Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:
X
Goodbye!

Sample I/O:

Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:
l
List of files: 42.txt, 1015.txt
Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:
d
Enter the filename:
42.txt
The meaning of life is blah blah blah ...
Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:
d
Enter the filename:
1015.txt
Computer Science class notes ... simplified
Do all work
Pass course
Be happy
Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:
d
Enter the filename:
1016.txt
File not found
Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:
x
Goodbye!
'''
