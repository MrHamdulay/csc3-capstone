# Question 3 piglatin

import piglatin

choice = input ("(E)nglish or (P)ig Latin?\n")
action = choice[:1]
if action == 'E':
    d = input("Enter an English sentence:\n")
    new_d = piglatin.toPigLatin(d)
    print("Pig-Latin:")
    print(new_d)
elif action =='P':
    d = input("Enter a Pig Latin sentence:\n")
    new_d = piglatin.toEnglish(d)
    print("English:")
    print(new_d)
    

