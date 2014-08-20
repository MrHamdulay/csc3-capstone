#Khyati Jinerdeb
#JNRKHY001
#ASSIGNMENT 5
#Date 17/04/2014

x=" "
message="no message yet "

   #using a while loop till a certain condition applies or not
while x!="X" or x!="x":
      print("Welcome to UCT BBS")
      print("MENU")
      print("(E)nter a message")
      print("(V)iew message")
      print("(L)ist files")
      print("(D)isplay file")
      print("e(X)it")
      
      
      selection=input("Enter your selection:\n")
     
      
      if selection=="E"or selection=="e":
            message=input("Enter the message:\n")
         
      elif selection=="V" or selection=="v":
                  print("The message is:",message)
      
      elif selection=="l"or selection=="L":
            print("List of files: 42.txt, 1015.txt")
     
         
      elif selection =="d" or selection == "D":
            file=input("Enter the filename:\n")
            if a=="42.txt":
                  print("The meaning of life is blah blah blah...")
            
            elif a=="1015.txt":
                  print("Computer science class notes...simplified")
                  print("Do all work")
                  print("Pass course")
                  print("Be happy")
               
            else:
                  print("File not found")
         
      else:
            print("Goodbye!") 
            break                  


            
      
      
      
      
      
      