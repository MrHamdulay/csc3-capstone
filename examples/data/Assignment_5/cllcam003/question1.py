# BBS program
#CLLCAM003
#15/04/2014
task="f" #initial variable
while task!="X" or task!="x": #loop repeats menu unless exit is chosen 
                print("Welcome to UCT BBS")
                print("MENU")
                print("(E)nter a message")
                print("(V)iew message")
                print("(L)ist files")
                print("(D)isplay file")
                print("e(X)it")
                task=input("Enter your selection:\n") 
                if task=="E" or task=="e":
                                while task=="E" or task=="e":# allows us to seperate when their is a message and when there is not.
                                                message=input("Enter the message:\n")
                                                print("Welcome to UCT BBS")
                                                print("MENU")
                                                print("(E)nter a message")
                                                print("(V)iew message")
                                                print("(L)ist files")
                                                print("(D)isplay file")
                                                print("e(X)it")
                                                task=input("Enter your selection:\n")     
                                                if task=="V" or task=="v": # is message
                                                                print("The message is:",message)
                elif task=="V" or task =="v": # is not a message
                                print("The message is: no message yet")
                elif task=="L" or task=="l":
                                print("List of files: 42.txt, 1015.txt")
                elif task=="D" or task=="d":
                                filename=input("Enter the filename:\n")
                                if filename=="42.txt":
                                                print("The meaning of life is blah blah blah ...")
                                elif filename=="1015.txt":
                                                print("Computer Science class notes ... simplified")
                                                print("Do all work")
                                                print("Pass course")
                                                print("Be happy")
                                else: print("File not found")                
                elif task=="X" or task=="x":
                                break
print("Goodbye!") # if x is enetered as your option
        
        
        
        
        
        
   
                    
    
        
        
        
        