"""Muhammad Ahmad
AHMMUH009
17 April 2014"""


def UCT_BBS_MENU():
    files=['42.txt','1015.txt']             #creates a string of files
    message="no message yet"
    f=open("42.txt","w")
    f.write("The meaning of life is blah blah blah ...")
    f.close()
    f_2=open("1015.txt","w")
    f_2.write("Computer Science class notes ... simplified")
    f_2.write("\nDo all work")
    f_2.write("\nPass course")
    f_2.write("\nBe happy")
    f_2.close()
    while True:
        opt=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n").upper()
        if opt=="E":                #Selection to enter message
            message=input("Enter the message:\n")       #inputting the message
        elif opt=="V":              #selection to view the message
            print("The message is:",message)
        elif opt=="L":              #selection to list the message
            print("List of files: 42.txt, 1015.txt")
        elif opt=="D":              #selection to search the files for text
            file_name=input("Enter the filename:\n")
            if file_name not in files:
                print("File not found")
            else:
                f_new=open(file_name,"r")
                for line in f_new:
                    print(line,end="")
                print()
        elif opt=="X":                  #selection to exit
            print("Goodbye!")           #prints goodbye
            break
            
        
            
UCT_BBS_MENU()