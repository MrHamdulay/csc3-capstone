#Chantel Foot 
#Assignment 5, question 1 
def menu(): 
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file") 
    print("e(X)it")
    
menu()
response= input("Enter your selection:\n") 
answer ="no message yet" #if user types V before typed in a message. see line 28

while response== "e" or response =="E" or response=="V" or response =="v" or response =="L" or response =="l" or response =="D" or response =="d":
    answer = "no message yet"
    if response == "E" or response =="e": #must account for capital and lower case
        answer = input("Enter the message:\n") 
        menu()
        response= input("Enter your selection:\n") 
        
    if response== "V"or response=="v": 
        print("The message is:", answer)
        
    if response == "L" or response =="l":
        print("List of files: 42.txt, 1015.txt")
        
    if response == "D" or response== "d":
        file = input("Enter the filename:\n")
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
                
        else: #if any file other than 2 in the list given then print...
            print("File not found")   
    menu()
    response= input("Enter your selection:\n") 
    
if response == "X" or response== "x": 
    print("Goodbye!") #not within while loop. ending menu
