#Piglatin
# Sofia Palmer
# April 2 2014

def toPigLatin(s):
    sentence = s.split(" ")   
    vowels = "aeiou"
    new_s = ""
    for j in range(0,len(sentence)): 
        word = sentence[j]
        if word[0] in vowels:
            new_s += word + 'way' + " "
        else:
            for i in range(0,len(word)):
                if word[i] in vowels:
                    break          
            new_s += word[i:] + 'a' + word[:i] + 'ay' + " "
    print(new_s)

def toEnglish (s):
    sentence = s.split(" ")   
    vowels = "aeiou"
    new_s = ""
    for j in range(0,len(sentence)):
        word = sentence[j]
        i = 0
        for i in range(0,len(word)):
            if word [i] in ("w"):
                new_s += word[:i] + " "
                break
        if (i >= len(word)- 1):
            x = len(word) - 3              
            while(word[x] != 'a'):
                x -= 1
                x = x + 1
                new_s += word[x:len(word)-2] + word[:x-1] + " "
    print(new_s)




