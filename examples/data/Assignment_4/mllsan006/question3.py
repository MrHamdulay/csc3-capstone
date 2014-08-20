# test program for english/piglatin translator

import piglatin

c = input ("(E)nglish or (P)ig Latin?\n")
a = c[:1]
if a == 'E':
    s = input("Enter an English sentence:\n")
    new_s = piglatin.toPigLatin(s)
    print("Pig-Latin:")
    print(new_s)
elif a =='P':
    s = input("Enter a Pig Latin sentence:\n")
    new_s = piglatin.toEnglish(s)
    print("English:")
    print(new_s)
    

