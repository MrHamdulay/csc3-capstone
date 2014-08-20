# Question 1 - Assignment 5
# Richard van Gysen 
# define function

def uct_bbs():
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")    
    i = input("Enter your selection: \n")
    message = 'no message yet'
    
# exit 

    if i == 'X' or i =='x':
        print("Goodbye!")
        
# message prompt

    elif i!='x' or i!='X':            
        while i!='x' or i!='X':       
            if i == 'E' or i =='e':
                message = input("Enter the message: \n")
            elif i == 'V' or i =='v':
                if message=='no message yet':
                    print("The message is:",message)
                else:
                    print("The message is:",message)
            elif i == 'L' or i =='l':
                print("List of files: 42.txt, 1015.txt")
            elif i =='d' or i == 'D':    
                file = input("Enter the filename: \n")
                if file == '42.txt':
                    print("The meaning of life is blah blah blah ...")
                elif file == '1015.txt':
                    print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                else:
                    print("File not found")
            elif i == 'X' or i =='x':
                print("Goodbye!")
                break
            print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")    
            i = input("Enter your selection: \n")         
uct_bbs()