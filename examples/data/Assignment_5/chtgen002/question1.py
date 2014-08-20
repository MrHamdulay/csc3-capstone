"""
BBS using menu
Genevieve Brownyn Chetty (CHTGEN002)
16/04/2014
"""
sel="" #empty string initialised for selection
mes="" #empty string for message
txt42="The meaning of life is blah blah blah ..." #txt42 & txt1015 name of text files 42.txt & 1015.txt respectively
txt1015="Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
while((sel!='X') and (sel !='x')): #x could be lower or upper case
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it") #end of printing of menu. will be printed again until x is selected
    sel=input("Enter your selection:\n") #input of sel
    
    if((sel=='e') or (sel=='E')): #input of message
        mes=input("Enter the message:\n")    
    
    if((sel=='v') or (sel=='V')):
        if(mes==""): # if message string is empty
            print("The message is: no message yet")
        else:
            print("The message is:",mes)
    
    if((sel=='l') or (sel=='L')): #list file names
        print("List of files: 42.txt, 1015.txt")
    
    if((sel=='d') or (sel=='D')): #display "textfile" 
        fname=input("Enter the filename:\n")
        if(fname=="42.txt"):
            print(txt42)
        elif(fname=="1015.txt"):
            print(txt1015)
        else:
            print("File not found")

print("Goodbye!") #end


