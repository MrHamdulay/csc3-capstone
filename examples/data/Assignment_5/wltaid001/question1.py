"""Aiden Walton
WLTAID001
BBS system"""
import os
from sys import argv
#Give user options
def main():
    file1="The meaning of life is blah blah blah ..."
    file2="Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
    message="no message yet"
    while True:  
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        #ask for input
        ans=input("Enter your selection:\n")
        ans=ans.upper()
        if ans=="E":
            message=input("Enter the message:\n")
        elif ans=="V":
            print("The message is:", message)
        elif ans=="L":
            print ("List of files: 42.txt, 1015.txt")
        elif ans=="D":
            raw_input=input("Enter the filename:\n")
            if raw_input=="42.txt":
                print(file1)
            elif raw_input=="1015.txt":
                print(file2)
            else:
                print("File not found")
        elif ans=="X":
            print("Goodbye!")
            return False
            
main()
    
#execute option