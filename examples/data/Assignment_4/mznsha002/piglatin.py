#2 April 2014
#Shaun Muzenda
#Translating words from English to Pig Latin and vice a versa

def toPigLatin (s):
    
    pyg = 'ay'
    pyg2 = 'way'

    if len(s) > 0:
        lst = s.split()
        latin = []
        for item in lst:
            frst = item[0]
            scnd = item[1]
            if frst in 'aeiou':
                item = item + pyg2
            elif scnd in 'aeiou':
                item = item[1:] + 'a' + frst + pyg
            else:
                item = item[2:] + 'a' + frst+ scnd + pyg
            latin.append(item)
        return(' '.join(latin))
    
def toEnglish(s):
    sentence = s.split(" ")
    english = ""
    for word in sentence:
        c = 0
        for x in word:
            meow = -3 - c
            if word[meow] in ("aeiou"):
                break
            c = c + 1
        if word[-3:] == "way":
            word = word[:-3]
            
        elif word[-2:] == "ay" and word[-3] not in ("aeiou"):
            meow = -2 - c
            word = word[meow:-2] + word[:(meow - 1)]
        
        english = english + word + " "
    return english