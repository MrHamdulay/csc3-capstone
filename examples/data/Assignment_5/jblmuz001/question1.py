choice=""
msg=""
f = open('42.txt', 'r')
g = open('1015.txt','r')

def display_Menu():
  print("MENU")
  print("(E)nter a message")
  print("(V)iew message")
  print("(L)ist files")
  print("(D)isplay file")
  print("e(X)it")

def display():
    y="no message yet"
    while True:
        print("Welcome to UCT BBS")
        display_Menu()
        x=input("Enter your selection:\n")
        x=x.upper()
        if x=="E":
            y=input("Enter the message:\n")
        if x=="V":
            print("The message is: ", end="")
            print(y)
        if x=="L":
            print("List of files: 42.txt, 1015.txt")
        if x=="D":
            y=input("Enter the filename:\n")
            if y=="42.txt" :
                print(f.read())
                continue
            if y=="1015.txt":
                print(g.read())
                continue
            else:
                print("File not found")
                continue
        if x=="X":
            print("Goodbye!")
            break

display()