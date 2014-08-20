
import piglatin 
choice = input ("(E)nglish or (P)ig Latin?\n")
action = choice[:1]
if action == 'E':
    q = input("Enter an English sentence:\n")
    translated_q = piglatin.toPigLatin(q)
    print("Pig-Latin:")
    print(translated_q)
elif action =='P':
    q = input("Enter a Pig Latin sentence:\n")
    translated_q = piglatin.toEnglish(q)
    print("English:")
    print(translated_q)
    
