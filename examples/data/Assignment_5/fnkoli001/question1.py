# coding=utf-8

message = "no message yet"
files = {"42.txt": "The meaning of life is blah blah blah ...",
         "1015.txt": "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"}


def print_main_menu():
    print("""
Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
""", end='')
    uesr_input = input("Enter your selection:\n").upper()
    return uesr_input

#Inital input
user_input = print_main_menu()

while user_input != 'X':
    if user_input == 'E':
        message = input("Enter the message:")
    elif user_input == 'V':
        print("The message is:", message, end='')
    elif user_input == 'L':
        print("List of files:", ", ".join(file for file in files), end='')
    elif user_input == 'D':
        file = input("Enter the filename:\n")
        if file in files:
            print(files[file], end='')
        else:
            print("File not found", end='')
    else:
        print("Invalid Choice!", end='')

    #Recurring input
    user_input = print_main_menu()

print("Goodbye!", end='')