#Question1
#Assignment 5
#NGMTAS001

choice = 'a'
while choice[0] != 'X':
    
     print("Welcome to UCT BBS \nMENU \n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:")
     choice  = input().upper()
     global message
     
     
     

     if choice[0] == 'E':
          message = input("Enter the message:\n")
            
          
     
     elif (choice[0] == 'V'):
          
          try:
               print("The message is:",message)
          except NameError:
               print("The message is: no message yet")
     
     elif choice[0] == 'X':
          print("Goodbye!")
          break     
     elif choice[0] == 'L':
          
          print("List of files:", end ="")
          import os
          tmp = ""
          #search the directory for a file ending with txt
          for file in os.listdir():
               if file.endswith(".txt"):
                    tmp = tmp +file+", "        
          
          part = tmp[:len(tmp)-2].split(",")
          
          print (part[1],", ", part[0], sep="")
          
          
        
          
     
     elif choice[0] =='D':
          filename = input("Enter the filename:\n")
          
          #catching the file not found case
          try:
               file = open(filename)
               print (file.read())
               file.close()
          except:
               print("File not found")       
    