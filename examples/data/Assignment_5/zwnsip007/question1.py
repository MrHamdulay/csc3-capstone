'''BBS programme 
Siphesihle Zwane 
15-04-14'''
choice=""
mess="no message yet"
while choice!="x":  
#staying with one argument    
    y=input("Welcome to UCT BBS"'\n'"MENU"'\n'"(E)nter a message"'\n'"(V)iew message"'\n'"(L)ist files"'\n'"(D)isplay file"'\n'"e(X)it"'\n'"Enter your selection:"'\n')
    y=y.lower() #need to change case 
    if y=="e":
        mess=input("Enter the message:"'\n')
    if y=="v":
        print("The message is:",mess)     
    if y=="l":
        print("List of files: 42.txt, 1015.txt")
    if y=="x":
        print("Goodbye!")
        break
    if y=="d":
        x=input("Enter the filename:"'\n')
        if x=="42.txt": #not creating file
            print("The meaning of life is blah blah blah ...")
            
        if x=="1015.txt":
            print("Computer Science class notes ... simplified","Do all work","Pass course","Be happy", sep='\n')
            
        if x!="42.txt" and x!="1015.txt":
            print("File not found")
        
    
    

