"""Luke Joseph
JSPLUK001
2014-04-13
Question 1 of assignment 5"""
def main():
   qx= "Welcome to UCT BBS\n"
   qx+="MENU\n"
   qx+="(E)nter a message\n"
   qx+="(V)iew message\n"
   qx+="(L)ist files\n"
   qx+="(D)isplay file\n"
   qx+="e(X)it"
   a="b"
   m="no message yet"
   print(qx)
   while a=="b":
      y=input("Enter your selection:\n")
      while y!="x" or y!="X":
         if y=="E" or y=="e":
            m=input("Enter the message:\n")
            print(qx)
            break
         elif y=="v" or y=="V":
            print("The message is:",m)
            print(qx)
            break
         elif y=="l" or y=="L":
            print("List of files: 42.txt, 1015.txt")
            print(qx)
            break
         elif y=="d" or y=="D":
            f=input("Enter the filename:\n")
            if f=="42.txt":
               print("The meaning of life is blah blah blah ...")
               print(qx)
               break
            elif f=="1015.txt":
               print("Computer Science class notes ... simplified")
               print("Do all work")
               print("Pass course")
               print("Be happy")
               print(qx)
               break
            else:
               print("File not found")
               print(qx)
               break
         elif y=="X" or y=="x":
            a="c"
            print("Goodbye!")
            break
main()