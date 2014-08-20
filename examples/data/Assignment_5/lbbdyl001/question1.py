"""Make a bbs
Dylan Lubbe
 15 April 2014"""

def bbs():
    x = ""
    message = "no message yet"
    while x != 'X' and x != 'x':
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        x = input("Enter your selection:"'\n')
        if x == 'E' or x == 'e':
            message = input("Enter the message:"'\n')
        elif x == 'V' or x == 'v':
            print("The message is:", message)
        elif x == 'L' or x == 'l':
            print( "List of files: 42.txt, 1015.txt")
        elif x == 'D' or x == 'd':
            file = input( "Enter the filename:"'\n' )
            if file == '42.txt':
                print ( "The meaning of life is blah blah blah ..." )
            elif file == '1015.txt':
                print ( "Computer Science class notes ... simplified"'\n'
                        "Do all work"'\n'"Pass course"'\n'"Be happy" )
            else:
                print ( "File not found" )
    print( "Goodbye!" )

if __name__=="__main__":
    bbs()
    
                    
            

        

    
    
    