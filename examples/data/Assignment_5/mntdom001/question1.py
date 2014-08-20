"""" question1.py
a program that simulates a simple BBS with one stored message and 2 fixed files
Author: Dominic Manthoko
12 April 2014
"""

def main():
    menu= "MENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it"
    print("Welcome to UCT BBS")
    print(menu)
    
    # prompt the user for a selection
    selec = input("Enter your selection: \n")
    message = ""
    # while loop that will run only if the user does input a "X"
    while selec not in "X" and selec not in "x":
        
        # if the user inputs an E, prompt them to enter a message
        if selec == "E" or selec == "e":
            message = input("Enter the message: \n")
         
        # if the user inputs a V, print 'no message yet' if there is no message
        # and print a message if the user did type one
        elif selec == "V" or selec == "v":
            if message == "":
                print("The message is:", "no message yet")
            else:
                print("The message is:", message)
                
        # if the user selection is a L, print the list of files
        elif selec == "L" or selec == "l":
            print("List of files: 42.txt, 1015.txt")
         
        # if the user selection is a D, prompt the user for a file name
        # and print out the contents of the file
        elif selec == "D" or selec == "d":
            filename = input("Enter the filename: \n")
            
            file1, file2 = "42.txt", "1015.txt"
            
            # if the file name is not in the list if files, print file not 
            # found else print out the contents of the selected file
                
            if filename == file1:
                print("The meaning of life is blah blah blah ...")
            elif filename == file2:
                print("Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy")
            else:
                print("File not found")
            
        print("Welcome to UCT BBS")
        print(menu)
        # prompt the user to make another selection
        selec = input("Enter your selection: \n")  
    
    # the else will execute once the user has made a "X" as a selection    
    else:
        print("Goodbye!")
        
if __name__ == '__main__':
    main()
            