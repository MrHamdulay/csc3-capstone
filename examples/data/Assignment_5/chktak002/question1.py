#programme to for simple public bulettin board system
#takunda chikondo
#13 april 2014

def PBS():
           print("Welcome to UCT BBS") 
           print("MENU")
           print("(E)nter a message")
           print("(V)iew message")
           print("(L)ist files")
           print("(D)isplay file")
           print("e(X)it")
    
        
def cont():
           
           PBS()
           a=input("Enter your selection:\n")
           a=a.upper()
           b=""
           
           while not a=="X":
                      if a=="E": 
                                 b=input("Enter the message:\n")
                     
                      if a=="V" :
                                 if b!="":
                                            print("The message is:",b)
                                 else:
                                            print("The message is: no message yet")
                               
                      if a=="L":
                                 print("List of files: 42.txt, 1015.txt")
                            
                      if a=="D":
                                 a=input("Enter the filename:\n")
                                 if a=="42.txt":
                                            print("The meaning of life is blah blah blah ...")
                                 elif a=="1015.txt":
                                            print("Computer Science class notes ... simplified")
                                            print("Do all work")
                                            print("Pass course")
                                            print("Be happy") 
                                 else:
                                            print("File not found")                         
                                 
                     
                      PBS()
                      a=input("Enter your selection:\n")
                      a=a.upper()                                 
           else:
                      print("Goodbye!")
                                                                  
cont()

                        
    
    
    
    
