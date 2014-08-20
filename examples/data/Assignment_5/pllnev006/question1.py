# Program to simulate BBS
# Nevarr Pillay - PLLNEV006
# 12 April 2014

files = ["42.txt","1015.txt"]

def enter():
    mess2 = input("Enter the message:\n")
    return mess2
    
def view(mess):
    print("The message is:",mess)
    
def list():
    outfiles = ", ".join(files)
    print("List of files:",outfiles)
    
def display():
    name = input("Enter the filename:\n")
    try:
        infile = open(name,"r")
    
    except IOError:
        print("File not found")
    else:
        data = infile.read()
        print(data)
        
def exit():
    print("Goodbye!")
    return False
    
def main():    
    check = True    
    mess = "no message yet"
    while check:       
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        choice = input("Enter your selection:\n")
        choice = choice.upper()
        if choice == "E":
            mess = enter()
        elif choice == "V":
            view(mess)
        elif choice == "L":
            list()
        elif choice == "D":
            display()
        elif choice == "X":
            check = exit()
        
main()            
    
    