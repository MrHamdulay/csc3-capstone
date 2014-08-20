"""Assignment 5 question 1
Shaheen Karodia
Krdsha003
2014-04-15"""
def display():
    """function that prints a list of options that a user can choose to do"""
    
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")    


def main():
    message=("no message yet")  #initialise message variable 
    
    prompt=""  #initilaise prompt variable
    
    
    
    while prompt !=  "x":     #ensure loop runs till user exits 
        display()             #invoke display function
        
        prompt=(input("Enter your selection:\n")).lower()  #gets input and converts it to lower case
        
        if prompt=="e":           #allows user to enter a message
            message=input("Enter the message:\n")
            
            
            
        elif prompt=="v": #allows user to view message
            print("The message is:", message)
            
        elif prompt=="l":  #shows user a list of files 
            print("List of files: 42.txt, 1015.txt")
            
            
        elif prompt=="d":   #allows user to select file
            file_name=((input("Enter the filename:\n")).lower())
            
            if file_name==("42.txt"): 
                print("The meaning of life is blah blah blah ...")
                
            
            elif file_name=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
                
            else:
                print("File not found")
                
            
            
        
    print("Goodbye!")  #prints only once user eexits program
        
        

    
    
    

    
    
main()

