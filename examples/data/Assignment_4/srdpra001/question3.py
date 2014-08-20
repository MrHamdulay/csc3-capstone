# test program for english/piglatin translator
"""
Prashanth Sridharan
SRDPRA001
Assignment 4
Question 03
"""
import piglatin

chc = input ("(E)nglish or (P)ig Latin?\n")
act = chc[:1]
if act == 'E':
    s = input("Enter an English sentence:\n")
    new_s = piglatin.toPigLatin(s)
    print("Pig-Latin:")
    print(new_s)
elif act =='P':
    s = input("Enter a Pig Latin sentence:\n")
    new_s = piglatin.toEnglish(s)
    print("English:")
    print(new_s)
    

