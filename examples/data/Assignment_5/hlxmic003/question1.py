# Michaela Heale
# Assignment 5 Question 1
# UCT BBS
import os

opt = ""
msg = "no message yet"
while (opt != 'X'):
    opt = (input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")).upper()
    if (opt == 'E'):
        # Allows user to enter a message
        msg = input("Enter the message:\n")
        
    elif (opt =='V'):
        # Allows user to read the saved message
        print("The message is:",msg)
        
    elif (opt == 'L'):
        # Prints a list of all files present in the directory
        print("List of files: ",end="")
        msg = ""
        filas = []
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith('.txt'):
                    filas.append(file)
        lng = len(filas)-1
        while lng>-1:
            msg += filas[lng]+", "
            lng-=1  
        count = len(msg) - 2
        print(msg[0:count])

    elif (opt == 'D'):
        # Displays the file chosen by the user
        file = input("Enter the filename:\n")
        if not (file == "1015.txt" or file == "42.txt"):
            print("File not found")
        else:
            file_obj = open(file,'r')
            print(file_obj.read())
            file_obj.close()
print("Goodbye!")
