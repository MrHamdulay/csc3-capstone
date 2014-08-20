"""
Assignment 7 - Question 1
program that will remove doubles from a list of strings
Jayan Smart
29 April 2014
"""

def main():
    strings = []
    print("Enter strings (end with DONE):")
    while True:
        string = input()
        #check for break variable in if true, break from loop
        if string == 'DONE': 
            break
        #check if word is repeated, if not add to list
        if string not in strings:
            strings.append(string)
    print("\nUnique list:")    
    for i in range(len(strings)):
        print(strings[i])
main()
