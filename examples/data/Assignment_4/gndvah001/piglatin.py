def toPigLatin (s):
    VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    words =  s.split()
    for word in words:
        if word[0] in VOWELS:
            print (word + "way", end=" ")
        elif word[1] in VOWELS:
            print (word[1:] + "a" + word[0] + "ay", end=" ")
        elif word[2] in VOWELS:
            print (word[2:] + "a" + word[0:2] + "ay", end=" ")