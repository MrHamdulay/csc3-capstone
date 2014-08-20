def toPigLatin (s):
    words = s.split(' ')
    new_s = ""
    
    for word in words:
        if word[0] in 'aeiou':
            new_s = new_s + word + "way "
        else:
            end = ""
            while word and word[0] not in 'aeiou':
                end = end + word[0]
                word = word[1:]                 
                
            else:
                new_s = new_s + word + "a" + end + "ay "
        
    return new_s

def toEnglish (s):
    words = s.split(' ')
    new_s = ""
    
    for word in words:
        if 'a' in word:
            if word[len(word)-3:] == "way":
                new_s = new_s + word[:len(word)-3] + " "
            else:    
                word = word[:len(word)-2]
                start = ""
                while word[len(word)-1] not in 'aeiou':
                    start = start + word[len(word)-1]
                    word = word[:len(word)-1]                 
                new_s = new_s + start[::-1] + word[:len(word)-1] + " "
        else:
            new_s = new_s + word + " "
    return new_s