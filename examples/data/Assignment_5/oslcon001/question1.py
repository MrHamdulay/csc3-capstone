#Simulation of a simple BBS
#Conor O'Sullivan
#15/04/2014


#main function - asks user for comand, askes for message & prints message
def main():
    

    
    message = "no message yet"
    command = ""
    files = ["42.txt", "1015.txt"]
    
    while command != "X":
    
        print("""Welcome to UCT BBS 
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it""")    
        
        command = input("Enter your selection:\n")
        command = command.upper()
        if command == "E":
            message = input("Enter the message:\n")
        elif command == "V":
            print("The message is: " + message)
        elif command == "L":
            list_files(files)
        elif command == "D":
            display(files)
    print("Goodbye!")
        

#List files
def list_files(files):
    
    files = (", ").join(files)
    print("List of files: " + files)


#Display file
def display(files):
    file_name = input("Enter the filename:\n")
    if file_name in files:
        infile = open(file_name, "r")
        line = infile.read()
        print(line)
    else: print("File not found")

main()