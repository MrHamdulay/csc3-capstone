
def enter():
    a=input("Enter the message:\n")
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    choice = input("Enter your selection:\n")
    if choice == 'E' or choice == 'e':
        return enter()
    elif choice == 'L' or choice == 'l':
        return list()
    elif choice == 'V' or choice == 'v':
        print("The message is:",a)
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        choice = input("Enter your selection:\n")
        if choice == 'E' or choice == 'e':
            return enter()
        elif choice == 'L' or choice == 'l':
            return list()   
        elif choice == 'D' or choice == 'd':
            return display()
        elif choice == 'X' or choice =='x':
            return exit()     
    elif choice == 'D' or choice == 'd':
        return display()
    elif choice == 'X' or choice =='x':
        return exit()     

def display():
    b = input("Enter the filename: ")
    if b == '1015.txt':
        print("\nComputer Science class notes ... simplified")
        print("Do all work")
        print("Pass course")
        print("Be happy")
    elif b == '42.txt':
        print("\nThe meaning of life is blah blah blah ...")
    else:
        print("\nFile not found")
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    choice = input("Enter your selection:\n")
    if choice == 'E' or choice == 'e':
        return enter()
    elif choice == 'L' or choice == 'l':
        return list()
    elif choice == 'V' or choice == 'v':
            return view()    
    elif choice == 'D' or choice == 'd':
        return display()
    elif choice == 'X' or choice =='x':
        return exit()    
      
def list():
    print("List of files: 42.txt, 1015.txt")
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")   
    choice = input("Enter your selection:\n")
    if choice == 'E' or choice == 'e':
        return enter()
    elif choice == 'L' or choice == 'l':
        return list()
    elif choice == 'V' or choice == 'v':
            return view()    
    elif choice == 'D' or choice == 'd':
        return display()
    elif choice == 'X' or choice =='x':
        return exit()   
    
def exit():
    print("Goodbye!")
     
    
def question():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    choice = input("Enter your selection:\n")
    if choice == 'E' or choice == 'e':
        return enter()
    elif choice == 'V' or choice == 'v':
        print("The message is: no message yet")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        choice = input("Enter your selection:\n")  
        if choice == 'E' or choice == 'e':
            return enter()
        elif choice == 'L' or choice == 'l':
            return list()
        elif choice == 'V' or choice == 'v':
                return view()    
        elif choice == 'D' or choice == 'd':
            return display()
        elif choice == 'X' or choice =='x':
            return exit()          
    elif choice == 'L' or choice == 'l':
        return list()
    elif choice == 'D' or choice == 'd':
        return display()
    elif choice == 'X' or choice =='x':
        return exit()
    return question()

question()

                
                
            
            
            
            

    
    