# Program to encrypt a string
# Nomsa Gamedze
# 7 May 2014

import sys
sys.setrecursionlimit (30000)

def encrypt(string, i):
    i = i
    a = len(string)
    if i < a:
        if string[i].isalpha():
            if string[i].islower():
                if string[i] != "z":
                    ind = ord(string[i]) +1
                    string[i] = chr(ind)
                    i += 1
                    encrypt(string, i)
                elif string[i] == "z":
                    string[i] = "a"
                    i += 1
                    encrypt(string, i)
        else:
            i += 1
            encrypt(string, i)
    return string

def main():
    string = input("Enter a message:"'\n')
    print("Encrypted message:")
    string = list(string)
    result = encrypt(string, 0)
    print("".join(result)) # prints the list of encrypted characters as a string

main()