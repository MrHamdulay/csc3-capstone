

import piglatin

choice = input ("(E)nglish or (P)ig Latin?\n")
option = choice[:1]
if option == "E":
    s = input("Enter an English sentence:\n")
    new_s = piglatin.toPigLatin(s)
    print("Pig-Latin:")
    print(new_s)
elif option =="P":
    s = input("Enter a Pig Latin sentence:\n")
    new_s = piglatin.toEnglish(s)
    print("English:")
    print(new_s)