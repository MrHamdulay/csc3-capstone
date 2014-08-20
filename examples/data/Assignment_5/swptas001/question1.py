'''A program that simulates a BBS'''
### Tashiv Sewpersad (SWPTAS001)
### Assignment 5 - Question 1
### 14 - 04 - 2014

## Constants
sMenu = "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it"

## Decalarations
def RunBBS():
  __doc__ = "A Standardized function for handeling the interface"
  print(sMenu)
  sCommand = input("Enter your selection:\n").upper()
  return sCommand

## Live Code
sCommand = RunBBS()
sMesg = "no message yet"
Files = {"42.txt":"The meaning of life is blah blah blah ...","1015.txt":"Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"}
while sCommand != "X":
  if sCommand == "E": # Exit
    sMesg = input("Enter the message:\n")
    sCommand = RunBBS()
    continue
  if sCommand == "V": # View Message
    print("The message is:",sMesg)
    sCommand = RunBBS()
    continue
  if sCommand == "L": # List Files
    sFiles = ""
    for i in Files:
     sFiles += i + ", "
    print("List of files:",sFiles[:len(sFiles)-2]) # Corrects for the ", "
    sCommand = RunBBS()
    continue
  if sCommand == "D": #Displays a file
    sFile = input("Enter the filename:\n")
    if sFile in Files:
      print(Files[sFile])
    else:
      print("File not found")
    sCommand = RunBBS()
    continue
  print("Command not found")
  sCommand = RunBBS()
print("Goodbye!")