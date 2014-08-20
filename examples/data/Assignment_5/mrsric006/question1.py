""" UCT BBS Menu
Richard Marais
14/04/14"""

Stored = ["no message yet"]       #creating and storing in lists outside the function
List = [["42.txt","The meaning of life is blah blah blah ... "],["1015.txt","Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"]]
def Messagestore():    #main program
    i = print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  #prints menu
    select = input("Enter your selection:\n")                   #input for menu
    if select in "Xx":                             #sequence of if statements to give the appropriate output
        print("Goodbye!")
    if select in "Ee":                            #enter message
        Enter = input("Enter the message:\n")
        Stored[0] = Enter
        Messagestore()
    if select in "Vv":                               #returns text message
            print("The message is:",Stored[0])
            Messagestore()
    if select in "Ll":                              #prints the names of the stored files
        print("List of files: ",List[0][0],", ",List[1][0],sep='')
        Messagestore()
    if select in "dD":                            #prints the contents of a selected file
        j = input("Enter the filename:\n")
        if j == List[0][0]:
            print(List[0][1])
        elif j == List[1][0]:
            print(List[1][1])
        else:
            print("File not found")
        Messagestore()
        
        
        
        
        
    
    
    
    
    
    
    
    
Messagestore()