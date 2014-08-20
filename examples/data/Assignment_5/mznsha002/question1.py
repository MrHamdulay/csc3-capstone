# 13 April 2014
# Shaun Muzenda
# Simulating a public Bulletin Board System using a stored message and 2 fixed files

def main():
    
    message = ""            #default string if V selected before a message has eneterd

    while True:
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        menu_select = input("Enter your selection:\n")

        if menu_select == "E" or menu_select == "e":            #enters a message into the PBS
            message = input("Enter the message:\n")
            
        if menu_select == "X" or menu_select == "x":            #ends the program
            print("Goodbye!")
            break
        
        if menu_select == "V" or menu_select == "v":            
            if message != "":
                print("The message is:", message)               #displays the message if one has been entered
            else:
                print("The message is: no message yet")         #default message printed if none has been entered at the time
        
        if menu_select == "L" or menu_select == "l":            #displays list of files accessabile by PBS
            print("List of files: 42.txt, 1015.txt")
    
        if menu_select == "D" or menu_select == "d":
            file_name = input("Enter the filename:\n")          #displays the entire file selected
            
            if file_name == "42.txt":                           #the one file
                print("The meaning of life is blah blah blah ...")
            
            elif file_name == "1015.txt":                       #the other file   
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
                
            elif file_name != "42.txt" or file_name != "1015.tx":   #default message if incorrect file name inputed
                print("File not found")
    
main()