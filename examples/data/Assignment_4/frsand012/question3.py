import piglatin

choice = input ("(E)nglish or (P)ig Latin?\n")
action = choice[:1]
if action == 'E':
    a = input("Enter an English sentence:\n")
    new = piglatin.toPigLatin(s)
    print("Pig-Latin:")
    print(new)
elif action =='P':
    a = input("Enter a Pig Latin sentence:\n")
    new = piglatin.toEnglish(s)
    print("English:")
    print(new)
    

