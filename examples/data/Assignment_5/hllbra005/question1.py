#Assignment 5: Question 1, Bulletin Board Systems (BBS)
#Brandon Hall (HLLBRA005)
#17/04/2014

#The values below store the defult messages that are given when a file or message is not present or the contents of a file are accesed

message = "no message yet"
display="File not found"

fourtyTwo = "The meaning of life is blah blah blah ..." 
tenFifteen = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"

def main():
    
 menu()

def menu ():
   
   global message   
   
   while(True): #This is a while loop as it repeats indefinitly until the break command is given when the user enters in "x"
    
#Below is the menu    
    
      print("Welcome to UCT BBS")
      print("MENU")
      print("(E)nter a message")
      print("(V)iew message")
      print("(L)ist files")
      print("(D)isplay file")
      print("e(X)it")
      print("Enter your selection:")
      
      a = input()
      
      if(a.upper()=="E"):
         
         print("Enter the message:")
         message = input()
             
      elif(a.upper()=="V"):
               
         print("The message is: " + message)
   
      elif(a.upper()=="L"):
                        
         print("List of files: 42.txt, 1015.txt")    
         
      elif(a.upper()=="D"):
           
         print("Enter the filename:")

         name  = input()
         
         if(name == "42.txt"):
            print(fourtyTwo)
         elif(name == "1015.txt"):
            print(tenFifteen)
         else:
            print(display)
                        
         
      elif(a.upper()=="X"):
         
         break
                    
              
   print("Goodbye!")   
   
main()





