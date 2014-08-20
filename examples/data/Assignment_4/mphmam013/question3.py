# test program for english/piglatin translator

import piglatin

a = input ("(E)nglish or (P)ig Latin?\n")
x = a[:1]
if x == 'E':
    v = input("Enter an English sentence:\n")
    q = piglatin.toPigLatin(v)
    print("Pig-Latin:")
    print(q)
elif x =='P':
    v = input("Enter a Pig Latin sentence:\n")
    q = piglatin.toEnglish(v)
    print("English:")
    print(q)
    

