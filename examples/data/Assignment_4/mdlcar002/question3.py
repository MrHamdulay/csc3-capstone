# testing program for english/piglatin translator

import piglatin

option = input ("(E)nglish or (P)ig Latin?\n")
choice = option[:1]
if choice == 'E':
    s = input("Enter an English sentence:\n")
    new_s = piglatin.toPigLatin(s)
    print("Pig-Latin:")
    print(new_s)
elif choice =='P':
    s = input("Enter a Pig Latin sentence:\n")
    new_s = piglatin.toEnglish(s)
    print("English:")
    print(new_s)
    

