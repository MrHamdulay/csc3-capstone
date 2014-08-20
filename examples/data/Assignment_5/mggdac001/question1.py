def bbs():
     msg='no message yet'
     sel=''  
    
     while sel != "x":
          
          print('Welcome to UCT BBS')
          print('MENU')
          print('(E)nter a message')
          print('(V)iew message')
          print('(L)ist files')
          print('(D)isplay file')
          print('e(X)it')
          sel=input("Enter your selection:\n")
          
          
          if sel =="e":
               msg=input("Enter the message:\n")
                  
                        
          
          elif sel=="v":
                
                    print("The message is:",msg)
              
          elif sel=="x":
               print("Goodbye!")
               break
          elif sel=="l":
               print("List of files: 42.txt, 1015.txt")
          elif sel=="d":
               en=input("Enter the filename:\n")
               if en == "42.txt":
                    print("The meaning of life is blah blah blah ...")
               elif en=="1015.txt":
                    print("Computer Science class notes ... simplified")
                    print("Do all work")
                    print("Pass course")
                    print("Be happy")
               elif en=="1016.txt":
                    print("File not found")
                   
                    
               

          
               
               
               
            
            
       
       
  
        
        
        
bbs()    
    