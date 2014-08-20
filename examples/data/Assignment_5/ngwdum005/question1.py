"""Dumisani Ngwenza
16/04/2014
NGWDUM005"""
#Create fixed files
List1 = ["42.txt", "The meaning of life is blah blah blah ..."]
List2 = ["1015.txt", "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"]
message = ""

#create menu
def Menu():
    print ("Welcome to UCT BBS")
    print ("MENU")
    print ("(E)nter a message")
    print ("(V)iew message")
    print ("(L)ist files")
    print ("(D)isplay file")
    print ("e(X)it")


# listing file names
def ListFiles():
    print ("List of files: ", List1[0], ", ", List2[0], sep="")
    
#displaying file names
def DisplayFiles():
    filename = input ("Enter the filename:\n")
    if List1[0] == filename:
        print (List1[1])
    elif List2[0] == filename:
        print (List2[1])
    else:
        print ("File not found")

#main program
def main():
    message = ''
    Menu()
    x = input ("Enter your selection:\n")
    selection = x.lower()
    while selection != 'x':
        if selection == 'e':
            x = input ("Enter the message:\n")
            message = x
        elif selection == 'v':
            if message != '':
                print ("The message is:", message)
            else:
                print ("The message is: no message yet")
        elif selection == 'l':
            ListFiles()
        elif selection == 'd':
            DisplayFiles()
        Menu()
        x = input ("Enter your selection:\n")
        selection = x.lower()
    
    
    else:
        print ("Goodbye!")#stops program

if __name__=='__main__':
    main()