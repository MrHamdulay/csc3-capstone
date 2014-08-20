"""Assignment 5 question 1: Bulletin Board System
Ross van der Heyde VHYROS001
12 April 2014"""

def menu ():
      """Displays menu"""
      print("Welcome to UCT BBS")
      print("MENU")
      print("(E)nter a message")
      print("(V)iew message")
      print("(L)ist files")
      print("(D)isplay file")
      print("e(X)it")
      sel = input("Enter your selection:\n")
      
      return sel
      
def enterMessage ():
      """Asks user for a message"""
      a = input("Enter the message:\n")
      return a      
      
def view(a):
      """Prints the message"""
      print("The message is:",a)
      
def listFiles ():
      """Lists all files"""
      print("List of files: 42.txt, 1015.txt", )

def display():
      """Displays file specified by the user"""
      name = input("Enter the filename:\n")
      if name=="42.txt":
            print(f42)
      elif name == "1015.txt":
            print(f1015)
      else:
            print("File not found")

# Main method
if __name__ == "__main__":
      sel = ""
      message = "no message yet"
      f42 = "The meaning of life is blah blah blah ..."
      f1015 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
      
      sel = menu().lower()
      while sel != 'x':
            if sel == 'e':
                  message = enterMessage()
            elif sel == 'v':
                  view(message)
            elif sel == 'l':
                  listFiles()
            elif sel == 'd':
                  display()
            else :
                  print ("invalid choice")
            sel = menu().lower()
      print("Goodbye!")
# End main