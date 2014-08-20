#TSHKAR003
# test program for english/piglatin translator

import piglatin

choiceS = input ("(E)nglish or (P)ig Latin?\n")
action = choiceS[:1]
if action == 'E':
    s = input("Enter an English sentence:\n")
    print("Pig-Latin:")
    new_s = piglatin.toPigLatin(s)    
    print(new_s)
elif action =='P':
    s = input("Enter a Pig Latin sentence:\n")
    print("English:")
    new_s = piglatin.toEnglish(s)    
    print(new_s)
    

