# test program for english/piglatin translator

import piglatin

a = input ("(E)nglish or (P)ig Latin?\n")
y = a[:1]
if y == 'E':
    v = input("Enter an English sentence:\n")
    t = piglatin.toPigLatin(v)
    print("Pig-Latin:")
    print(t)
elif y =='P':
    v = input("Enter a Pig Latin sentence:\n")
    t = piglatin.toEnglish(v)
    print("English:")
    print(t)
    

