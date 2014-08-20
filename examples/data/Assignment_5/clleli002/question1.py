"""Program to simulate a simple BBS
Elizabeth Cilliers
14/04/2014"""

#Function that prints out intro and menu.  
def displayMenu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")    

def main():
    mes=""
    while True: 
        #While true display menu and ask user to ender selection.
        displayMenu() 
        sel=input("Enter your selection:\n")
        sel=sel.upper() #convert selecction to uppercase letter.
        
        #if selection is e then ask user to enter message. then start loop all over again.
        if sel=="E":
            mes=input("Enter the message:\n")
            continue
        #if selection is v then display message.   
        if sel=="V":
            if bool(mes)==True: #if the message is true then print message and continue by starting loop all over again.
                print("The message is:",mes)
                continue 
            else: #if the message is still "" then it is false. Then print no message yet.
                print("The message is: no message yet")
        #if selection is l then print the list of files.    
        if sel=="L":
            print("List of files: 42.txt, 1015.txt")
            continue    
        #if selection is D then print out the file selected/inout by the user. else print file not found.    
        if sel=="D":
            fileName=input("Enter the filename:\n")
            if fileName=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
                continue
            
            elif fileName=="42.txt":
                print("The meaning of life is blah blah blah ...")
            else:
                print("File not found")
                continue
        #if selection is x then print goodbye and break/terminate out of loop.    
        if sel=="X":
            print("Goodbye!")
            break    
main()


