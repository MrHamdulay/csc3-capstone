#BBS program
#Robin Hall
#16/04/2014

msg_variable = "no message yet" #default message 

def BBS(): #create a function in order to run it again after completion of a selection without a prompt 
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    # opening text 
    
    selection = input("Enter your selection:\n")
    
    if selection == 'e' or selection == 'E':
        global msg_variable #in order to change the message throughout the entire program
        msg_variable = input("Enter the message:\n")
        BBS() #runs program again
    
    elif selection == 'v' or selection == 'V':
        print("The message is:",msg_variable,sep = ' ')
        BBS()
        
    elif selection == 'l' or selection == 'L':
        print("List of files: 42.txt, 1015.txt")
        BBS()
    
    elif selection == 'd' or selection == 'D':
        file_select = input("Enter the filename:\n")
        if file_select == '42.txt': #nested loop inside 'd' selection to account for 2 listed files
            print("The meaning of life is blah blah blah ...")
        elif file_select == '1015.txt':
            print("Computer Science class notes ... simplified","Do all work","Pass course","Be happy",sep = '\n')
        else:
            print("File not found") #boundary condition satisfied
        BBS()

    elif selection == 'x' or selection == 'X':
        print("Goodbye!")

BBS()