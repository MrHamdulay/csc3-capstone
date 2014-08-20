#Program for UCT BBS
#Author: Litha Maqungo
#Date: 16 April 2014


    
def menu(): #setting what the standard menu is for the program 
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
menu()
selection=input("Enter your selection: \n")
answer= print("no message yet")
files= ['42.txt', '1015.txt']
messagevalue = 'false'

commands= ['d', 'D', 'e', 'E', 'v', 'V']
for i in range (len(commands)):
        if selection == "L" or selection =="l": #ifs go through the different answers and their scenarios
                print(files)
                menu()
        elif selection == "D" or selection =="d":
                filename = input("Enter the filename: \n")
                if filename == "42.txt":
                        print("The meaning of life is blah blah blah...")
                        menu()
                        if filename == "1015.txt":
                                print("Computer Science notes ... simplifed \n Do all work \n Pass course \n Be happy")
                                menu()
                        else: 
                                print("File not found")
                                menu()
        elif selection == "E" or selection =="e":
                        print("Enter the message:")
                        message=input()
                        messagevalue = 'true'
                        menu()
        elif selection == "V" or selection =="v":
                if messagevalue == 'true':
                        print(message)
                        menu()
                else:
                        print("no message yet") 
                        menu()
if selection == "X" or selection =="x":
                print ("Goodbye!") #outside the loop which allows it to kill the progrm


        
        
    