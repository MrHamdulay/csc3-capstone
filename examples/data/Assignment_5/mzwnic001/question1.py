#Nicholas Mazower, MZWNIC001
#18/04/2014
#UCT BBS simulator

#menu string
menu="Welcome to UCT BBS\n" + "MENU\n" + "(E)nter a message\n" + "(V)iew message\n" + "(L)ist files\n" + "(D)isplay file\n" + "e(X)it\n" + "Enter your selection:\n"

#Dummy messsage
message="no message yet"
#File list
files=['42.txt', '1015.txt']
#Sel is short for selection
def method():
    sel = input(menu)
    if sel=="E" or sel=="e":
        global message        
        message = input("Enter the message:\n")
    elif sel=="V" or sel=="v":
        print("The message is:", message, sep=" ")
    elif sel=="L" or sel=="l":
        print("List of files: ",files[0],", ",files[1], sep="")
    elif sel=="D" or sel=="d":
        filename=input("Enter the filename:\n")
        if filename=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    elif sel=="X" or sel=="x":
        print ("Goodbye!")
        return message
    method()
method()
