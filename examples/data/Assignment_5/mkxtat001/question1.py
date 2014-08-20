#Tato Moaki MKXTAT001
#Program to simulate a simple Bulletin Board System
#Assignment5 question1

def menu():
    
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection = input("Enter your selection:\n")
    selection = selection.lower()
    return selection

def csc1015():
    print("Computer Science class notes ... simplified")
    print("Do all work")
    print("Pass course")
    print("Be happy")
    
def textFile():
    print("The meaning of life is blah blah blah ...")
    
emptyStr = ""
def message(m):
    global emptyStr #declare as global to be used through out the program 
    emptyStr += m
    return emptyStr
   
def main():
    flag = True
    while flag:
        selection = menu()
        if(selection == "e"):
            msg = input("Enter the message:\n")
            message(msg)
            
        elif(selection == "v"):
            if(emptyStr == ""):
                print("The message is: no message yet")
            else:
                print("The message is:",emptyStr)
                
        elif(selection == "l"):
            print("List of files: 42.txt, 1015.txt")
        
        elif(selection == "d"):
            fileName = input("Enter the filename:\n")
            if(fileName == "1015.txt"):
                csc1015()
            elif(fileName == "42.txt"):
                textFile()
            else:
                print("File not found")          
        
        elif(selection == "x"):
            print("Goodbye!")
            flag = False #exit out of the loop
            
if __name__=="__main__":
    main()