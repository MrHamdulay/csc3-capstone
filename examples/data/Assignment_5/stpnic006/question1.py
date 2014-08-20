"""Nicholas Stephenson
Bulletin Board Systems (BBS)
15 April"""


print("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew Message \n(L)ist files \n(D)isplay file \ne(X)it")
#Menue provided by I/O

mes = "no message yet"
#Create Variable

US = input("Enter your selection:\n")
#User Selelction

if US == "x" or US == "X":
    print("Goodbye!")
#Terminate BBS if x

while (US != "x" and US != "X") : 
    if US == "e" or US == "E": 
        mes = input ("Enter the message:\n")
        #User Enters new Message, option E
    if US == "v" or US == "V":
        print("The message is:", mes)
        #Shows Mes, option V
    if US == "L" or US == "l":
        print("List of files: 42.txt, 1015.txt")
        #List 2 given files, option L
    if US == "D" or US == "d":
        USF = input("Enter the filename:\n")
        #User Selection File, D
        if USF == "42.txt":
            print("The menaing of life is blah blah blah ...")
        elif USF =="1015.txt":
            print("Computer Science class notes ... simplified \nDo all work \nPass Course \nBe happy")
        else: print("File not found")
        #Options of 42- or 1015.txt
        

    print("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew Message \n(L)ist files \n(D)isplay file \ne(X)it")
#Menue provided by I/O

        
    US = input("Enter your selection:\n")
#User Selelction

    if US == "x" or US == "X":
            print("Goodbye!")
#Terminate BBS if x