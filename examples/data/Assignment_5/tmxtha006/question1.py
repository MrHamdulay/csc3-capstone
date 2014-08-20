"""program to simulate a simple Bulleting Board System
Hebert Tema-TMXTHA006
13 April 2014"""

#initialize the variables    
msg = "no message yet"   
decision="E"


while decision in "EVLDX":                          #proceed into the while loop only if the condition is met
    decision = (input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")).upper()    #get an input from the use and make it uppercase
    
    #perform the coputation chosen and return the output
    if decision == "E":
        msg = input("Enter the message:\n")

    elif decision == "V":
        print("The message is:" ,msg)

    elif decision == "L": 
        #import os.path
        print("List of files: ",end="")
        print("42.txt", "1015.txt", sep=", ")          ##
        #for file in os.listdir("."):
            #if file.endswith(".txt"):
                #print(" ",file,end="")
        #print("")

    elif decision == "D":
        import os.path
        f_name=input("Enter the filename:\n")
        if os.path.isfile(f_name):                  #boolean expression to search if the file exist
            infile=open(f_name, "r")                #open the filr in read mode
            print(infile.read())
        else: print("File not found")   
    
    elif decision == "X":    #X is an input for breaking out the loop
        print("Goodbye!") 
        break
