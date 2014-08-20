# Gadziraiushe Bangure: BNGGAD001
#Assignment 5: Functions and flow of control mechanisms
# Written by ~Shay~
# Date: 18/04/2014
menu=("Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it")

print(menu)

choice=input("Enter your selection:\n")

choice=choice.capitalize()

file1="The meaning of life is blah blah blah ..."
file2="Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy"
msg="no message yet"

while choice:
    if choice=="E": msg=input("Enter the message:\n")
    if choice=="V": print("The message is:",msg)
    if choice=="L": print("List of files: 42.txt, 1015.txt")
    if choice=="D":
        name=input("Enter the filename:\n")
        if name=="42.txt": 
            print(file1)
        else:
            if name=="1015.txt": 
                print(file2)
                
            else: print("File not found")
            
    if choice=="X":
        print("Goodbye!")
        break
    
    print(menu)
    choice=input("Enter your selection:\n")
    
    choice=choice.capitalize()
