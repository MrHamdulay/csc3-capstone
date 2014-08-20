""" 
Mazwi Myeza    Assignment5
14 April 2014   
Question1     """
# Creating Menu
menu = "Welcome to UCT BBS\n"
menu += "MENU\n"
menu += "(E)nter a message\n"
menu += "(V)iew message\n"
menu += "(L)ist files\n"
menu += "(D)isplay file\n"
menu +="e(X)it"
#Creating and assigning variables
message = ""
files = ["42.txt","1015.txt"]
m1 = "The meaning of life is blah blah blah ..."
m2 = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
#printing menu and asking for selection

selection = ""
# processing 
while selection != "x":
    print(menu)
    selection = input("Enter your selection:\n")
    selection = selection.lower()
    if selection == "x":
        print("Goodbye!")
    elif selection == "e":
        message = input("Enter the message:\n")
        
    elif selection == "v":
        if message =='':
            print('The message is: no message yet')
        else:
            print("The message is:",message)
    elif selection == "l":
        print("List of files: 42.txt, 1015.txt")
    elif selection == "d":
        filename = input("Enter the filename:\n")
        if filename in files:
            if filename == files[0]:
                print(m1)
            else:
                print(m2)
        else:
            print("File not found")
    