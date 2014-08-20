"""Question1, Assignment 5
Emma Jordi
15 april 2014"""

#define text files
text1="The meaning of life is blah blah blah ..."
text2= "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"


#define homescreen page
def homescreen():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
#Print out welcome msg and selections    
homescreen()
    #get input

selection= input("Enter your selection:\n")
selection= selection.capitalize() #CHECKED

while selection!= "X":
    
    #set default message
    message="no message yet"    
    
    if selection=="E":
              
        message=input("Enter the message:\n")
        homescreen()        
        selection= input("Enter your selection:\n")
        selection= selection.capitalize()
             
      
        if selection=="V":
            print("The message is:",message)
        elif message=="":
            print("The message is: no message yet") 
            
    elif selection=="V":
        
        print("The message is:",message)
    
    elif selection=="L":
        print("List of files: 42.txt, 1015.txt",)#huh??
        
    elif selection== "D":
        
        filename= input("Enter the filename:\n")
        if filename=="42.txt":
            print(text1)
        elif filename=="1015.txt":
            print(text2)
        else:
            print("File not found")
        
    #Print out welcome msg and selections
    homescreen()

    #get input

    selection= input("Enter your selection:\n")
    selection= selection.capitalize() #CHECKED

            
else:
    print("Goodbye!")
 




    

