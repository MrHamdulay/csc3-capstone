#Program simulating a simple BBS 
#by Alexander Brunette
#15/04/201

def main():
        new_message=''
        while True:
                print("Welcome to UCT BBS")
                print("MENU")
                print("(E)nter a message")
                print("(V)iew message")
                print("(L)ist files")
                print("(D)isplay file")
                print("e(X)it")
                selection=input("Enter your selection:\n")
                if selection.upper()=="L":
                        print("List of files: 42.txt, 1015.txt")
                elif selection.upper()=="D":
                        fil_na=input("Enter the filename:\n")
                        if fil_na=="1015.txt":
                                print("Computer Science class notes ... simplified")
                                print("Do all work")
                                print("Pass course")
                                print("Be happy")
                        elif fil_na=="42.txt":
                                print("The meaning of life is blah blah blah ...")
                        else:
                                print("File not found")                
                elif selection.upper()=="E":
                        old_message=input("Enter the message:\n")
                        old_message+=new_message
                elif selection.upper()=="V":
                        if new_message=="":
                                print("The message is: no message yet")
                        else:
                                print("The message is:",new_message)
                                
                        
                      
                elif selection.upper()=="X":
                        print("Goodbye!")
                        break
              
              

main()                
                
            
            
            
            
    