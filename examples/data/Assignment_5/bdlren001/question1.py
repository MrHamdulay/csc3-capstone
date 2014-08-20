# BBS program to exchange information in a community of users 
# Budeli Rendani
# BDLREN001
# 16/04/2104


y="no message yet" # Setting initial variable of x to default message

def main():# defining function main
    global y #Bringing the variable inside the funtion
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    x=input("Enter your selection:\n") # User must enter a selection 
    
    if x=="E" or x=="e":
        y=input("Enter the message:\n") # User must enter a message
        
    elif x=="V" or x=="v": 
            print("The message is: "+y)
        
   
    elif x=="L" or x=="l":
        print("List of files: 42.txt, 1015.txt")
    
    elif x=="D" or x=="d":
            z=input("Enter the filename:\n") # User must enter a file name
            if z=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif z=="1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy") 
            else:
                print("File not found")
    if x=="x" or x=="X":
            print("Goodbye!")
            return # break out the funtion
    main()
    
main()
    