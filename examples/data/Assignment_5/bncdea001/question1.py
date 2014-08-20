# Assignment 5 Question 1
# BBS Program
#Dean Bunce
#12 April 2014
#BBT program


def main():
    
    
    #Create List to iterate through to to print the menu
    
    st=["Welcome to UCT BBS", "MENU", "(E)nter a message", "(V)iew message", "(L)ist files","(D)isplay file", "e(X)it"]
    for i in st: print(i)
    
    #Get input from user
    ans=input("Enter your selection: \n").upper()
    
    mess=""
    
    #Display menu until the user exist
    
    while ans!="X":
        
        #Get the message
        if ans=="E":
            mess=input("Enter the message: \n")
            
            for i in st:print(i)
            ans=input("Enter your selection: \n").upper()
        
        # To display message
        if ans=="V":
            if mess!="": print("The message is:",mess)
            else: print("The message is: no message yet")
                
            for i in st:print(i)
            ans=input("Enter your selection: \n").upper()        
            
        #Show list of files   
        if ans=="L":
            print("List of files: 42.txt, 1015.txt")
        
            for i in st:print(i)
            ans=input("Enter your selection: \n").upper()        
    
        #open and display files
        if ans=="D":
            file=input("Enter the filename: \n")
            if file=="42.txt":
                infile=open("42.txt","r")
                printo=infile.read()
                print(printo)
            elif file=="1015.txt":
                infile2=open("1015.txt","r")
                printo2=infile2.read()
                print(printo2)
            
            else: print("File not found")
        
            for i in st:print(i)
            ans=input("Enter your selection: \n").upper()       
    
    #Exit if ans is quit
       
    if ans=="X":
        print("Goodbye!")
    
    
    

main()