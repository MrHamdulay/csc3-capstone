#Keegan Naidoo
#NDXKEE009
#16 April 2014

x=True                       #Creates a boolean variable to enter and exit the programme
message='no message yet'     #Assigns default message

while(x==True):  #Enters the loop with boolean value
    
    print("Welcome to UCT BBS \n","MENU\n","(E)nter a message\n","(V)iew message\n","(L)ist files\n","(D)isplay file\n","e(X)it",sep='') # prints menu
    
    selec=input("Enter your selection:\n") # Inputs selection
    
    if(selec=='X' or selec=='x'):      #Selection to exit loop
        
        print("Goodbye!") 
        x=False
    
    elif(selec=='E' or selec=='e'):    #Selection to enter message
        
        message=input("Enter the message: \n")
        
    
    elif(selec=='V' or selec=='v'):    #Selection to print message
        
        print("The message is:",message)
    
    elif(selec=='l' or selec=='L'):    #Selection to display list
        
        list=print("List of files: 42.txt, 1015.txt")
    
    elif(selec=='d' or selec=='D'):    #Selection to search for text file
        
        file=input("Enter the filename:\n")
        
        if(file=='42.txt'):            #Search for text file
            
            print("The meaning of life is blah blah blah ...")
        
        elif(file=='1015.txt'):        #Search for text file
            
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy",sep='')
            
        else:
            
            print("File not found")