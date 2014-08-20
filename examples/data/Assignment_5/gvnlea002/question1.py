"""BBS with one stored message and 2 fixed files
Leandra Govender
13 April 2014"""
     
selection= ""
message=""
e="e" or"E"   #define selections
v="v" or "V"
l="l" or "L"
d= "d" or "D"
x= "x" or "X"

while selection != x:               #continue displaying menue until user selects x
 #display menue
 print("Welcome to UCT BBS")
 print("MENU")
 print("(E)nter a message")
 print("(V)iew message")
 print("(L)ist files")
 print("(D)isplay file")
 print ("e(X)it")
 selection= input("Enter your selection:""\n") #ask user for selection
 e="e" or"E"
 v="v" or "V"
 l="l" or "L"
 d= "d" or "D"
 x= "x" or "X"        
 text1="The meaning of life is blah blah blah ..."           
 text2= "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
 
 if selection == e:
  message=input("Enter the message:""\n")
 else:    
  if selection == v:
   if message!="":
    print("The message is:",message)
   elif message=="":
    print("The message is: no message yet")
  else:
   if selection== l:
    print("List of files: 42.txt, 1015.txt")
   else:
    if selection== d:
     file=input("Enter the filename:\n")
     if file=="42.txt":
      print(text1)
     elif file=="1015.txt":
      print(text2)
     else:
      print("File not found")
    else:
     if selection== x:
      print("Goodbye!")      
    