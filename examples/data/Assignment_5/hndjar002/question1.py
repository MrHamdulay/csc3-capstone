""" Question 1
 Jaren Hendricks
 17 April 2014 """

# function to display welcome message
def Print():
       print ("Welcome to UCT BBS")
       print ("MENU")
       print ("(E)nter a message")
       print ("(V)iew message")
       print ("(L)ist files")
       print ("(D)isplay file")
       print ("e(X)it")
       
# Declaring variables to empty strings. 
selection = ""
filename = ""
message = "no message yet"

# loop will break if the supplied input is "X" 
# the loop will output specific according to the selection
while not selection == "X":
       Print()
       selection = input("Enter your selection:\n")
       if (selection == "E") or (selection == "e"):
              message=(input("Enter the message:\n"))
       if (selection == "V") or (selection == "v"):
              print("The message is:", message)
       if (selection == "L") or (selection == "l"):
              print("List of files: 42.txt, 1015.txt")
       if (selection == "D") or (selection == "d"):
              filename = input("Enter the filename:\n")
              if filename == "42.txt":
                     print ("The meaning of life is blah blah blah ...")
              if filename == "1015.txt":
                     print ("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
              if filename == "1016.txt":      
                     print("File not found")
       if (selection == "X") or (selection == "x"):
              print("Goodbye!") 
              break
       
