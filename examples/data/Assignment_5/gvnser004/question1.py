""" Serayen Govender
Assignment 5 question 1
16 April 2014"""

print("Welcome to UCT BBS\nMENU")
#print title

inp=""
#option letter
file_42="The meaning of life is blah blah blah ..."
file_1015="Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
#file contents
mes=""
while inp!="x" and inp!="X":
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    inp=input("Enter your selection:\n")
    #options
    
    if(inp=="E" or inp=="e"):
        mes=input("Enter the message:\n")
    elif(inp=="V" or inp=="v"):
        if(mes==""):
            print("The message is: no message yet")
        else:
            print("The message is: ", mes)
    elif(inp=="L" or inp=="l"):
        print("List of files: 42.txt, 1015.txt")
    elif(inp=="D" or inp=="d"):
        file=input("Enter the filename:\n")
        if(file=="42.txt"):
            print (file_42)
        elif(file=="1015.txt"):
            print(file_1015)
        else:
            print("File not found")
print("Goodbye!")
         
# if and else statements for selection and action fro each selection