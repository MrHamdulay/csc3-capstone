"""Assignment 5
Jadon Thomson
13-04-2014"""

def main(a):
    message = a
    print("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it")
    selection = input("Enter your selection: \n")
    selection = selection.upper()
    if selection == 'E':
        main(_enter())
    elif selection == 'V':
        print("The message is:",message)
        main(message)
    elif selection == 'L':
        print("List of files: 42.txt, 1015.txt")
        main(message)
    elif selection == 'D':
        _display()
        main(message)
    elif selection == 'X':
        print("Goodbye!")

def _enter():
    message = input("Enter the message: \n")
    return message

def _display():
    file_name = input("Enter the filename: \n")
    if file_name == '42.txt':
        #f = open('42.txt')
        #string = str(f.readlines())
        #print(string[2:-2:1])
        #f.close()
        print("The meaning of life is blah blah blah ... ")
    elif file_name == '1015.txt':
        #f = open('1015.txt')
        #string = (str(f.readlines(1)))[2:-4] + chr(13)
        #string += (str(f.readlines(2)))[2:-4] + chr(13)
        #string += (str(f.readlines(3)))[2:-4] + chr(13)
        #print(string)
        #f.close()
        print("Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy")
    else:
        print("File not found")
        

main('no message yet')