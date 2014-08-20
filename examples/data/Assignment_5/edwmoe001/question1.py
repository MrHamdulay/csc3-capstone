import os
def option(x):
    if x == "E":
        enter()
    elif x == "V":
        view()
    elif x == "L":
        list_files()
    elif x == "D":
        display()
    elif x == "X":
        exit()
    else:
        print("Enter your selection:")
        choice = input()
        choice = str.upper(choice)
        option(choice)        

def enter():
    global msg
    msg = input("Enter the message:\n")
    main()
    
def view():
    #global msg
    if "msg" in globals():
        print("The message is:", msg )
        main()
    else:
        print("The message is: no message yet")
        main()        

def list_files(): 
    directory =[]
    for file in os.listdir("./"):
        if file.endswith(".txt"):
            directory.append(file)
    directory[0], directory[1] = directory[1], directory[0]
    print("List of files:",", ".join(directory))
    main()
    
def display():
    file = input("Enter the filename:\n")
    if any(file in s for s in os.listdir("./")):
        f = open(file,mode='r')
        x = f.read()
        print(x)
        main()
    else:
        print("File not found")
        main()
    
def exit():
    print("Goodbye!")
    

def main():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    print("Enter your selection:")
    choice = str.upper(input())
    option(choice)
 
main()