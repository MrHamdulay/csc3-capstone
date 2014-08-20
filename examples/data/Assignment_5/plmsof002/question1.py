# Bulletin Board System
# Sofia Palmer
# 15 April 2014


def main ():
        output = "0"
        message = "no message yet"
        while output != 'X':            #print the menu until user wants to exit
                print("Welcome to UCT BBS")
                print("MENU")
                print("(E)nter a message")
                print("(V)iew message")
                print("(L)ist files")
                print("(D)isplay file")
                print("e(X)it")
                output = input("Enter your selection:\n").upper()
                if output == 'E':
                        message = input("Enter the message:\n")          
                elif output == 'V':
                        print("The message is:",message)
                elif output == 'L':
                        print("List of files: 42.txt, 1015.txt")
                elif output == 'D':
                        filename = input("Enter the filename:\n")
                        if filename == '42.txt':
                                print("The meaning of life is blah blah blah ...")
                        elif filename == '1015.txt':
                                print("Computer Science class notes ... simplified")
                                print("Do all work")
                                print("Pass course")
                                print("Be happy")
                        else:
                                print("File not found")
                elif output == 'X':
                        print("Goodbye!")
                        return

main()
                


        
        

    
    


