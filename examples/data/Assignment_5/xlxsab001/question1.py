"""UCT BBS Program
Sabelo Xulu
15 April 2014"""

x=1
message=0
while x:
       
       print("Welcome to UCT BBS")
       print("MENU")
      
       print("(E)nter a message")
        
       print("(V)iew message")
       print("(L)ist files")
       
       print("(D)isplay file")
       print("e(X)it") 
       
       
       z=input("Enter your selection:\n")
       x=z.lower()
       
       if x=="e":
              
              message=input("Enter the message:\n")
              
       elif x=="v":
              message1=("no message yet")
              if message==0:
                     print("The message is:",message1)
              else:
                     print("The message is:", message)
              
       elif x=="l":
              print("List of files: 42.txt, 1015.txt")
        
       elif x=="d":
              y=input("Enter the filename:\n")
              
              
              if y=="42.txt":
                     print("The meaning of life is blah blah blah ...")
              elif y=="1015.txt":
                     print("Computer Science class notes ... simplified")
                     print("Do all work")
                     print("Pass course")
                     print("Be happy")
                     
              elif y!= "42.txt" or "1015.txt":
                     print("File not found")                     
       
              
       elif x=="x":
              print("Goodbye!")
              break
        
    
   
    
    
    