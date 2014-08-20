""" assignment 5 - question 1
zaheer mahmood
4 - 15 - 2014"""
#create text files
text_file = open("42.txt","r")

text_file_2 = open("1015.txt","r")


# loop of standard message
answer = ""
get_input=""
while answer != "X":
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    answer = input("Enter your selection:\n")
    answer=answer.upper()
    

#create conditions  
    if answer == "E":
        get_input=input("Enter the message:\n")
        

    if answer == "V":
        if len(get_input) == 0: 
            print("The message is: no message yet")
        else:
            print("The message is:",get_input)

    if answer == "L":
        print("List of files: 42.txt, 1015.txt")
    
    if answer == "D":
        file_input = input("Enter the filename:\n")
        if file_input == "42.txt":
            print (text_file.read())
            text_file.close()
            #get 42.txt
        elif file_input == "1015.txt":
            print (text_file_2.read())
            text_file_2.close()        
            #get 1015.txt
        else:
            print("File not found")
    if answer == "X":
        print("Goodbye!")
    
    