
#a program that simulates a simple BBS 
#Author: Sithembiso Mashinini
#12 April 2014


def main():
    menu= "MENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it"
    print("Welcome to UCT BBS")
    print(menu)
    
    # prompt the user to input a selection
    selection = input("Enter your selection: \n")
    message = ""
    # while loop that will run only if the user does input a "X"
    while selection not in "X" and selection not in "x":
        
        # if the user inputs an E, e incase the user enters a lower letter  prompt them to enter a message
        if selection == "E" or selection == "e":
            message = input("Enter the message: \n")
         
        # if the user inputs a V, print 'no message yet' if there is no message
        # and print a message if the user did type one
        elif selection == "V" or selection == "v":
            if message == "":
                
                print("The message is:", "no message yet")
            else:
                print("The message is:", message)
                
        # if the user selection is a L, print the list of files
        elif selection == "L" or selection == "l":
            print("List of files: 42.txt, 1015.txt")
         
        # if the user selection is a D, prompt the user for a file name
        # and print out the contents of the file
        elif selection == "D" or selection == "d":
            filename = input("Enter the filename: \n")
            
            file_1, file_2 = "42.txt", "1015.txt"
            
            #this is for when thefile name is not found  
            # found else print out the contents of the selected file
                
            if filename == file_1:
                print("The meaning of life is blah blah blah ...")
            elif filename == file_2:
                print("Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy")
            else:
                print("File not found")
            
        print("Welcome to UCT BBS")
        print(menu)
        # prompt the user for multiple selections
        selection = input("Enter your selection: \n")  
    
    # this exits the program  
    print("Goodbye!")
        
if __name__ == '__main__':
    main()
            