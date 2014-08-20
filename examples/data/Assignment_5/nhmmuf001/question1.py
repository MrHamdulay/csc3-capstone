""" program to simulate BBS
Mufudzi Nhamoinesu
2014 04 014 """
def farmyard():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
farmyard()

def selection():
    sheep = ''
    cottonwool=''
    while sheep  != "X":
        sheep = input("Enter your selection:\n")
        sheep = sheep.upper()

        if sheep == "E":
            cottonwool =input("Enter the message:\n")
            farmyard()               
        if sheep == "V":
            if cottonwool=="":
                print("The message is: no message yet")
                farmyard()
            else:
                print("The message is:", cottonwool)
                farmyard()
        if sheep == "L":
            print("List of files: 42.txt, 1015.txt")
            farmyard()
        if sheep == "D":
            lambchops = input("Enter the filename:\n")
            if lambchops == "42.txt":
                print("The meaning of life is blah blah blah ...")
                farmyard()
            elif lambchops == "1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                farmyard()
            else:
                print("File not found")
                farmyard()
    if sheep == "X":
        print("Goodbye!")
    
    
selection() 

    

#print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy\nWelcome to UCT BBS")

#print("The meaning of life is blah blah blah ...")

