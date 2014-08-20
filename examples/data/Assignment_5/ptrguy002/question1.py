from functools import *
global files
global msg
msg = ""
files = {"42.txt":"The meaning of life is blah blah blah ...",
         "1015.txt":"Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"}
inp = ""

def getInput():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    print("Enter your selection:")
    return input()

def L():
    print("List of files: " + reduce(lambda x, y: x+", "+y, files.keys()))

def E():
    global msg
    msg = input("Enter the message:\n")

def V():
    if (msg == ""):
        print("The message is: no message yet")
    else:
        print("The message is: " + msg)

def D():
    tmp = input("Enter the filename:\n")
    if tmp in files:
        print(files[tmp])
    else:
        print("File not found")

while(True):
    inp = getInput()
    if (inp == "x" or inp == "X"):
        print("Goodbye!")
        break
    if (inp == "l" or inp == "L"):
        L()
    if (inp == "v" or inp == "V"):
        V()
    if (inp == "d" or inp == "D"):
        D()
    if (inp == "e" or inp == "E"):
        E()
