def main():
    BBS()
   
def BBS():
    message = "no message yet"
    command=""
    exitcommand={"x", "X"}
    while (command not in exitcommand):
        #this part is the main programme, it prints the possible responses for the options availiable 
        print ("Welcome to UCT BBS")
        print ("MENU")
        print ("(E)nter a message")
        print ("(V)iew message")
        print ("(L)ist files")
        print ("(D)isplay file")
        print ("e(X)it")
        #this asks and acesses an input to the function and prints an appropriate response
        command = input ("Enter your selection:\n")
        responses = {"E", "V", "L", "D", "X", "e", "v", "l", "d", "x"}
        the_42_txt = "The meaning of life is blah blah blah ..."
        the_1015_txt = ("Computer Science class notes ... simplified"+"\n"+"Do all work"+"\n"+"Pass course"+"\n"+"Be happy")        
        if command not in responses:
            print ("Enter a command")
        elif command == "D" or command == "d":
            file = input ("Enter the filename:\n")
            if file == "42.txt":
                print (the_42_txt)
            elif file == "1015.txt":
                print (the_1015_txt)
            else:
                print ("File not found")        
        elif command == "E" or command == "e":
            message = input ("Enter the message:\n")             
        elif command == "V" or command == "v":
            print ("The message is:", message)
        elif command == "L" or command == "l":
            print ("List of files: 42.txt, 1015.txt")   
        elif command == "x" or "X":# why is it treating x as a file input?ask tutor 
                print ("Goodbye!")        
       
main()