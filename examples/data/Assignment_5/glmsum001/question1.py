#GLMSUM001
#Sumayah Goolam Rassool
#15 April 2014

#-------------------------------------------MENU DISPLAY----------------------------------------------------

print("Welcome to UCT BBS")
print("MENU")
print("(E)nter a message")
print("(V)iew message")
print("(L)ist files")
print("(D)isplay file")
print("e(X)it")

#-------------------------------------------USER INPUT------------------------------------------------------
selection=input("Enter your selection:\n")
selection=selection.upper()#---------------converts user input to upper case

if selection=="X":
    print("Goodbye!")#--------------------exits program
    
message=""    
#------------------Continues to display menu and run through menu option as long as user does not exit-------

while selection!="X":
 
    
#--------------------------------Executes the command carried by each menu option---------------------------    
    if selection=="E":
        message=input("Enter the message:\n")                         #allows user to enter a message
            
    elif selection=="V":
        if message!="":
            print("The message is:",message) #allows user to view the message
        else:
            print("The message is: no message yet")
        
    elif selection=="L":
        print("List of files: 42.txt, 1015.txt")                                    #displays names of files that are available
        
    elif selection=="D":
        file_name=input("Enter the filename:\n")                   #allows user to view contents of desired file
        
        if file_name=="42.txt":
            print("The meaning of life is blah blah blah ...")
            
        elif file_name=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
            
            
        else:
            print("File not found")#----------------------informs user that requested file does not exist
    else:
        print("Invalid entry")#---------------------------validates the selection that the user inputs i.e anything other than E,V,L,D,X is invalid
    
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")   
    
    selection=input("Enter your selection:\n")
    selection=selection.upper()#---------------------------converts user input to uppercase
    if selection=="X":
        print("Goodbye!")    
    
