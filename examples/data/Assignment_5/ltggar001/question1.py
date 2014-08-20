"""Bulletin Board System program that the public can interact with
Gareth Lategan
15-04-2014"""


#fresh variable
message=['no message yet']
list1 = ['42.txt', '1015.txt']
#function that processes users command
def prompt():
    
    #give the options and get input
    choice = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    
    #convert input into a capital letter for consistency
    command = choice.upper()

    if command == 'E':
        a=input("Enter the message:\n")
        message[0]=a
        prompt() #recalls the function so that the user can input more

    elif command == 'V':
        if len(message)==0: #a '0' means there's nothing in the array yet
            print("no message yet")
            prompt()
        else:
            print("The message is:",message[0]) #this only prints the 1st message, not sure if that's right
            prompt()

    elif command == 'L':
        print("List of files:",', '.join(list1))
        prompt()

    elif command == 'D':
        file = input("Enter the filename:\n")
        if file == "42.txt":
            file_42 = open("42.txt",'r') #calls the text file
            print(file_42.read()) #prints what's in the text file
            file_42.close #makes sure the file doesn't stay open in the background unnecessarily
            prompt()
        elif file == "1015.txt":
            file_1015 = open("1015.txt",'r')
            print(file_1015.read())
            file_1015.close
            prompt()
        else:
            print("File not found") #anything inexact will not be found
            prompt()

    elif command == 'X':
        print("Goodbye!") #no longer calls the function

#call the function
prompt()