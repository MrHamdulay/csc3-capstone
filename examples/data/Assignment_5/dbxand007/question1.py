#Cherise Dube
#12 April 2014
"""Program to simulate simple Bulletin Board System"""


def BBS():
    message=""  
    while True:
        print ("Welcome to UCT BBS\nMENU")
        print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        answer=input("Enter your selection:\n")
        answer=answer.capitalize()
        if answer=='E':
            message=input("Enter the message:\n")
        
        
        elif answer=='V':
            if message=="":
                print("The message is: no message yet")
            else:
                print("The message is:",message)
            
        elif answer=='L':
            print("List of files: 42.txt, 1015.txt")
            
        elif answer=='D':
            filename=input("Enter the filename:\n")
            
            if filename=='42.txt':
                print("The meaning of life is blah blah blah ...")
            
            elif filename=='1015.txt':
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            
            else: 
                print("File not found")
        
        elif answer=='X':
            print("Goodbye!")
            break

BBS()        
            
        
        
        
        