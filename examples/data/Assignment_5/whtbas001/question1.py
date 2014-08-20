#THOMAS WHITEHEAD
#WHTBAS001
#15-04-2014
#CSC1015F
#ASSIGNMENT 5
#QUESTION 1


def bss_main(): #function to contain selection loop
    selection = 'a' #defining selection to be anything but exit criteria of while loop
    stored_message = "no message yet"   
    while selection != 'x': #indefinite loop to cycle through board till x inputted
        print("Welcome to UCT BBS") #Titles...
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")        
        selection = input("Enter your selection:\n") #selection prompt.
        if selection == 'x': #exits loop
            print("Goodbye!") #says goodbye
        if selection == 'e': 
            stored_message = input("Enter the message:\n") #storing message
        if selection == 'v':
            print("The message is:",stored_message) #displays stored message
        if selection == 'l': 
            print("List of files: 42.txt, 1015.txt") #literally prints 'file' list
        if selection == 'd':
            choose_file = input("Enter the filename:\n") #chooses a file
            if choose_file == str('1015.txt'):
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy") #prints 'notes'
            elif choose_file == str('42.txt'):
                    print("The meaning of life is blah blah blah ...") #prints Hitchhikers reference
            else:
                print("File not found") #rejects any other input
                        

bss_main() #invokes function
            
        