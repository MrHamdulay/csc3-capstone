'''Simple Bulletin Board System simulation
Mutali Mashamba
MSHMUT003
15 april 2014'''

# Print welcome message and Menu
welcome = '''Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it'''

msg = "no message yet"
while True:
    print(welcome)
    # Get input from user
    f = input("Enter your selection:\n")
    f = f.upper()    
    # Get messgae from user
    if f == "E":
        msg = input("Enter the message:\n")
    # View the message
    elif f == 'V':
        print("The message is:",msg)
    # View the items in the list
    elif f == 'L':
        print("List of files: 42.txt, 1015.txt")
    # View an item in the list of files
    elif f == 'D':
        file = input('Enter the filename:\n')
        if file == '1015.txt':
            print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
        elif file == "42.txt":
            print('The meaning of life is blah blah blah ...')
        else: print('File not found')
    # End the programme
    elif  f == 'X':
        print('Goodbye!')
        break
    # Be happy