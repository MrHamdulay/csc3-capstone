# program to simulate a simple BBS(Bulletin Board Systems)
# Ali Goldstein
# 16 April 2014

#creating empty string for these variables
mess=" "
sel = " "

#printing these options until 'x' or 'X' is selected
while not sel == 'X' or  sel=='x':
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    sel=input("Enter your selection: \n") 
  
#each letter display different options. we seperate each option with if statements    
    if sel=='E' or sel =='e':
        mess=input("Enter the message: \n")
        
    elif sel=='V' or sel=='v':
        if mess!=" ":
            print("The message is:",mess)
        else:
            print("The message is: no message yet")
        
    elif sel == 'L' or sel =='l':
        print("List of files: 42.txt, 1015.txt")
    
    elif sel == 'D' or sel=='d':
        filename=input("Enter the filename: \n")
        if filename=='42.txt':
            print("The meaning of life is blah blah blah ...")
        elif filename=='1015.txt':
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else: 
            print("File not found")
            
 #if 'x' or 'X' is selected is prints "goodbye" an the break statement ends the while loop   
    elif sel == 'X' or sel=='x': 
        print("Goodbye!")    
        break
    


    
