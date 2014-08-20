"""UCT Bulletin Board System
Dudley Mutero
17-4-14"""

def print1():
    print ("Welcome to UCT BBS")
    print ("MENU")
    print ("(E)nter a message")
    print ("(V)iew message")
    print ("(L)ist files")
    print ("(D)isplay file")
    print ("e(X)it")    


def BSS():
    inputselection="A"
    stored_message=""
    while inputselection != "X":
        print1()
        input1=input("Enter your selection:\n")#prompts user for input
        input1=input1.upper()
        if input1 =="E": 
            stored_message+=input("Enter the message:\n")
            inputselection="E"
            #return stored_message
    
        
        elif input1=="V":
            if stored_message== "":
                print ("The message is: no message yet")
            else:
                print ("The message is:",stored_message)
            inputselection="V"
        
        elif input1=="L":#choice l
            print ("List of files: 42.txt, 1015.txt")
            inputselection="L"
        
        elif input1=="D":#choice d
            filename=input("Enter the filename:\n")
            if filename=="42.txt":
                print ("The meaning of life is blah blah blah ...")
                inputselection="D"
            
            elif filename =="1015.txt":
                print ("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                inputselection="D"
            
            else:
                print ("File not found")
        elif input1=="X":#stops the program
            break
            
    print ("Goodbye!")

BSS()
       
    
        
        
    
            
        
    
    
    