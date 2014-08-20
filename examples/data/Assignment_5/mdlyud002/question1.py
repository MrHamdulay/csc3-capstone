# Yudhi Moodley
# Assignmnt 5 Question 1
# 14 April 2014
# Write a code function for UCT BBS

# 0ne function more efficient as appose to my idea of 3 separate functions earlier (One function to rule them all)
def main(): 
    i = 0 
    message = "no message yet" 
    files = ['42.txt','1015.txt']  
    while i == 0:
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")            
        sel = input("Enter your selection:\n").upper()
        if sel == 'L':
            print("List of files: " + files[0] + ", " + files[1])
            i=i=0
        elif sel == 'E':
            message = input("Enter the message:\n")
            i=i=0
        elif sel == 'V':
            print("The message is:",message)
            i=i=0
        elif sel == 'X':
            print("Goodbye!") # sentinel (felt like an x-man when i deployed it ;) )
            i=i+1
        elif sel == 'D':
            file = input("Enter the filename:\n")
            if file == '42.txt':
                print("The meaning of life is blah blah blah ...")
                i=i=0
            elif file == '1015.txt':
                print("Computer Science class notes ... simplified"+"\n"+"Do all work"+"\n"+"Pass course"+"\n"+"Be happy")
                i=i=0
            else:
                print("File not found")
                i=i+0
                                    
if __name__ == '__main__': # beginning to understand why this is so useful
    main()