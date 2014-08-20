#A program that allows the user to enter a list of strings and print them in the same order without duplicates
#Author: Michelle Njoroge
#29 April 2014

#Define a function
def string():
    string=input("Enter strings (end with DONE):\n")
    liststrings=[] #create a list to store the strings
    while string!="DONE":
        if string not in liststrings:
            liststrings.append(string)
        string=input()
    print()
    print("Unique list:")
    for word in liststrings:
        print(word)
string()

        