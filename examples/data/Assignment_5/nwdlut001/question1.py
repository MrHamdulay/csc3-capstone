def menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    
    print("(D)isplay file")
    print("e(X)it")
def selection():
    v=''
    
    while(True):
        menu()
        choice=input("Enter your selection:\n")
        if choice=="E"or choice=="e":
            v+=input("Enter the message:\n")
           
        elif choice=="V" or choice=="v":
            if v!='':
                print("The message is:",v)
            else:
                print("The message is: no message yet")
           
        elif choice=="X" or choice=="x":
            print("Goodbye!")
            break
         
        elif choice=="l":
            print("List of files: 42.txt, 1015.txt")
        elif choice=="d":
            file_name=input("Enter the filename:\n")
            if file_name=="1015.txt":
              print("Computer Science class notes ... simplified")
              print("Do all work")
              print("Pass course")
              print("Be happy")
            elif file_name=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file_name!="42.txt" and file_name!="1015.txt":
                print("File not found")
            elif choice!="l" and choice!="E"  and choice!="V" and choice!="d" and choice!="X" and choice!="e" and choice!="v" and choice=="d" and choice=="D":
                print("No message yet")
            
        
        
    
selection()
        
      
       

    