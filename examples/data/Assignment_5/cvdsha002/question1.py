#Shahrain Coovadia
#CVDSHA002



selection='start' 
message='no message yet'

while selection != "X" or selection!="x":                        

     print("Welcome to UCT BBS")                               #display posible input options
     print("MENU")
     print("(E)nter a message")
     print("(V)iew message")
     print("(L)ist files")
     print("(D)isplay file")
     print("e(X)it")
     
     selection=input("Enter your selection:\n")
     
     if selection=="E" or selection=="e":                     #choose selection
          message=input("Enter the message:\n")                
        
    
     if selection=="V" or selection=="v":                 #view     
          print ("The message is:", message)
    
     if selection=="L" or selection=="l":                   #show list of files
          print("List of files: 42.txt, 1015.txt")
    
     if selection=="D" or selection=="d":
          file=input("Enter the filename:\n")                
          
          if file=="42.txt":
               print("The meaning of life is blah blah blah ...")                              # create files
               
          elif file=="1015.txt":
               print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy", sep='')
          
          else:
               print("File not found")                 #accounting for incorrect inputs
       
        
     if selection=="X" or selection=="x":                  #end of program                           
          print("Goodbye!")
          break
     

    
    
