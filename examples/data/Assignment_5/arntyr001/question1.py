#BBS simulator
#ARNTYR001
#15 April 2014

def bbs_sim():
    new_msg = "no message yet"
    choice=0
    
    while choice != "X" and choice != "x":
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print('(D)isplay file')
        print("e(X)it")
        
        choice = input("Enter your selection:\n") #finds choice
                    
        
        if choice == "E" or choice == "e":
            new_msg = input("Enter the message:\n") #gives new message
            
            
                        
        elif choice == "V" or choice == "v":
            print("The message is:", new_msg)
            
        
        elif choice == "L" or choice == "l":
            print("List of files: 42.txt, 1015.txt")
            
        elif choice == "D" or choice == "d":
            text_file = input("Enter the filename:\n")
            
            if text_file == "42.txt":
                print("The meaning of life is blah blah blah ...")
                
            elif text_file == "1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                
            else:
                print("File not found")
        elif choice == "X" or choice == "x":
            print("Goodbye!")
            x=2
            
        
bbs_sim()
    
    

    
    
    #new_msg = input("(E)nter a message")
    #view_msg = input("(V)iew message")
    #list_files = input("(L)ist files")
    #disp_file = input("(D)isplay file")
    #exit = input("e(X)it")
    
    